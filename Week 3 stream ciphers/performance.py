import time
from rc4 import rc4

plaintext = "HELLO" * 1000
key = "secret"

start = time.time()

rc4(key, plaintext)

end = time.time()

print("Execution Time:", end - start, "seconds")