import sys
import os


def main():
    doc_dir = os.path.join(os.getcwd(), sys.argv[1])
    lista = []
    option = 0

    while option == 0:
        selected = input('''
Elige la opción deseada:
[1] Agregar
[2] Listar
[3] Buscar
[4] Salir

''')

        if selected == '1':
            register_data(doc_dir)

        if selected == '2':
            list_data(doc_dir)

        if selected == '3':
            find_data(doc_dir)

        if selected == '4':
            print('Adios!')
            option += 1


def register_data(doc_dir):
    header = 'Cedula,Nombre,Apellido,Edad'
    counter = 0

    try:
        with open(doc_dir, 'a+') as doc:
            if os.path.getsize(doc_dir) == 0:
                doc.write(header)

            while counter == 0:
                print('Ingresa tus datos.')
                cid = input('Cedula: ')
                name = input('Nombre: ')
                lastname = input('Apellido: ')
                age = input('Edad: ')
                data = f'{cid},{name},{lastname},{age}'

                respuesta = input('¿Deseas guardar? si/no\n')

                if respuesta == 'no':
                    counter += 1

                else:
                    doc.write('\n')
                    doc.write(data)
    except IOError:
        print('Ruta del documento inválida.')


def list_data(doc_dir):
    try:
        with open(doc_dir, 'r') as doc:
            lines = doc.readlines()
            if len(lines) < 2:
                print('No hay registros.')
            else:
                doc.seek(0)
                head = doc.readline().strip('\n').split(',')
                for idx, line in enumerate(lines, 1):
                    split_line = line.strip('\n').split(',')
                    print(f'''
    Record #{idx}:
    {head[0]}: {split_line[0]}
    {head[1]}: {split_line[1]}
    {head[2]}: {split_line[2]}
    {head[3]}: {split_line[3]}
    ''')
    except IOError:
        print('Ruta del documento inválida.')


def find_data(doc_dir):
    cid = input('Cedula: ')
    try:
        with open(doc_dir, 'r') as doc:
            lines = doc.readlines()
            if len(lines) < 2:
                print('No hay registros que buscar.')
            else:
                doc.seek(0)
                head = doc.readline().strip('\n').split(',')
                for idx, line in enumerate(lines, 1):
                    split_line = line.strip('\n').split(',')

                    if split_line[0] == cid:
                        print(f'''
    Record #{idx}:
    {head[0]}: {split_line[0]}
    {head[1]}: {split_line[1]}
    {head[2]}: {split_line[2]}
    {head[3]}: {split_line[3]}
    ''')

    except IOError:
        print('Ruta del documento inválida.')


if len(sys.argv) >= 2:
    main()
else:
    print('Especificar document. ej. reg_data.py datos.csv')
