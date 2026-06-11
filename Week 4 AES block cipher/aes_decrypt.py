from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Load key
with open("secret.key", "rb") as f:
    key = f.read()

# Load encrypted file
with open("encrypted.bin", "rb") as f:
    data = f.read()

# Extract IV and ciphertext
iv = data[:16]
ciphertext = data[16:]

cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt and unpad
decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)

# Save result
with open("decrypted.txt", "wb") as f:
    f.write(decrypted)

print("Decryption successful!")
print("Decrypted text:", decrypted.decode())