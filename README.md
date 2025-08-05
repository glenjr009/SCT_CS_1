    Caesar Cipher Tool 🔒
A simple command-line tool for encrypting and decrypting messages using the classic Caesar Cipher algorithm. This project was created as an introduction to cryptography and basic Python programming concepts for my cybersecurity internship.

Features ✨
Encryption and Decryption: Easily switch between encrypting and decrypting a message.

Customizable Shift: Use any integer value as the shift key.

Case Preservation: The program maintains the original casing of letters.

Handles Non-Alphabetic Characters: Punctuation, spaces, and numbers are preserved and not altered.

User-Friendly Interface: Clear prompts guide the user through the process.

Robust Input Handling: The program validates user input for the shift value, preventing errors.

How to Use 🚀
Clone the Repository:

Bash

git clone https://github.com/glenjr009/SCT_CS_1.git
Navigate to the Project Directory:

Bash

cd [SCT_CS_1.git]
Run the Program:

Bash

python caesar_cipher.py
Follow the Prompts: The program will ask you to choose between encrypting or decrypting, enter a message, and provide a shift value.

Example 💡
Here is a sample interaction with the tool:

--- Caesar Cipher ---
Enter 'e' to encrypt, 'd' to decrypt, 'q' to quit: e
Enter your message: Hello, World!
Enter the shift value: 3
Encrypted: Khool, Zruog!

--- Caesar Cipher ---
Enter 'e' to encrypt, 'd' to decrypt, 'q' to quit: d
Enter your message: Khool, Zruog!
Enter the shift value: 3
Decrypted: Hello, World!

*Future Improvements* 🚧
Implement more complex ciphers like the Vigenère Cipher.

Add a feature to perform a brute-force attack on an encrypted message.

Create a graphical user interface (GUI) for a better user experience.