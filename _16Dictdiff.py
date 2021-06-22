def dictdiff(first, second):
    output = {}
    all_keys = first.keys() | second.keys()

    for key in all_keys:
        """Just like d[k], except that it returns None (or the second, optional argument) if k isn’t in d."""
        # x = d.get(k) or x = d.get(k, 10)
        if first.get(key) != second.get(key):
            output[key] = [first.get(key), second.get(key)]
    return output
d1 = {'a':1, 'b':2, 'c':3}

d2 = {'a':1, 'b':2, 'd':4}
print(dictdiff(d1, d2))
