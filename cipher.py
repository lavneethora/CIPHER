from lists import alphabet
from art import caesar_logo

def caesar():
    if starting_text == "encode":
        def encrypt(user_text, user_shift):
            for letter in user_text:
                position = alphabet.index(letter)
                new_position = position + user_shift
                encrypted_letter = alphabet[new_position]
                encrypted_text.append(encrypted_letter)
            cipher = ''.join(encrypted_text)
            print(cipher)
        encrypt(user_text = text, user_shift = shift)
        
    elif starting_text == "decode":
        def decrypt(cipher_text, user_shift):
            for letter in cipher_text:
                position = alphabet.index(letter)
                new_position = position - user_shift
                decrypted_letter = alphabet[new_position]
                decrypted_text.append(decrypted_letter)
            decode = ''.join(decrypted_text)
            print(decode)
        decrypt(cipher_text = text, user_shift = shift)
         
program_end = False
while not program_end:
    print(caesar_logo)
    starting_text = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    encrypted_text = []
    decrypted_text = []
    cipher = ''
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    shift = shift % 26
        
    caesar()     
        
    restart_program = input("Type 'Y' if you want to go again. Otherwise type 'N'. ").upper()
    if restart_program == "N":
        program_end = True
        print("Program Closing. Goodbye!!")   