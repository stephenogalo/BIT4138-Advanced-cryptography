def rc4(key, plaintext):
    S = list(range(256))
    j = 0

    key = [ord(c) for c in key]

    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0
    ciphertext = []

    for char in plaintext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256

        S[i], S[j] = S[j], S[i]

        k = S[(S[i] + S[j]) % 256]

        ciphertext.append(ord(char) ^ k)

    return ciphertext


key = "secret"
plaintext = "HELLO"

encrypted = rc4(key, plaintext)

print("Plaintext:", plaintext)
print("Encrypted:", encrypted)