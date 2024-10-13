from lists import alphabet
from art import caesar_logo

caesar_logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

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
