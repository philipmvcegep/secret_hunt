from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def rsa_encrypt(plaintext, public_key):
    """
    Encrypts a plaintext message using an RSA public key.
    """
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(plaintext.encode())
    return ciphertext

key = RSA.generate(1024)
public_key_obj = key.publickey()  
phi_n = (key.p - 1) * (key.q - 1)

print("Generated a 1024-bit key pair.")
print(f"Public Key (N, e): ({public_key_obj.n}, {public_key_obj.e})")

# Pas le bon message
plaintext_message = 'o'
encrypted_data = rsa_encrypt(plaintext_message, public_key_obj)

print(f'encrypted_text: {encrypted_data}')
print(f'phi: {phi_n}')