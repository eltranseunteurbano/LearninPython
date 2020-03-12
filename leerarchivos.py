# coding=utf-8
def run():
    archivo = str(input("Introduzca el archivo que quiere abrir: "))
    accion = str(input("r = Leer, w = Escribir, a = Añadir, r+ = Leer y escribir: "))
    try:
        if(accion == 'r' or accion == 'w' or accion == 'a' or accion == 'r+'):
            with open (archivo, accion) as prueba:
                if accion == 'r':
                    print(prueba.readlines())
                elif accion == 'w':
                    prueba.write("Esta es una prueba")
                elif accion == 'a':
                    print('Añadiendo')
                elif accion == 'r+':
                    print('Leyendo y escribiendo')
        else:
            print('Ese comando no esta disponible')
            accion = str(input("r = Leer, w = Escribir, a = Añadir, r+ = Leer y escribir: "))
                
    except FileNotFoundError:
        print('El archivo {} que esta intentando abrir, no existe'. format(archivo))
if __name__ == '__main__':
    run()