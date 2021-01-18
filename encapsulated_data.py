import sys
import os
from char_char import read_char, read_int
from bitpacking import pack_data, unpack_data


doc_dir = os.path.join(os.getcwd(), sys.argv[1])


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
            register_data()

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


def register_data():
    header = 'Cedula,Nombre,Apellido,Edad,Sexo,Estado_Civil,Grado_Academico'
    counter = 0

    try:
        with open(doc_dir, 'a+') as doc:
            if os.path.getsize(doc_dir) == 0:
                doc.write(header)

            lines = doc.readlines()

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

                data_list = [age, sex, civil_state, grade]
                packed_data = pack_data(data_list)

                data = f'{cid},{name},{lastname},{packed_data}'

                respuesta = input('¿Deseas guardar? si/no\n')

                if respuesta == 'no':
                    counter += 1
                    print('bye')

                else:
                    doc.write('\n')
                    doc.write(data)
                    print('Registro creado.')
    except IOError:
        print('Ruta del documento inválida.')


def list_data():
    try:
        with open(doc_dir, 'r') as doc:
            lines = doc.readlines()
            if len(lines) < 2:
                print('No hay registros.')
            else:
                doc.seek(0)
                head = doc.readline().strip('\n').split(',')
                for idx, line in enumerate(lines[1:], 1):
                    split_line = line.strip('\n').split(',')
                    unpacked = unpack_data(int(split_line[3]))
                    print(f'''
    Record #{idx}:
    {head[0]}: {split_line[0]}
    {head[1]}: {split_line[1]}
    {head[2]}: {split_line[2]}
    {head[3]}: {unpacked[0]}
    {head[4]}: {unpacked[1]}
    {head[5]}: {unpacked[2]}
    {head[6]}: {unpacked[3]}
    ''')
    except IOError:
        print('Ruta del documento inválida.')


def find_data(cid):
    try:
        with open(doc_dir, 'r') as doc:
            lines = doc.readlines()
            if len(lines) < 2:
                print('No hay registros que buscar.')
            else:
                found = False
                doc.seek(0)
                head = doc.readline().strip('\n').split(',')
                for idx, line in enumerate(lines[1:], 1):
                    split_line = line.strip('\n').split(',')

                    if split_line[0] == cid:
                        found = True
                        unpacked = unpack_data(int(split_line[3]))
                        print(f'''
    Registro #{idx}:
    {head[0]}: {split_line[0]}
    {head[1]}: {split_line[1]}
    {head[2]}: {split_line[2]}
    {head[3]}: {unpacked[0]}
    {head[4]}: {unpacked[1]}
    {head[5]}: {unpacked[2]}
    {head[6]}: {unpacked[3]}
    ''')
                        return idx

                print('Registro no encontrado.')

    except IOError:
        print('Ruta del documento inválida.')


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
