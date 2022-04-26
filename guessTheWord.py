# This is a guess the number game.
import random
contents_list = ['banana', 'sunscreen', 'computer', 'irrigation', 'explorer']
secret_word = random.choice(contents_list)
print('I am thinking of a random word.')

# Ask the player to guess 8 times.
for guessesTaken in range(1, 9):
    print('Take a guess.')
    guess = int(input())

    if guess != secret_word:
        print('Try again...')
    else:
        break     # This condition is the correct guess!

if guess == secret_word:
    print('Good job! You guessed the word in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The word I was thinking of was ' + str(secret_word))