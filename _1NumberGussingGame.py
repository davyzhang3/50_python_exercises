import random

def guessing_game():
    answer = random.randint(0,100)

    while True:

        while True:
            guessed_number = input('input your guess: ')
            if str.isdigit(guessed_number):
                guessed_number = int(guessed_number)
                break
            else:
                print('Type in integers plz')

        if answer < guessed_number:
            print(f'Your answer {guessed_number} is too high')
        elif answer == guessed_number:
            print(f'Just right, the answer is {guessed_number}')
            break
        else:
            print(f'Your answer {guessed_number} is too low')


guessing_game()

# import random

# def guessing_game():
#     number = random.randint(0,100)
#     guessed_number = int(input('input your guess: '))

#     while number != guessed_number:
        

#         if number < guessed_number:
#             print('Too high')
#         elif number == guessed_number:
#             print('Just right')
#         else:
#             print('Too low')
#         guessed_number = int(input('input your guess: '))

# guessing_game()