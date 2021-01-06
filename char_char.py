import sys
import os
import tty
import termios


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
                pass_counter = 0
                print('Nombres: ')
                names = read_char()

                print('Apellidos: ')
                lastnames = read_char()

                print('Edad: ')
                age = read_int()

                print('Ahorros: ')
                savings = read_decimal()

                while pass_counter == 0:
                    print('Contraseña: ')
                    password = read_pass()

                    print('Confirmar contraseña: ')
                    password2 = read_pass()

                    if password == password2:
                        pass_counter += 1
                    else:
                        print('Contraseñas no concuerdan, intenta nuevamente.')

                data = f'{names},{lastnames},{age},{savings},{password}'
                print(data)

                respuesta = input('¿Deseas guardar? si/no\n')

                if respuesta == 'no':
                    counter += 1
                    print('bye')

                else:
                    doc.write('\n')
                    doc.write(data)
                    print('Registro creado.')
                    counter += 1

    except IOError:
        print('Ruta del documento inválida.')


def _getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1).strip('\n')

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def read_char():
    stringer = ''
    while True:
        cha = _getch()

        if cha.isalpha():
            print(cha, end='', flush=True)
            stringer += cha

        elif cha == '\x7f':
            print('\b \b', end='', flush=True)
            stringer = stringer[:-1]

        elif cha == '\r':
            print('\r')
            break

    return stringer


def read_int():
    inger = ''
    while True:
        cha = _getch()

        if cha.isdigit():
            print(cha, end='', flush=True)
            inger += cha

        elif cha == '\x7f':
            print('\b \b', end='', flush=True)
            inger = inger[:-1]

        elif cha == '\r':
            print('\r')
            break

    return inger


def read_decimal():
    inger = ''
    while True:
        cha = _getch()

        if cha.isdigit() or cha == '.' or cha == ',':
            print(cha, end='', flush=True)
            inger += cha

        elif cha == '\x7f':
            print('\b \b', end='', flush=True)
            inger = inger[:-1]

        elif cha == '\r':
            print('\r')
            break

    rounded = "%.2f" % float(inger)
    return rounded


def read_pass():
    passger = ''
    while True:
        cha = _getch()

        if cha.isprintable():
            print('*', end='', flush=True)
            passger += cha

        elif cha == '\x7f':
            print('\b \b', end='', flush=True)
            passger = passger[:-1]

        elif cha == '\r':
            print('\r')
            break

    return passger


if len(sys.argv) >= 2:
    main()
else:
    print('Especificar documento. ej. reg_data.py datos.csv')