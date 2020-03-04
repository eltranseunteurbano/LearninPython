# coding=utf-8
import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = ['vaca', "celular", "amor", "principe", "duque", "desarrollo", "diseno"]

def random_word():
    number = random.randint(0, len(WORDS))
    print(number)
    return word

def run():
    word = random_word()

if __name__ == '__main__':
    print("- B I E N V E N I D O S  A  A H O R C A D O S -")
    run()