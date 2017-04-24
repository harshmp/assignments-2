import base64

def encrypt(message, key):
    cipherChars = []
    for i in range(len(message)):
        currentKey = key[i % len(key)]
        currentChar = chr(ord(message[i]) + ord(currentKey) % 256)
        cipherChars.append(currentChar)

    ciphertext = "".join(cipherChars)
    return ciphertext

def decrypt(ciphertext, key):
    plainChars = []
    for i in range(len(ciphertext)):
        currentKey = key[i % len(key)]
        currentChar = chr((256 + ord(ciphertext[i]) - ord(currentKey)) % 256)
        plainChars.append(currentChar)

    plaintext = "".join(plainChars)
    return plaintext

def overload(text1, text2, flag):
    if flag is True:
        output = encrypt(text1, text2)
        return output
    else:
        output = decrypt(text1, text2)
        return output

message = raw_input("Enter a message: ")
key = raw_input("Enter a key: ")

ciphertext = overload(message, key, True)
gibberish = base64.urlsafe_b64encode(ciphertext)
print(gibberish)

plaintext = overload(ciphertext, key, False)
print(plaintext)
