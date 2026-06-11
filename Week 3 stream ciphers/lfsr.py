def lfsr(seed, taps, length):
    state = seed[:]
    output = []

    for _ in range(length):
        output.append(state[-1])

        feedback = 0
        for tap in taps:
            feedback ^= state[tap]

        state = [feedback] + state[:-1]

    return output


seed = [1, 0, 1, 1]
taps = [0, 1]

sequence = lfsr(seed, taps, 20)

print("Generated Sequence:")
print(sequence)