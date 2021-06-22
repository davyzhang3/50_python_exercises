from io import StringIO

f = StringIO('this is a bunch of text\nand it should be translated\n')

def plword(word):
    if word[0] in 'aeiou':
        return word + 'way'

    return word[1:] + word[0] + 'ay'

def plfile(s):
    return ' '.join(plword(one_word)
                    for one_line in s
                    for one_word in one_line.split()) 

print(plfile(f)) # using StringIO