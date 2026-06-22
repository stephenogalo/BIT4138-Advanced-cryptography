# Avalanche Effect Demonstration

import hashlib

print("=== Avalanche Effect Demo ===")

text1 = "HELLO"
text2 = "HELLo"   # small change (case difference)

hash1 = hashlib.sha256(text1.encode()).hexdigest()
hash2 = hashlib.sha256(text2.encode()).hexdigest()

print("\nInput 1:", text1)
print("SHA-256:", hash1)

print("\nInput 2:", text2)
print("SHA-256:", hash2)

print("\nObservation:")
print("Small change in input produces completely different hash output.")
