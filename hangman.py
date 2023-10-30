import string
import random
from words import words

def get_valid_words(word):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word 

def hangman():

    alphabet = set(string.ascii_uppercase)

    word = get_valid_words(words).upper()

    used_letters = set()

    word_letters = set(word)

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(f'You have {lives} lives left and you have currently used the following letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('The current word is: ', ' '.join(word_list))

        user_guess = input('Guess a letter from the word: ').upper()

        if user_guess in alphabet - used_letters:
            used_letters.add(user_guess)

            if user_guess in word_letters:
                word_letters.remove(user_guess)

            else:
                lives -= 1 
                if lives == 1:

                    letter_position = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eight", "ninth", "tenth", "eleventh", "twelveth"]

                    for idx, letter in enumerate(word_list):
                        if letter == '-':
                            print(f"Here is a HINT, the {letter_position[idx]} letter of the word is {word[idx]}")
                            break
            
        
        elif user_guess in used_letters:
                print('You ahve already used this letter before.')
            
        else:
            print('Invalid Character, please guess again.')

    if lives == 0:
        print(f'You died, the correct word was {word}!')
    
    else:
        print(f'Goodwork, you guessed the word {word} correctly!')

hangman()

