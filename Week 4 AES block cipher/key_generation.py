from Crypto.Random import get_random_bytes

# Generate a secure 16-byte AES key
key = get_random_bytes(16)

# Save key to file
with open("secret.key", "wb") as f:
    f.write(key)

print("AES Key generated and saved to secret.key")