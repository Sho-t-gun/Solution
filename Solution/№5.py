def generate_sequence(n):
    sequence, num = [], 1
    while len(sequence) < n:
        sequence.extend([num] * num)
        num += 1
    return ' '.join(map(str, sequence[:n]))


n = 10
print(generate_sequence(n))