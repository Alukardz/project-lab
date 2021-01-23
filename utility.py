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

    return int(inger)


def perso_sort(lis):

    for idx in range(1, len(lis)):
        current_obj = lis[idx]
        loc = idx

        while loc > 0 and lis[loc-1].__gt__(current_obj):
            lis[loc] = lis[loc-1]
            loc = loc-1

        lis[loc] = current_obj

    return lis


def search_age(lis, obj_age, start, end):
    obj_list = []

    if end >= start:

        mid = (start + end) // 2

        if obj_age == lis[mid]._age:
            obj_list.append(lis[mid])

            while len(lis) > 1 and mid+1 <= len(lis)-1 and obj_age == lis[mid+1]._age:
                obj_list.append(lis[mid+1])
                mid += 1

            while len(lis) > 1 and mid-1 >= 0 and obj_age == lis[mid-1]._age:
                obj_list.append(lis[mid-1])
                mid -= 1

            return obj_list

        elif lis[mid]._age > obj_age:
            return search_age(lis, obj_age, start, mid-1)

        else:
            return search_age(lis, obj_age, mid+1, end)

    else:
        return -1
