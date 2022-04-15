import random

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

random_alpha = random.choice(alphabets)

print('your random selection', random_alpha)

print('************GUESS THE ALPHABET***********')

your_guesses = ''
chances = 10

while chances > 0:
    wrong_guesses = 0
    for character in random_alpha:
        if character in your_guesses:
            print(f'Correct Guess!: {character}')
        else:
            wrong_guesses +=1
            print('__')
    if wrong_guesses == 0:
        print('Correct Guess!')
        print(f'Alphabet is : {random_alpha}')
        break
    guess = (input('Guess an alphabet: ')).upper()
    your_guesses += guess

    if guess not in random_alpha:
        chances -= 1
        print(f'Wrong! You have {chances} chances more!!')

        if chances == 0:
            print('Game Over!!!')
