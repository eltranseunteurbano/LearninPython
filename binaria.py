# -*- coding: utf-8 -*-

def binary_search(numbers, number_to_find, low, high ):
    #Caso base
    if low > high:
        return False

    mid = int( (low + high) / 2)

    if numbers[mid] == number_to_find:
        return True

    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid - 1)

    else:
        return binary_search(numbers, number_to_find, mid + 1, high)


if __name__ == '__main__':

    numbers = [1,3,4,6,8,9,10,11,13,14,18,19,20,22,24,26,30,35,40,42,44,46,48,50,58,60,72]
    find = int(input("Ingresa un número: "))

    result = binary_search(numbers, find, 0, len(numbers) - 1 )

    if result == True:
        print('El número si está en la lista')
    else:
        print('El número no esta está en la lista')