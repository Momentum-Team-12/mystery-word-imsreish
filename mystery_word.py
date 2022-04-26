import string
import random


def play_game():
    # get the computer to read the files
    with open('words.txt') as file_contents:
        # read the contents 
        contents_string = file_contents.read()
        # print(contents_string)
        contents_list = contents_string.split()
        # print(contents_list)
        random_word = random.choice(contents_list)
        print(random_word)
        print(f'I am thinking of a word. It has {len(random_word)} letters...')
        # Ask the player to guess 8 times.
        guesses = ''
        turns = 0
        while turns > 0:
            failed = 0
            for letter in random_word:
                if letter in guesses:
                    print(letter, end="")
                else:
                    print("_")
                    print(letter, end=" ")
                    failed += 1
            if failed == 0:
                print(f'Good job! You guessed the word in ' + {str(random_word)} + ' guesses!')
            break
        print()
        guess = input("Guess a letter: ")


if __name__ == "__main__":
    play_game()
