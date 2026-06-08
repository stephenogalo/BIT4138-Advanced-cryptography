from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

message = b"Hello Cryptography"

encrypted = cipher.encrypt(message)

print("Original:", message)
print("Encrypted:", encrypted)