def sum_numbers(numbers):
    output = sum(int(number) for number in numbers.split() if number.isdigit())
    return output

print(sum_numbers('1 2 3 4 a b c 5'))