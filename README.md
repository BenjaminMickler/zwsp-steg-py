# zwsp-steg-py
Zero-Width Space Steganography. Encodes and decodes hidden messages as non printable/readable characters.
This repository is a modification of [zwsp-steg-py](), which is a Python porting of [zwsp-steg-js](https://github.com/offdev/zwsp-steg-js).
All credits to [offdev](https://github.com/offdev)!
Every modification made by Benjamin Mickler and everything added by Benjamin Mickler is subject to copyright, Benjamin Mickler 2022.

### Modifications
- added AES 128 bit encryption
- added option to merge with string
- added file handling options
- added option to copy to clipboard

### Installation
```bash
$ pip install zwsp-steg-py
```

### Usage Example
```.py
import zwsp_steg

encoded = zwsp_steg.encode('hidden message')
decoded = zwsp_steg.decode(encoded)

print(decoded)  # hidden message
```
See `example.py` for more examples.


Note that decoding a message will ignore all non 'special' characters. That means if you hide your message within a readable string, and decode the whole string, you will only return the hidden message.

### Parameters
You can use different sets of characters in different encoding / decoding modes.

```.py
import zwsp_steg

zwsp_steg.encode('hidden message', zwsp_steg.MODE_ZWSP)
zwsp_steg.encode('hidden message', zwsp_steg.MODE_FULL)
```

#### Character sets used
- **MODE_ZWSP**: Zero-Width Space (\u200b), Zero-Width Non-Joiner (\u200c), Zero-Width Joiner (\u200d)
- **MODE_FULL**: All MODE_ZWSP characters, Left-To-Right Mark (\u200e), Right-To-Left Mark (\u200f)

### License
[MIT](https://opensource.org/licenses/MIT)
