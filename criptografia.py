# coding=utf-8

KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}

def cypher(message):
    words = message.split(' ')
    cypher_message = []
    for i in words:
        cypher_word = ''
        for letter in i:
            cypher_word += KEYS[letter]

        cypher_message.append(cypher_word)
    return ' '.join(cypher_message)
    

def decipher(message):
    words = message.split(' ')
    decipher_message = []
    for i in words:
        decipher_word = ''

        for letter in i:
            
            for key, value in KEYS.items():
                if value == letter:
                    decipher_word += key

        decipher_message.append(decipher_word)
    return ' '.join(decipher_message)

def run():
    while True:
        command = str(input('''* --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *
        
            Bienvenido a criptografía. ¿Qué deseas hacer?
            
            [c] Cifrar
            [d] Decifrar Mensaje
            [s] Salir
            '''))
        
        if command == 'c' or command == 'C':
            message = str(input("Escribe tu mensaje: "))
            cypher_message = cypher(message)
            print(cypher_message)

        elif command == 'd' or command == 'D':
            message = str(input("Escribe tu mensaje cifrado: "))
            cypher_message = decipher(message)
            print(cypher_message)

        elif command == 's' or command == 'S':
            print("Salir")
        else:
            print('El comando "{}" no ha sido encontrado. Por favor ingrese el comando nuevamente.'.format(command))


if __name__ == '__main__':
    run()