# Write your code here
import random
import string


def play_game():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    guess_word = random.choice(word_list)
    word_list = list(guess_word)
    len_word = len(guess_word)
    hidden_word = len_word * "-"
    new_output = list(hidden_word)
    set_guesses = set()
    alphabet_list = list(string.ascii_lowercase)

    print("H A N G M A N\n")

    count = 0
    while count < 8:
        print(hidden_word)
        letter = input("Input a letter: ")
        if len(letter) > 1:
            print("You should input a single letter\n")
            continue
        if letter not in alphabet_list:
            print("It is not an ASCII lowercase letter\n")
            continue
        if letter not in guess_word and letter not in set_guesses:
            if count == 7:
                print("No such letter in the word ")
                print("You are hanged!")
                break
            else:
                set_guesses.add(letter)
                print("No such letter in the word\n")
                count += 1
        elif letter not in guess_word and letter in set_guesses:
            print("You already typed this letter\n")
            continue
        elif letter in guess_word and letter in set_guesses:
            print("You already typed this letter\n")
            continue
        elif letter in guess_word and letter not in set_guesses:
            print("")
            set_guesses.add(letter)
            hidden_word = ''.join(x if x in set_guesses else '-' for x in guess_word)
            if hidden_word == guess_word:
                print(guess_word)
                print("You guessed the word! You survived!\n")
                break
            else:
                while letter in guess_word and letter not in set_guesses:
                    set_guesses.add(letter)
                    hidden_word = ''.join(x if x in set_guesses else '-' for x in guess_word)
                    if hidden_word == guess_word:
                        print(guess_word)
                        print("You guessed the word!\nYou survived!")
                        break
                    else:
                        continue




while True:
    input_start = input('Type "play to play the game, "exit" to quit: ')
    if input_start == "play":
        play_game()
    elif input_start == "exit":
        break
    else:
        continue



