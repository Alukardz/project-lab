def main():
    header = 'Nombres,Apellidos,Edad,Ahorros,Password'
    doc_dir = os.path.join(os.getcwd(), sys.argv[1])
    counter = 0

    try:
        with open(doc_dir, 'a+') as doc:
            if os.path.getsize(doc_dir) == 0:
                doc.write(header)

            lines = doc.readlines()

            while counter == 0:
                names = input('Cedula: ')
                lastnames = input('Nombre: ')
                age = input('Edad: ')
                savings = input('Apellido: ')
                password = input('Apellido: ')
                data = f'{names},{lastnames},{age},{savings},{password}'

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


if len(sys.argv) >= 2:
    main()
else:
    print('Especificar document. ej. reg_data.py datos.csv')