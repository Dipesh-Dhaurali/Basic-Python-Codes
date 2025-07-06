"""
Write a program to implement RSA Algorithm.
"""
# Import required module
from sympy import isprime
import math

# Function to find gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find modular inverse of e under mod phi
def modinv(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

# RSA Key Generation
def generate_keys(p, q):
    if not (isprime(p) and isprime(q)):
        raise ValueError("Both numbers must be prime.")

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    # Compute d
    d = modinv(e, phi)

    return ((e, n), (d, n))

# Encryption
def encrypt(message, public_key):
    e, n = public_key
    cipher = [(ord(char) ** e) % n for char in message]
    return cipher

# Decryption
def decrypt(cipher, private_key):
    d, n = private_key
    plain = [chr((char ** d) % n) for char in cipher]
    return ''.join(plain)

# Example usage
p = 17
q = 19
public_key, private_key = generate_keys(p, q)

message = input("Enter message: ")
encrypted = encrypt(message, public_key)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, private_key)
print("Decrypted:", decrypted)
