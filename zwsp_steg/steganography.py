try:
    import pyperclip
except:
    pyperclip = False
try:
    from cryptography.fernet import Fernet
except:
    Fernet = False

MODE_ZWSP = 0
MODE_FULL = 1

ZERO_WIDTH_SPACE = '\u200b'
ZERO_WIDTH_NON_JOINER = '\u200c'
ZERO_WIDTH_JOINER = '\u200d'
LEFT_TO_RIGHT_MARK = '\u200e'
RIGHT_TO_LEFT_MARK = '\u200f'

list_ZWSP = [
    ZERO_WIDTH_SPACE,
    ZERO_WIDTH_NON_JOINER,
    ZERO_WIDTH_JOINER,
]

list_FULL = [
    ZERO_WIDTH_SPACE,
    ZERO_WIDTH_NON_JOINER,
    ZERO_WIDTH_JOINER,
    LEFT_TO_RIGHT_MARK,
    RIGHT_TO_LEFT_MARK,
]

def create_key(filename=None):
    key = Fernet.generate_key()
    if filename:
        with open(filename, "wb") as key_file:
            key_file.write(key)
    return key

def key_file(filename):
    with open(filename, "rb") as f:
        key = f.read()
    return key

def get_padding_length(mode):
    return 11 if mode == MODE_ZWSP else 7  # Keep padding as small as possible


def to_base(num, b, numerals='0123456789abcdefghijklmnopqrstuvwxyz'):
    """
    Python implementation of number.toString(radix)
    Thanks to jellyfishtree from https://stackoverflow.com/a/2267428
    """
    return ((num == 0) and numerals[0]) or (to_base(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])


def encode(message, key=None, string=None, copy=False, input_file=None, output_file=None, mode=MODE_FULL):
    if not isinstance(message, str):
        raise TypeError('Cannot encode {0}'.format(type(message).__name__))
    if key:
        f_obj = Fernet(key)
        message = f_obj.encrypt(message.encode()).decode()
    alphabet = list_ZWSP if mode == MODE_ZWSP else list_FULL
    padding = get_padding_length(mode)
    encoded = ''

    if (len(message) == 0):
        return ''

    for message_char in message:
        code = '{0}{1}'.format('0' * padding, int(str(to_base(ord(message_char), len(alphabet)))))
        code = code[len(code) - padding:]
        for code_char in code:
            index = int(code_char)
            encoded = encoded + alphabet[index]
    if input_file:
        with open(input_file) as f:
            string = f.read()
    if output_file:
        with open(output_file, "w") as f:
            f.write(encoded+string)
    if copy:
        if not pyperclip:
            print("Can not copy, please install pyperclip")
        else:
            pyperclip.copy(encoded+string)
    return encoded+(string if string else "")


def decode(message, key=None, input_file=None, mode=MODE_FULL):
    if not isinstance(message, str):
        raise TypeError('Cannot decode {0}'.format(type(message).__name__))
    if input_file:
        with open(input_file) as f:
            message = f.read()
    alphabet = list_ZWSP if mode == MODE_ZWSP else list_FULL
    padding = get_padding_length(mode)
    encoded = ''
    decoded = ''

    for message_char in message:
        if message_char in alphabet:
            encoded = encoded + str(alphabet.index(message_char))

    if (len(encoded) % padding != 0):
        raise TypeError('Unknown encoding detected!')

    cur_encoded_char = ''

    for index, encoded_char in enumerate(encoded):
        cur_encoded_char = cur_encoded_char + encoded_char
        if index > 0 and (index + 1) % padding == 0:
            decoded = decoded + chr(int(cur_encoded_char, len(alphabet)))
            cur_encoded_char = ''
    if key:
        f_obj = Fernet(key)
        decoded = f_obj.decrypt(decoded.encode()).decode()
    return decoded
