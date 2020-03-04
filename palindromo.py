# coding=utf-8

#Forma 2 de comprar palabras si son iguales
def palindromoDos(word):
    reverse_word = word[::-1]

    if reverse_word == word:
        return True
    return False


#Forma 1 de comprar palabras si son iguales
def palindromo(word):
    reversed_letters = []

    for letter in word:
        reversed_letters.insert(0,letter)

    reverse_word = ''.join(reversed_letters)

    if word == reverse_word:
        return True
    return False

if __name__ == '__main__':
    word = str(raw_input('Escribe una palabra. '))

    result = palindromoDos(word)
    if result is True:
        print('"{}" si es un palindromo'.format(word.upper()))
    else:
        print('"{}" no es un palindromo'.format(word.upper()))