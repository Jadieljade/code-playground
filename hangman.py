''' A begginer level hangman game'''


import random
import string
from words import words


def get_valid(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives remaining and have used these letters',
              ' '.join(used_letters))
        word_list = [
            letter if letter in used_letters else '-'for letter in word]

        print('current words: ', ' '.join(word_list))

        user_letter = input('guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1

                print('letter is not in word. ')
                if lives == 5:
                    print('''
---
                    ''')
                elif lives == 4:
                    print('''
------
      |
      |
                    ''')
                elif lives == 3:
                    print('''
------
      |
      |
      O

                    ''')

                elif lives == 2:
                    print('''
-------
       |
       |
       O
     / | \\

                    ''')
                elif lives == 1:
                    print('''
-------
       |
       |
       O
     / | \\
       |
                    ''')
        elif user_letter in used_letters:
            print('you have already guessed that character')
        else:
            print('Invalid character please try again.')
    if lives == 0:
        print(f'''
-------
       |
       |
       O
     / | \\
       |
      / \\



you died the word was {word}



''')
    else:
        print(f'You got it right the word was {word} !!!!')
