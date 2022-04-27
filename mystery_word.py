import string
import random
import sys
import time
    

def play_start():
    print(f'Welcome!')
    time.sleep(1)
    print(f'(To exit at any time, press Control C (^C) on your keyboard.)')
    time.sleep(2)
    print(f'Some of these wont work yet!')
    print(f'Press P to play. Press R for rules. Press D for difficulty. Press L for language.')
    playstart_response = input()
    play_option = ['p', 'P']
    difficulty_option = ['d', 'D']
    if playstart_response in play_option:
        time.sleep(1)
        print(f'Getting ready...')
        time.sleep(2)
        play_game()
    if playstart_response in difficulty_option:
        play_difficulty()
    else:
        print("Invalid response. Press P to play, or press Command C (^C) to exit.")
        time.sleep(1)
        print("Starting again in a moment...")
        time.sleep(3)
        print()
        play_start()


def play_difficulty():
    with open('words.txt') as file_contents:
        # read the contents
        contents_string = file_contents.read()
        contents_list = contents_string.split()
        EASY_LIST = []
        NORMAL_LIST = []
        HARD_LIST = []
        for word in contents_list:
            if 4 <= len(word) <= 6:
                EASY_LIST.append(word)
            elif 7 <= len(word) <= 8:
                NORMAL_LIST.append(word)
            elif 9 <= len(word):
                HARD_LIST.append(word)
        selected_list = NORMAL_LIST
        random_word = random.choice(selected_list)
        play_game(random_word)


def play_again():
    print("Game over. Would you like to play again? y/n")
    play_response = input()
    yes_input = ['y', 'Y']
    no_input = ['n', 'N']
    if play_response in yes_input:
        play_game()
    elif play_response in no_input:
        time.sleep(1)
        print(f'See you next time!')
        time.sleep(1)
        exit()
    else:
        print("Invalid response. Enter y for new game, n to exit.")
        play_again()
    exit()


def play_game(random_word):
    print(random_word)
    time.sleep(1)

    print(f'I am thinking of a word.')
    time.sleep(2)
    print(f'It has {len(random_word)} letters:')
    print()

    guesses = ' '
    turns = 8

    while turns > 0:
        failed = 0

        for letter in random_word:
            if letter in guesses:
                print(letter, end=" ")

            else:
                print("_", end=" ")
                failed += 1

        if failed == 0:
            print(f'Good job! You guessed the word in {8 - turns} guesses!')
            play_again()

        print()
        guess = input("Guess a letter... ")
        guesses += guess

        if guess not in random_word:
            turns -= 1
            print(f'Not quite. You have {turns} guesses left.')

            if turns == 0:
                # call play_again
                play_again()


if __name__ == "__main__":
    play_start()
