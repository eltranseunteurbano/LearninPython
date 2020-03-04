# coding=utf-8

def palindormo(word):
    reversed_letters = []

    for letter in word:
        reversed_letters.insert(0,letter)

    reverse_word = ''.join(reversed_letters)

    if word == reverse_word:
        return True
    return False

if __name__ == '__main__':
    word = str(raw_input('Escribe una palabra. '))

    result = palindormo(word)
    if result is True:
        print('"{}" si es un palindromo'.format(word.upper()))
    else:
        print('"{}" no es un palindromo'.format(word.upper()))