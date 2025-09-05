from Crypto.Cipher import ChaCha20
import os

# Ce ne sont pas les bonnes valeurs
plaintext = b"Bob."
key = os.urandom(32)
nonce = os.urandom(12)

# Objet cipher
cipher = ChaCha20.new(key=key, nonce=nonce)
ciphertext = cipher.encrypt(plaintext)