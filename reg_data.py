#!/usr/bin/python3.8
import sys
import os


def register_data(file):
    doc_dir = os.path.join(os.getcwd(), file)
    header = 'Cedula,Nombre,Apellido,Edad'
    counter = 0
    with open(doc_dir, 'a+') as doc:
        if os.path.getsize(doc_dir) == 0:
            doc.write(header)

        while counter == 0:
            print('Ingresa tus datos.')
            cid = input('Cédula: ')
            name = input('Nombre: ')
            lastname = input('Apellido: ')
            age = input('Edad: ')
            data = f'{cid},{name},{lastname},{age}'

            respuesta = input('¿Deseas guardar? si/no\n')
            if respuesta == 'no':
                counter += 1

            elif respuesta == 'si':
                doc.write('\n')
                doc.write(data)

        print('Adios!')


if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) >= 2:
        register_data(sys.argv[1])
    else:
        print('Especificar documento. ej. reg_data.py datos.csv')