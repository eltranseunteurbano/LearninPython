# _*_ coding: utf-8 _*_

def decorar (parametro):

    def interior(password):
        if password == 'platzi':    
            return parametro()
    
        else:
            print('La contraseña es incorrecta')
    return interior    

@decorar
def protected_func():
    print('Tu contraseña es correcta.')

if __name__ == '__main__':
    password = str(input('Ingresa tu contraseña: '))

    protected_func(password)