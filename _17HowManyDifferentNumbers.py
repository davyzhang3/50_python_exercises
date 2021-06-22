def how_many_different_numbers(numbers):
    unique_numbers = set(numbers)
    return len(unique_numbers)
print(how_many_different_numbers([1, 2, 3, 1,
2, 3, 4, 1]))

# # another way to do that
# def how_many_different_numbers(numbers):
#     # This tells Python that it should take the elements of numbers and feed them (in a sort of for loop) to the curly braces.
#     unique_numbers = {*numbers}
#     return len(unique_numbers)