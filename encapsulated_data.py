import sys
import os
from char_char import read_char, read_int
from bitpacking import pack_data, unpack_data
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
            Operations.register_data('a+')

        elif selected == '2':
            list_data()

        elif selected == '3':
            cid = input('Cedula: ')
            find_data(cid)

        elif selected == '4':
            cid = input('Cedula del registro a editar: ')
            edit_data(cid)

        elif selected == '5':
            cid = input('Cedula del registro a eliminar: ')
            delete_data(cid)

        elif selected == '6':
            print('Adios!')
            option += 1


class Operations:

    def __init__(self, mode):
        self.load_file(mode)

    def load_file(self, mode):
        write_header = 'Cedula,Nombre,Apellido,packed_info'
        try:
            doc_dir = os.path.join(os.getcwd(), sys.argv[1])
            self._doc = open(doc_dir, mode)
            lines = self._doc.readlines()

            if os.path.getsize(doc_dir) == 0:
                self._doc.write(write_header)
            elif len(lines) < 2:
                print('No hay registros.')
            else:
                self._doc.seek(0)
                head = self._doc.readline().strip('\n').split(',')
                for idx, line in enumerate(lines[1:], 1):
                    split_line = line.strip('\n').split(',')
                    perso = ComPerson(split_line[0], split_line[1], split_line[2])
                    perso.unpack_data(int(split_line[3]))

                return ComPerson.person_list

        except IOError:
            print('Ruta del documento inválida.')

    def register_data(self):
        counter = 0

        while counter == 0:
            print('Cedula: ')
            cid = read_int()

            print('Nombre: ')
            name = read_char()

            print('Apellido: ')
            lastname = read_char()

            print('Edad: ')
            age = read_int()

            print('Sexo: F/M ')
            sex = read_char()

            print('Estado Civil: C/S ')
            civil_state = read_char()

            print('Grado A: B/G/P: ')
            grade = read_char()

            perso = Person(cid, name, lastname)
            perso.pack_data(age, sex, civil_state, grade)
            data = str(perso)

            respuesta = input('¿Deseas guardar? si/no\n')

            if respuesta == 'no':
                counter += 1
                print('bye')

            else:
                self._doc.write('\n')
                self._doc.write(data)
                print('Registro creado.')


def list_data():
    perso_list = load_file('r')
    for idx, perso in enumerate(perso_list, 1):
        print(f'Record: {idx}')
        print(str(perso))


def find_data(cid):
    perso_list = load_file('r')
    for idx, perso in enumerate(perso_list, 1):
        if perso._cid == cid:
            print(f'Record: {idx}')
            print(str(perso))

            return idx

    print('Registro no encontrado.')
    return cid


def edit_data(cid):
    idx = find_data(cid)

    if idx:
        try:
            with open(doc_dir, 'r+') as doc:
                lines = doc.readlines()
                doc.seek(0)

                print('Cedula: ')
                ced = read_int()

                print('Nombre: ')
                name = read_char()

                print('Apellido: ')
                lastname = read_char()

                print('Edad: ')
                age = read_int()

                print('Sexo: F/M ')
                sex = read_char()

                print('Estado Civil: C/S ')
                civil_state = read_char()

                print('Grado A: B/G/P: ')
                grade = read_char()

                data_list = [age, sex, civil_state, grade]
                packed_data = pack_data(data_list)

                data = f'{ced},{name},{lastname},{packed_data}\n'
                lines[idx] = data

                respuesta = input('¿Deseas guardar? si/no\n')

                if respuesta == 'si':
                    doc.writelines(lines)
                    print('Registro guardado.')
                else:
                    print('bye')

        except IOError:
            print('Ruta del documento inválida.')


def delete_data(cid):
    idx = find_data(cid)

    if idx:
        respuesta = input('¿Seguro que desea eliminar este registro? si/no\n')
        if respuesta == 'si':

            try:
                with open(doc_dir, 'r+') as doc:
                    lines = doc.readlines()
                    doc.seek(0)
                    doc.truncate()

                    for line in lines:
                        if line != lines[idx]:
                            doc.write(line)
                    print('Registro eliminado.')

            except IOError:
                print('Error eliminando registro.')


if len(sys.argv) >= 2:
    main()
else:
    print('Especificar document. ej. reg_data.py datos.csv')
