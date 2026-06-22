from caesar import caesar_encrypt
from vigenere import vigenere_encrypt

print("\n--- TESTING RESULTS ---")

print("Caesar Test:", caesar_encrypt("ATTACK", 4))
print("Vigenère Test:", vigenere_encrypt("ATTACK", "KEY"))