# Block Cipher Security Analyzer

from collections import Counter
import hashlib

print("=== Block Cipher Security Analyzer ===")

text1 = input("Enter first message: ")
text2 = input("Enter second message: ")

print("\n--- Difference Analysis ---")

length = min(len(text1), len(text2))

for i in range(length):
    diff = ord(text1[i]) ^ ord(text2[i])
    print(f"Position {i+1}: {diff}")

print("\n--- Avalanche Effect ---")

hash1 = hashlib.sha256(text1.encode()).hexdigest()
hash2 = hashlib.sha256(text2.encode()).hexdigest()

print("Hash 1:", hash1)
print("Hash 2:", hash2)

print("\n--- Frequency Distribution ---")

frequency = Counter(text1)

for char, count in frequency.items():
    print(char, ":", count)

print("\n--- Statistical Report ---")

total = len(text1)

for char, count in frequency.items():
    probability = count / total
    print(char, "Probability:", round(probability, 3))