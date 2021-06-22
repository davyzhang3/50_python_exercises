def hex_output():
    decnum = 0
    hexnum = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit) * (16 ** power)
    print(f'The decimal number of he hex number you inputed is {decnum}')
hex_output()