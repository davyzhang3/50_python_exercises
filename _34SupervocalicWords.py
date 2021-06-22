from io import StringIO

f = StringIO('''
a
aa
aal
aalii
aam
Aani
aardvark
aardwolf
Aaron
apiaceous
autoelectrolytic
superregeneration

''')

def get_sv(filename):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    return {word.strip()
            for word in filename
            if vowels < set(word.lower())} 

print(get_sv(f))