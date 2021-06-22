def ubbi_dubbi(word):
    output = []
    for letter in word:
        if letter in 'aeiou':
            output.append(f'ub{letter}')
        else:
            output.append(letter)
    return ''.join(output)

if __name__ == "__main__":
    print(ubbi_dubbi('python'))