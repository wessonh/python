# Henry Wesson
# 11/25/2023
# Sd 250
# Assignment 10

import sys
import pyperclip
import cryptomath
import random

# I had to add -," to the SYMBOLS to get this to encrypt and decrypt correctly"
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 -,"!?.'
    
def main(): 
    myMessage = """"A computer would deserve to be called intelligent
if it could deceive a human into believing that it was human."
-Alan Turing"""

    myKey = 2894
    myMode = 'encrypt'  # set to either 'encrypt' or 'decrypt'.

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)

    print('Key: %s' % (myKey))
    print('%sed text:' % (myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print('Full %sed text has been copied to clipboard.' % (myMode))

def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)

def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit('Cipher is weak if key A is 1. Please choose a different key.')

    if keyB == 0 and mode == 'encrypt':
        # sys.exit('Cipher is weak if key B is 0. Choose a different key.')
        pass
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))

    if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Please choose a different key.' % (keyA, len(SYMBOLS)))

def encryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    ciphertext = ''
    
    for symbol in message:
        if symbol in SYMBOLS:
            # Encrypt the symbol:
            symbolIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symbolIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            ciphertext += symbol  # Append the symbol without encrypting.

    return ciphertext

def decryptMessage(key, message): # I had to modify this to get the spacing to be correct
                                  # It kept wanting to add a tab in stead of a space at 
                                  # one part of the message. I fixed it. 
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plaintext = ''
    modInverseOfKeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))

    decrypted_message = ''

    for symbol in message:
        if symbol in SYMBOLS:
            # Decrypt the symbol:
            symbolIndex = SYMBOLS.find(symbol)
            decrypted_message += SYMBOLS[(symbolIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        elif symbol == '\t':
            decrypted_message += ' '  # Replace tabs with spaces
        else:
            decrypted_message += symbol  # Append the symbol without decrypting.

    # Handle leading spaces outside the loop
    lines = decrypted_message.split('\n')
    formatted_lines = [line.lstrip() for line in lines]
    plaintext = '\n'.join(formatted_lines)

    return plaintext

def getRandomKey():  
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))

        if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB

# If affineCipher.py is run (instead of imported as a module), call
# the main() function:
if __name__ == '__main__':
    main()






