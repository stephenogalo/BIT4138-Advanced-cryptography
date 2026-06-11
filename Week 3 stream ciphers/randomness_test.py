from lfsr import lfsr

seed = [1, 0, 1, 1]
taps = [0, 1]

sequence = lfsr(seed, taps, 1000)

ones = sum(sequence)
zeros = len(sequence) - ones

print("Randomness Test")
print("Length:", len(sequence))
print("Number of Ones:", ones)
print("Number of Zeros:", zeros)

if abs(ones - zeros) < 100:
    print("Sequence passes frequency test.")
else:
    print("Sequence fails frequency test.")