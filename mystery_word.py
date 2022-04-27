import string
import random
import sys
import time
    

def play_start():
    print(f'Welcome!')
    time.sleep(2)
    print(f'Press D to play with defaults. Press O for options. Press I for rules.')
    playstart_response = input()
    defaults_option = ['d', 'D']
    options_option = ['o', 'O', '0']
    if playstart_response in defaults_option:
        time.sleep(1)
        print(f'Getting ready...')
        time.sleep(2)
        play_defaults()
    if playstart_response in options_option:
        play_options()
    else:
        print(f'Invalid response.')
        time.sleep(1)
        print(f'(To exit at any time, press Control C (^C).)')
        time.sleep(2)
        print(f'Starting again in a moment...')
        time.sleep(3)
        print(f'---')
        print()
        play_start()


def play_defaults():
    with open('words.txt') as file_contents:
        # read the contents
        contents_string = file_contents.read()
        contents_list = contents_string.split()
        MEDIUM_LIST = []
        for word in contents_list:
            if 7 <= len(word) <= 8:
                MEDIUM_LIST.append(word)
        selected_list = MEDIUM_LIST
        random_word = random.choice(selected_list)
        play_game(random_word)


def play_options():
    print(f'Options:')
    time.sleep(2)
    print(f'To view rules, press R.')
    time.sleep(1)
    print(f'To play with defaults (intensity: easy, language: en), press D.')
    time.sleep(1)
    print(f'To change gameplay intensity, press I.')
    time.sleep(1)
    print(f'To change language pack, press L.')
    playoptions_response = input()
    rules_option = ['r', 'R']
    defaults_option = ['d', 'D']
    intensity_option = ['i', 'I']
    if playoptions_response in defaults_option:
        time.sleep(1)
        print(f'Getting ready...')
        time.sleep(2)
        play_defaults()
    if playstart_response in intensity_option:
        play_difficulty()
    else:
        print(f'Invalid response.')
        play_options()


def play_difficulty():
    with open('words.txt') as file_contents:
        # read the contents
        contents_string = file_contents.read()
        contents_list = contents_string.split()
        EASY_LIST = []
        MEDIUM_LIST = []
        HARD_LIST = []
        for word in contents_list:
            if 4 <= len(word) <= 6:
                EASY_LIST.append(word)
            elif 7 <= len(word) <= 8:
                MEDIUM_LIST.append(word)
            elif 9 <= len(word):
                HARD_LIST.append(word)
        print(f'Select an intensity:')
        time.sleep(1)
        print(f'Press E for mild')
        print(f'Press M for medium')
        print(f'Press H for caliente')
        playdifficulty_response = input()
        easy_option = ['e', 'E']
        medium_option = ['m', 'M']
        hard_option = ['h', 'H']
        if playdifficulty_response in easy_option:
            time.sleep(1)
            print(f'Getting ready...')
            time.sleep(2)
            selected_list = EASY_LIST
            random_word = random.choice(selected_list)
            play_game(random_word)
        if playdifficulty_response in medium_option:
            time.sleep(1)
            print(f'Getting ready...')
            time.sleep(2)
            selected_list = MEDIUM_LIST
            random_word = random.choice(selected_list)
            play_game(random_word)
        if playdifficulty_response in hard_option:
            time.sleep(1)
            print(f'Getting ready...')
            time.sleep(2)
            selected_list = HARD_LIST
            random_word = random.choice(selected_list)
            play_game(random_word)
        else:
            print(f'Invalid response.')
            time.sleep(1)
            play_difficulty()


def play_again():
    print(f'Game over. Would you like to play again? y/n')
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
        print(f'Invalid response. Enter y for new game, n to exit.')
        time.sleep(1)
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
