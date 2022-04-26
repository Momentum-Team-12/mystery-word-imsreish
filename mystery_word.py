import string
import random


def play_game():
    # get the computer to read the files
    with open('words.txt') as file_contents:
        # read the contents
        contents_string = file_contents.read()
        contents_list = contents_string.split()
        random_word = random.choice(contents_list)
        print(random_word)
        print(f'I am thinking of a word. It has {len(random_word)} letters...')
        print()

        guesses = ' '
        turns = 8

        while turns > 0:
            failed = 0

            for letter in random_word:
                if letter in guesses:
                    print(letter, end=" ")

                else:
                    print("_")
                    # print(letter, end=" ")
                    failed += 1

            if failed == 0:
                print(f'Good job! You guessed the word in {turns} guesses!')
            break

        print()
        guess = input("Guess a letter: ")
        guesses += guess

        if guess not in random_word:
            turns -= 1
            print(f'Not quite. You have {turns} guesses left.')

            if turns == 0:
                print("Game over")


if __name__ == "__main__":
    play_game()
