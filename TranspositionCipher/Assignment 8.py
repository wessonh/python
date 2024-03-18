# https://www.nostarch.com/crackingcodes (BSD Licensed)

import random, sys, transpositionEncrypt, transpositionDecrypt

def main():
    random.seed(42) # set the random "seed" to a static value

    for i in range(20): # test 20 times
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        message = list(message)
        random.shuffle(message)
        message = ''.join(message)

        print('Test #%s: "%s..."' % (i + 1, message[:50]))

        for key in range(1, int(len(message) /2)):
            encrypted = transpositionEncrypt.encryptMessage(key, message)
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted)

            if decrypted != message:
                print('Mismatch with key %s and message %s.' % (key, message))
                print('Decrypted as: ' + decrypted)
                sys.exit()

    print('Transposition cipher test passed.')

if __name__ == '__main__':
    main()
