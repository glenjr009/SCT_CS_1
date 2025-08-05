# My first attempt at a Caesar Cipher tool.
# Simple but gets the job done quicker.
# Caesar Cipher tool which help (e)encrypt and (d)decrypt text with the help of an a shift key.
# Shift Value is the key to (d)decrypt the (e)encrypted text 
# Author [Glen.F] aka [cyb3rPh03n1x]

def cipher(text, shift, mode):
    result = ""
    
    # Decryption is just a negative shift
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if 'a' <= char <= 'z':
            start = ord('a')
            shifted = (ord(char) - start + shift) % 26
            result += chr(shifted + start)
        elif 'A' <= char <= 'Z':
            start = ord('A')
            shifted = (ord(char) - start + shift) % 26
            result += chr(shifted + start)
        else:
            # Leave other characters alone
            result += char
            
    return result

def main():
    print("\n ***_CAESAR CIPHER PROGRAM_***")
    
    while True:
        choice = input("Enter '(e)' to encrypt an plain text, '(d)' to decrypt an ecrypted text, 'q' to quit the program: ").lower()
        
        if choice == 'q':
            print("Goodbye Mate!")
            break
            
        if choice not in ['e', 'd']:
            print("Invalid choice.")
            continue
        
        msg = input("Enter your message: ")
        
        # Make sure the shift value is a number
        while True:
            try:
                shift_val = int(input("Enter the shift value: "))
                break
            except ValueError:
                print("Must be a number.")
        
        if choice == 'e':
            encrypted = cipher(msg, shift_val, 'encrypt')
            print(f"Encrypted Message: {encrypted}")
        else:
            decrypted = cipher(msg, shift_val, 'decrypt')
            print(f"Decrypted : {decrypted}")

if __name__ == "__main__":

    main()
