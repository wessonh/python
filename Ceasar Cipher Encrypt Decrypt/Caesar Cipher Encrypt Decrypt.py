#Henry Wesson
#SD 250
#11/3/2023
#Caesar Cipher - HANDLES THE SPACES VERSION

# This program allow the user to encrypt or decrypt text using a 3 letter shift.
# you can choose to encrypt, decrypt or press no to quit. This menu ignores
# leading and trailing white spaces and is not case sensitive. Encrypting
# and decrypting will ignore non letter characters, ignores trailing
# white spaces and is not case-sensitive.

# Any spaces entered between words will be converted to % symbols in
# the encrypted message. Decrypting will revert any symbols back to
# blank spaces. Any punctuation, and non-alphabetic characters
# will not show up in the encrypted or decrypted text.
# Uses for loops and while loops.



#this function ecrpyts input using a three letter shift
def encrypt(input):
    cipher=''
    for letter in input:                  #for the letters in the input
        if letter.isalpha():              #if input is alphabetic character
            letter = letter.lower()       #makes lowercase so its not case sensistive
            new_shift = ord(letter) + 3   #three letter shift
            if new_shift > ord('z'):      #if new_shift goes past z
                new_shift -= 26           #restarts at beginning of alphabet
            cipher += chr(new_shift)      #add new_shift to cipher
        elif letter.isspace():            #else if letter is blank space
            cipher += '%'                 #replace space with %   
    return cipher                         #returns the cipher

#this function ecrypts input using a three letter shift back
def decrypt(input):
    text=''
    for letter in input:                  #for the letter in the input
        if letter.isalpha():              #if input is alphabetic character
            letter = letter.lower()       #makes lowercase so its not case sensitive
            new_shift = ord(letter) - 3   #three letter shift
            if new_shift < ord('a'):      #if new_shift goes past a
                new_shift += 26           #restarts at end of alphabet
            text += chr(new_shift)        #adds new shift to text
        elif letter == '%':               #else if letter is %
            text += ' '                   #replace % with a space
    return text                           #returns the decrypted text

def menu():
    quit_program = False         #sets quit program to false
    while not quit_program:      #main while loop of menu, while quit_program is false
        option = input('Would you like to encrypt or decrypt a text? \n("encrypt", "decrypt", or "no" to quit)\n: ').strip().lower() 
        if option == 'encrypt':  #if user types encrypt asks for text, calls encrypt and prints code
            input_text = input('Please enter the text you want to encrypt \n(case insensitive and will ignore spaces and non-alphabet characters)\n: ').strip().lower()
            encrypted = encrypt(input_text)
            print('Encrypted text: ', encrypted)
        elif option =='decrypt': #if user types decrypt asks for text, calls decrypt and prints text
            input_text = input('Please enter the text you want to decrypt \n(case insensitive and will ignore spaces and non-alphabet characters)\n: ').strip().lower()
            decrypted = decrypt(input_text)
            print('Decrypted text: ', decrypted)
        elif option == 'no':            #if user types no, quits program
            print('Goodbye')
            quit_program = True         #sets quit program to true
        else:                           #otherwise error message
            print('Error! Please make a valid choice! \n("encrypt", "decrypt", or "no" to quit)\n')
        
menu() # calls menu function and runs the program        
            
        
        
