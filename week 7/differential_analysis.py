# Differential Cryptanalysis Simulation

print("=== Differential Cryptanalysis Simulation ===")

plaintext1 = input("Enter first plaintext: ")
plaintext2 = input("Enter second plaintext: ")

if len(plaintext1) != len(plaintext2):
    print("Plaintexts must have the same length.")
else:
    print("\nCharacter-by-Character Differences:")

    for i in range(len(plaintext1)):
        difference = ord(plaintext1[i]) ^ ord(plaintext2[i])

        print(
            f"Position {i+1}: "
            f"'{plaintext1[i]}' XOR '{plaintext2[i]}' = {difference}"
        )