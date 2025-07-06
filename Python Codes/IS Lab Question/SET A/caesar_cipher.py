"""
Write a program to encrypt and decrypt text using the Caesar cipher.
"""
def caesar(text, shift, mode='encrypt'):
    if mode == 'decrypt':
        shift = -shift
    result = ""

    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char
    return result

# Input
msg = input("Enter text: ")
s = int(input("Enter shift: "))

enc = caesar(msg, s, 'encrypt')
print("Encrypted:", enc)

dec = caesar(enc, s, 'decrypt')
print("Decrypted:", dec)
