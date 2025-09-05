def vigenere_encrypt(plaintext, key):
    encrypted_text = ""
    key_index = 0
    plaintext = plaintext.upper()
    key = key.upper()
    key_length = len(key)

    for char in plaintext:
        if 'A' <= char <= 'Z':
            p_val = ord(char) - ord('A')
            k_val = ord(key[key_index % key_length]) - ord('A')

            # Formule de Vigenère: C = (P + K) mod 26
            c_val = (p_val + k_val) % 26

            encrypted_char = chr(c_val + ord('A'))
            encrypted_text += encrypted_char

            # Prochain caractère
            key_index += 1
        else:
            encrypted_text += char

    return encrypted_text

# Ce n'est pas le plaintext utilisé
plaintext = "HELLO WORLD, HELLO WORLD!"
# Ce n'est pas la clé que j'ai utilisé
key = "EXEMPLE"
ciphertext = vigenere_encrypt(plaintext, key)
print(f"Vigenère Ciphertext: {ciphertext}")
# Sortie: LBPXD HSVIH, TTWPS TSDAO!