import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Load key
with open("secret.key", "rb") as f:
    key = f.read()

# Large test data
data = b"A" * 100000

cipher = AES.new(key, AES.MODE_CBC, b"0000000000000000")

# Measure encryption time
start = time.time()
cipher.encrypt(pad(data, AES.block_size))
end = time.time()

print("AES Encryption Time:", end - start, "seconds")