import sys
import tty
import termios


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
