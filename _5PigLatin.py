def pig_latin(word):
    if word[0] in 'aeiou':
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'

if __name__ == '__main__':
    print(pig_latin('python'))
