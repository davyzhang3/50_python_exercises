def join_numbers(numbers):
    numbers = (str(number) for number in numbers)
    return ','.join(numbers)

print(join_numbers(range(15)))