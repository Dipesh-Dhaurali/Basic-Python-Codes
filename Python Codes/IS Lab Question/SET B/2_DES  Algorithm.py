"""
Write a program to encrypt and decrypt plaintext using DES.
"""
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

# Key must be 8 bytes
key = b'abcdefgh'

# Function to encrypt plaintext using DES
def encrypt_des(plaintext):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext.encode(), DES.block_size)
    encrypted_text = des.encrypt(padded_text)
    return binascii.hexlify(encrypted_text).decode()  # Convert bytes to hex string

# Function to decrypt ciphertext using DES
def decrypt_des(ciphertext_hex):
    des = DES.new(key, DES.MODE_ECB)
    encrypted_bytes = binascii.unhexlify(ciphertext_hex)  # Convert hex string to bytes
    decrypted_padded = des.decrypt(encrypted_bytes)
    return unpad(decrypted_padded, DES.block_size).decode()

# Example usage
plain_text = input("Enter plain text to encrypt: ")

# Encrypt
cipher_text = encrypt_des(plain_text)
print("Encrypted (hex):", cipher_text)

# Decrypt
decrypted_text = decrypt_des(cipher_text)
print("Decrypted:", decrypted_text)
