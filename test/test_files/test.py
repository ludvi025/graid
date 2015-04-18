
def makeKeyTA(alphabet):
    import random
    return ''.join(sorted(alphabet, key=lambda x: random.random()))

def encryptMsgTA(plaintext, key, alphabet):
    return ''.join(map(lambda ch: key[alphabet.find(ch)] if ch in alphabet else '', plaintext.lower()))

def decryptMsgTA(ciphertext, key, alphabet):
    return encryptMsgTA(ciphertext, alphabet, key)


alphabet = 'abcdefghijklmnopqrstuvwxyz.,!? '
msg = 'The quick, brown fox jumped over the.. #lazy dog!'
key = makeKey(alphabet)
emsg = encryptMsg(msg, key, alphabet)
emsgta = encryptMsgTA(msg, key, alphabet)
dmsg = decryptMsg(emsg, key, alphabet)
dmsgta = decryptMsgTA(emsgta, key, alphabet)

print("Alphabet:    ", alphabet)
print("Key:         ", key)
print("Text:        ", msg)
print()
print("Encrypted:   ", emsg)
print("Encrypted TA:", emsgta)
print()
print("Decrypted:   ", dmsg)
print("Decrypted TA:", dmsgta)

