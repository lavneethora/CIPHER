# Caesar Cipher

## Overview

This project implements a Caesar Cipher, a type of substitution cipher where each letter in the plaintext is shifted by a certain number of positions in the alphabet. The Caesar Cipher is a simple yet classic encryption technique that has been used for centuries, dating back to Julius Caesar, who is credited with its creation.

In this Python program, the user can both encrypt and decrypt messages by specifying the shift amount. The program supports the wrapping of letters at the ends of the alphabet and can handle both upper and lower-case inputs.

## Features

- **Encryption**: Shift the letters of a message forward by a specified number of positions in the alphabet.
- **Decryption**: Shift the letters of an encrypted message backward by the same number of positions to reveal the original message.
- **Bidirectional Input Handling**: The user can either encrypt or decrypt a message in the same run.
- **Case Preservation**: The case of letters (upper/lower) is preserved during the encryption and decryption processes.
- **Non-letter Characters**: Characters that are not part of the alphabet (e.g., numbers, spaces, punctuation) remain unchanged during encryption/decryption.

## How It Works

1. The user provides a message they wish to encrypt or decrypt.
2. The user specifies a shift value (the number of positions to move each letter).
3. The program shifts each letter by the specified amount while preserving the non-letter characters.
4. If the user selects encryption, the letters are shifted forward; if decryption is chosen, the letters are shifted backward.

## Encryption Example

- **Input**: `"hello"`
- **Shift**: `3`
- **Output**: `"khoor"`

## Decryption Example

- **Input**: `"khoor"`
- **Shift**: `3`
- **Output**: `"hello"`

## Installation and Running

1. **Clone the Repository**:
```bash
git clone https://github.com/lavneethora/Hangman.git
```

2. **Navigate to the Project Directory**:
```bash
cd Hangman
```

3. **Run the Game**:
```bash
python hangman.py
```

## Sample Execution

```bash
Welcome to Caesar Cipher!
Would you like to encrypt or decrypt a message? (Type 'encrypt' or 'decrypt'): encrypt
Enter your message: hello
Enter the shift number: 3
Here is your encrypted message: khoor

Would you like to encrypt or decrypt another message? (Type 'yes' or 'no'): no
Goodbye!
```

## Code Breakdown

- **Cipher Function**: The core function of this program handles both encryption and decryption based on the user’s choice.
- **Shift Logic**: Letters are shifted based on the ASCII values of characters, which allows both upper and lower case letters to be processed.
- **Non-alphabetic Handling**: Non-alphabetic characters (such as spaces or punctuation) are left unchanged.

## Future Enhancements

- **Dynamic Shift Calculation**: Automatically detect the shift value for decryption based on frequency analysis of letters in the encrypted message.
- **Multiple Ciphers**: Expand the project to include other types of ciphers (e.g., Vigenère, Atbash).
- **Graphical User Interface**: Add a GUI for easier use without requiring terminal input.
- **Support for Multi-language Alphabets**: Extend the cipher to work with non-English alphabets.

## License

- This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions
- Feel free to submit issues or pull requests for any improvements or bug fixes.

## Author

- Lavneet Hora
- Sophomore @ Texas Tech University
- Computer Science
