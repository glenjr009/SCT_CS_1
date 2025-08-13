# My first attempt at a Caesar Cipher tool.
# Simple but gets the job quicker.
# Caesar Cipher tool which help (e)encrypt and (d)decrypt text with the help of an a shift key.
# Shift Value is the key to (d)decrypt the (e)encrypted text
# Created by [Glen.F] aka [cyb3rPh03n1x]

from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

def cipher(text: str, shift: int, mode: str) -> str:
    """
    Encrypts or decrypts a text using the Caesar Cipher.

    Args:
        text (str): The message to process.
        shift (int): The number of positions to shift.
        mode (str): 'encrypt' or 'decrypt'.

    Returns:
        str: The processed message.
    """
    result = ""
    
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
            result += char
            
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    """Handles the web page for the cipher tool."""
    result = ""
    if request.method == 'POST':
        text = request.form.get('text')
        try:
            shift = int(request.form.get('shift'))
        except (ValueError, TypeError):
            shift = 0
        mode = request.form.get('mode')
        result = cipher(text, shift, mode)
    
    return render_template('index.html', result=result)

# This part is only for local testing and will be ignored by PythonAnywhere's web server
if __name__ == "__main__":
    app.run(debug=True)
