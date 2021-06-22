from _5PigLatin import pig_latin
def pl_sentence(sentence):
    output = []
    sentence = sentence.split()
    for word in sentence:
        output.append(pig_latin(word))
    return ' '.join(output) # this makes a list of words join together with ' ' as the delemiter of the sentence

print(pl_sentence('This is a test'))

