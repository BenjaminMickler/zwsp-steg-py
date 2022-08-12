import zwsp_steg

# using a key stored in a variable
key = zwsp_steg.create_key()
encoded = zwsp_steg.encode('hidden message', string="hello world", key=key)
print(encoded)
decoded = zwsp_steg.decode(encoded, key=key)
print(decoded)

print("---------------------------------")

# using a key stored in a file
key = zwsp_steg.create_key(filename="key.key")
encoded = zwsp_steg.encode('hidden message', string="hello world", key=zwsp_steg.key_file("key.key"))
print(encoded)
decoded = zwsp_steg.decode(encoded, key=zwsp_steg.key_file("key.key"))
print(decoded)

print("---------------------------------")

# no encryption but copy to clipboard
encoded = zwsp_steg.encode('hidden message', string="hello world", copy=True)
print(encoded)
decoded = zwsp_steg.decode(encoded)
print(decoded)