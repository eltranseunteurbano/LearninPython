# coding=utf-8

class Lamp:

    def __init__(self):
        self.prendido = False

    def prender(self):
        self.prendido = True
        self._display_image()
        
    def apagar(self):
        self.prendido = False
        self._display_image()

    def _display_image(self):
        if self.prendido:
            print("Lampara prendida")
        else:
            print("Lampara apagada")

def run():
    lamp = Lamp()

    while True:
        command = str(input('''
            [p] Prender
            [a] Apagar 
            [s] Salir
        '''))

        if command == 'p' or command == 'P':
            lamp.prender()
        
        elif command == 'a' or command == 'A':
            lamp.apagar()

        else:
            break

if __name__ == '__main__':
    run()