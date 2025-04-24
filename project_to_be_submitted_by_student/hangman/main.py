import random
import string

from words import words


def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    lives = 7
    # getting user input
    while len(word_letters) > 0 and lives > 0:
       # letters used
       # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
       print('You have used these letters: ', ' '.join(used_letters))

       # what current word is (ie W - R D)
       word_list = [letter if letter in used_letters else '-' for letter in word]
       print('Lives left: ', lives, 'Current word: ', ' '.join(word_list))

       user_letter = input('Guess a letter: ').upper()
       if user_letter in alphabet - used_letters:
           used_letters.add(user_letter)
           if user_letter in word_letters:
               word_letters.remove(user_letter)
           else:
               lives = lives - 1
               print('Letter is not in word. ')

       elif user_letter in used_letters:
           print('You have already guessed that letter. ')
       else:
           print('Invalid character. Please try again. ')
    
    if lives == 0:
        print('You died, sorry. 😔🥹 The word was', word)
    else:
        print('You guessed the word', word, 'in', lives, 'lives remaining🎉😍 !!')

def main():
    hangman()

if __name__ == '__main__':
    main()

