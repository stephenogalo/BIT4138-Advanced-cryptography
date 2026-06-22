# Frequency Analysis

from collections import Counter

print("=== Frequency Analysis ===")

data = "ABABABABCCCCDDD"

frequency = Counter(data)

print("\nInput Data:", data)
print("\nCharacter Frequencies:")

for char, count in frequency.items():
    print(char, ":", count)

print("\nObservation:")
print("This shows how statistical patterns can exist in data.")