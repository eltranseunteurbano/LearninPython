# coding=utf-8
import csv

class Contact:
    def __init__(self, name, phone, email):
        self._name = name
        self._phone = phone
        self._email = email

class ContactBook:
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        if len(self._contacts) > 0:

            for contact in self._contacts:
                self._print_contact(contact)
        else:
            print('No tienes contactos en tu agenda.')

    def _print_contact(self, contact):
        print('* --- * --- * --- * --- * --- * --- *')
        print('Nombre: {}'.format(contact._name))
        print('Telefono: {}'.format(contact._phone))
        print('Email: {}'.format(contact._email))
        print('* --- * --- * --- * --- * --- * --- *')

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact._name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break

    def search(self, name):
        for contact in self._contacts:
            if contact._name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found(name)
    
    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow( ('nombre', 'phone', 'email') )

            for contact in self._contacts:
                writer.writerow( (contact._name, contact._phone, contact._email) )
    
    def _not_found(self, name):
        print('* --- * --- * --- * --- * --- * --- *')
        print('El contacto que buscas con el nombre de "{}" no fue encontrado'.format(name.upper()))
        print('* --- * --- * --- * --- * --- * --- *')

    def update(self, name):
        for contact in self._contacts:
            if contact._name.lower() == name.lower():
                new_name = str(input('Escribe el nombre del contacto: '))
                new_phone = str(input('Escribe el  telefono del contacto: '))
                new_email = str(input('Escribe el email del contacto: '))

                contact._name = new_name
                contact._email = new_email
                contact._phone = new_phone
                self._save()
                print('* --- ' * 8)
                print('Contacto actualizado')
                break
        else:
            self._not_found(name)

def run():

    contact_book = ContactBook()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            if len(row) == 0:
                continue

            contact_book.add(row[0], row[1], row[2])
            


    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a] Agregar contacto
            [c] Actualizar contacto
            [b] Buscar contacto
            [e] Eliminar contacto
            [l] Listar contactos
            [s] Salir
        
        '''))

        if command == 'a' or command == 'A':
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el  telefono del contacto: '))
            email = str(input('Escribe el email del contacto: '))
            contact_book.add(name, phone, email)

        if command == 'c' or command == 'C':
            contact = str(input('¿Cual contacto quieres actualizar?: '))
            contact_book.update(contact)

        if command == 'b' or command == 'B':
            contact = str(input('¿Cual es el nombre del contacto que estas buscando?: '))
            contact_book.search(contact)

        if command == 'e' or command == 'E':
            eliminar = str(input('Escribe el nombre del contacto a eliminar: '))
            contact_book.delete(eliminar)

        if command == 'l' or command == 'L':
            contact_book.show_all()

        if command == 's' or command == 'S':
            print('Salir')
            break


if __name__ == ('__main__'):
    print('B I E N V E N I D O   A   L A   A G E N D A')
    run()
