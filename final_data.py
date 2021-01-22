import sys
import os
from utility import read_char, read_int, perso_sort, search_age, write_data
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
            print('Cedula: ')
            cid = read_int()
            op = Operations('r')
            op.find_data(cid)

        elif selected == '4':
            print('Cedula del registro a editar: ')
            cid = read_int()
            op = Operations('r+')
            op.edit_data(cid)

        elif selected == '5':
            print('Cedula del registro a eliminar: ')
            cid = read_int()
            op = Operations('r+')
            op.delete_data(cid)

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
                    perso.unpack_data(int(split_line[3]))

                self._perso_list = perso_sort(ComPerson.person_list)
                return True

        except IOError:
            print('Ruta del documento inválida.')

    def register_data(self):
        counter = 0

        while counter == 0:
            data_list = write_data()

            perso = Person(data_list[:3])
            perso._age = data_list[3]

            if self.find_person(perso):
                print('Persona registrada, especificar otra.')
                self.register_data()

            respuesta = input('¿Deseas guardar? si/no\n')

            if respuesta == 'no':
                counter += 1
                print('bye')

            else:
                perso.pack_data(data_list[3:])
                self._doc.write('\n')
                self._doc.write(str(perso))
                print('Registro creado.')
        self._doc.flush()

    def find_data(self, cid):
        for perso in self._perso_list:
            if int(perso._cid) == cid:
                print('Record Encontrado')
                return perso

        return False

    def list_data(self):
        if self._perso_list:
            for idx, perso in enumerate(self._perso_list, 1):
                print(f'Record: {idx}')
                print(str(perso))
            return True

        print('Registro no encontrado.')
        self._doc.flush()

    def edit_data(self, cid):

        data_list = write_data()

        perso = Person(data_list[:3])
        perso._age = data_list[3]

        if self.find_person(perso):
            respuesta = input('¿Deseas guardar? si/no\n')

            if respuesta == 'si':
                perso.pack_data(data_list[3:])
                self._doc.seek(0)
                self._doc.write(self.write_header)
                for person in self._perso_list:
                    self._doc.write('\n')
                    self._doc.write(str(person))
                print('Registro guardado.')
            else:
                print('bye')

            self._doc.flush()

        else:
            print('Registro no encontrado.')

    def delete_data(self, cid):
        perso = self.find_data(cid)

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

    def find_person(self, obj):
        lis = self._perso_list
        start = 0
        end = len(lis)-1

        obj_list = search_age(lis, obj._age, start, end)

        if obj_list != -1:
            for perso in obj_list:
                if obj.__eq__(perso):
                    return True
                else:
                    return False

        else:
            return False


if len(sys.argv) >= 2:
    main()
else:
    print('Especificar document. ej. reg_data.py datos.csv')
