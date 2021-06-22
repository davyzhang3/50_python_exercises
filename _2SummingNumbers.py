def mysum(*numbers): # * allow the function to be called in the usual way when you pass a iterable object
    output = 0
    for number in numbers:
        output += number
    return output

print(mysum(1,4,6,7))