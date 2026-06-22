# XOR-Based Analysis

plaintext = 12
key = 5

ciphertext = plaintext ^ key

recovered_key = ciphertext ^ plaintext

print("=== XOR-Based Analysis ===")
print("Plaintext:", plaintext)
print("Key:", key)
print("Ciphertext:", ciphertext)
print("Recovered Key:", recovered_key)