from caesar import caesar_encrypt, caesar_decrypt
from vigenere import vigenere_encrypt, vigenere_decrypt

print("=== CRYPTOGRAPHY PROJECT ===")

text = "HELLO WORLD"

# Caesar test
print("\nCAESAR CIPHER")
encrypted_caesar = caesar_encrypt(text, 3)
decrypted_caesar = caesar_decrypt(encrypted_caesar, 3)

print("Encrypted:", encrypted_caesar)
print("Decrypted:", decrypted_caesar)

# Vigenère test
print("\nVIGENERE CIPHER")
encrypted_vig = vigenere_encrypt(text, "KEY")
decrypted_vig = vigenere_decrypt(encrypted_vig, "KEY")

print("Encrypted:", encrypted_vig)
print("Decrypted:", decrypted_vig)

# ===== FIG 3: Encryption & Decryption =====

text = "HELLO WORLD"
shift = 3

encrypted = caesar_encrypt(text, shift)
decrypted = caesar_decrypt(encrypted, shift)

print("\n--- FIG 3 OUTPUT ---")
print("Original:", text)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)

# ===== FIG 4: Input Validation =====

user_input = input("\nEnter text: ")

if user_input.strip() == "":
    print("Error: Text cannot be empty")
else:
    print("Valid input:", user_input)


    # ===== FIG 5: Testing Results =====

print("\n--- FIG 5: CIPHER TESTING RESULTS ---")

# Caesar tests
print("Caesar Test 1:", caesar_encrypt("ATTACK", 4))
print("Caesar Test 2:", caesar_encrypt("HELLO", 5))

# Caesar decrypt test
encrypted = caesar_encrypt("SECRET", 3)
print("Encrypted SECRET:", encrypted)
print("Decrypted SECRET:", caesar_decrypt(encrypted, 3))