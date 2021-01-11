def pack_data(data):
    packed_info = 0
    age = data[0]
    sex = data[1]
    civil_state = data[2]
    grade = data[3]

    packed_info = age << 4

    if sex == 'M':
        packed_info = packed_info | 8

    if civil_state == 'C':
        packed_info = packed_info | 4

    if grade == 'P':
        packed_info = packed_info | 3

    elif grade == 'G':
        packed_info = packed_info | 2

    elif grade == 'B':
        packed_info = packed_info | 1

    return packed_info


def unpack_data(packed_info):
    grade = ''
    civil_state = ''
    sex = ''

    if not packed_info & 1:
        grade = 'G'

    elif packed_info >> 1 & 1:
        grade = 'P'
    else:
        grade = 'B'

    if packed_info >> 2 & 1:
        civil_state = 'C'
    else:
        civil_state = 'S'

    if packed_info >> 3 & 1:
        sex = 'M'
    else:
        sex = 'F'

    age = packed_info >> 4
    data = [age, sex, civil_state, grade]

    return data
