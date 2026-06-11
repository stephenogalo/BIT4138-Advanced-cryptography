from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# Load key
with open("secret.key", "rb") as f:
    key = f.read()

# Generate IV (Initialization Vector)
iv = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_CBC, iv)

# Read file
with open("sample.txt", "rb") as f:
    data = f.read()

# Pad data correctly
padded_data = pad(data, AES.block_size)

# Encrypt
encrypted_data = cipher.encrypt(padded_data)

# Save IV + ciphertext together
with open("encrypted.bin", "wb") as f:
    f.write(iv + encrypted_data)

print("File encrypted successfully")