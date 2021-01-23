import sys
import os
from utility import read_char, read_int, perso_sort, search_age
from encapsulated import Person, ComPerson


def main():
    option = 0

    while option == 0:
        selected = input('''
Elige la opción deseada:
[1] Agregar
[2] Listar
[3] Buscar
[4] Editar
[5] Eliminar
[6] Salir

''')

        if selected == '1':
            op = Operations('a+')
            op.register_data()

        elif selected == '2':
            op = Operations('r')
            op.list_data()

        elif selected == '3':
            op = Operations('r')
            op.find_data()

        elif selected == '4':
            op = Operations('r+')
            op.edit_data()

        elif selected == '5':
            op = Operations('r+')
            op.delete_data()

        elif selected == '6':
            print('Adios!')
            option += 1


class Operations:
    write_header = 'Cedula,Nombre,Apellido,Packed_Info'

    def __init__(self, mode):
        self.load_file(mode)

    def load_file(self, mode):
        try:
            doc_dir = os.path.join(os.getcwd(), sys.argv[1])
            self._doc = open(doc_dir, mode)
            lines = self._doc.readlines()
            current_pos = self._doc.tell()

            if os.path.getsize(doc_dir) == 0:
                self._doc.write(self.write_header)

            else:
                self._doc.seek(0)
                head = self._doc.readline().strip('\n').split(',')
                for idx, line in enumerate(self._doc.readlines(), 1):
                    split_line = line.strip('\n').split(',')
                    perso = ComPerson(split_line[:3])
                    # print(split_line[:3])
                    perso.unpack_data(int(split_line[3]))

                self._perso_list = perso_sort(ComPerson.person_list)
                return True

        except IOError:
            print('Ruta del documento inválida.')

    def register_data(self):
        counter = 0

        while counter == 0:
            perso = self.write_data('create')

            respuesta = input('¿Deseas guardar? si/no\n')

            if respuesta == 'no':
                counter += 1
                print('bye')

            else:
                perso.pack_data()
                self._doc.write('\n')
                self._doc.write(str(perso))
                print('Registro creado.')
        self._doc.flush()

    def find_data(self):
        perso = self.find_person()

        print(str(perso))
        return True

    def list_data(self):
        if self._perso_list:
            for idx, perso in enumerate(self._perso_list, 1):
                print(f'Record: {idx}')
                print(str(perso))
            return True

        print('Registro no encontrado.')
        self._doc.flush()

    def edit_data(self):

        perso = self.write_data('update')

        respuesta = input('¿Deseas guardar? si/no\n')

        if respuesta == 'si':
            perso.pack_data()
            self._doc.seek(0)
            self._doc.write(self.write_header)
            for person in self._perso_list:
                self._doc.write('\n')
                self._doc.write(person.get_perso())
            self._doc.truncate()
            print('Registro guardado.')
        else:
            print('bye')

        self._doc.flush()

    def delete_data(self):
        perso = self.find_person()

        if perso:
            respuesta = input('¿Seguro que desea eliminar este registro? si/no\n')
            if respuesta == 'si':
                self._doc.seek(0)
                self._doc.truncate()
                self._doc.write(self.write_header)
                for person in self._perso_list:
                    if person != perso:
                        self._doc.write('\n')
                        self._doc.write(person.get_perso())
                print('Registro eliminado.')

            self._doc.flush()

    def find_person(self):
        lis = self._perso_list
        start = 0
        end = len(lis)-1

        print('Cedula: ')
        cid = read_int()
        data = (str(cid),)

        print('Edad: ')
        age = read_int()

        self._obj = Person(data)
        self._obj._age = age

        obj_list = search_age(lis, age, start, end)

        if obj_list != -1:
            for perso in obj_list:
                if self._obj.__eq__(perso):
                    return perso
                else:
                    return False

        else:
            return False

    def write_data(self, mode):
        found = self.find_person()

        if mode == 'create' and found:
            print('Persona registrada, especificar otra.')
            self.write_data('create')

        elif mode == 'update' and not found:
            print('No registros encontrados, intenta nuevamente.')
            self.write_data('update')

        perso = self._obj if not found else found

        print('Nombre: ')
        perso._name = read_char()

        print('Apellido: ')
        perso._lastname = read_char()

        print('Sexo: F/M ')
        perso._sex = read_char()

        print('Estado Civil: C/S ')
        perso._civil_state = read_char()

        print('Grado A: B/G/P: ')
        perso._grade = read_char()

        return perso


if len(sys.argv) >= 2:
    main()
else:
    print('Especificar document. ej. reg_data.py datos.csv')
