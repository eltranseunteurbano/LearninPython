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

WORDS = ['vaca', "celular", "amor", "principe", "duque", "desarrollo", "diseno", "jerry"]

def random_word():
    number = random.randint(0, len(WORDS))
    return WORDS[number]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('* --- * --- * --- * --- * --- *')

def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0
    
    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Escoge una letra: '))

        letter_indexes = []
        for i in range(len(word)):
            if word[i] == current_letter:
                letter_indexes.append(i)
    
        if len(letter_indexes) == 0:
            tries +=1
        
        else:
            for i in letter_indexes:
                hidden_word[i] = current_letter

            letter_indexes = []

        if tries == len(WORDS):
            print('Perdiste. La palabra correcta era "{}"'.format(word))
            break
        
        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('¡Felicidades! Ganaste. La palabra correcta es: "{}"'.format(word))
            break

if __name__ == '__main__':
    print("- B I E N V E N I D O S  A  A H O R C A D O S -")
    run()