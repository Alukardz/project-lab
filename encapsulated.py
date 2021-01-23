class Person:

    def __init__(self, *args):
        data = args[0]
        self._cid = data[0]
        if len(data) > 1:
            self._name = data[1]
            self._lastname = data[2]

    def __hash__(self):
        return hash((self._age, self._cid))

    def __eq__(self, other):
        return self._age == other._age and self._cid == other._cid

    def __gt__(self, other):
        return self._age > other._age

    def pack_data(self):

        packed_info = self._age << 4

        if self._sex == 'M':
            packed_info = packed_info | 8

        if self._civil_state == 'C':
            packed_info = packed_info | 4

        if self._grade == 'P':
            packed_info = packed_info | 3

        elif self._grade == 'G':
            packed_info = packed_info | 2

        elif self._grade == 'B':
            packed_info = packed_info | 1

        self._packed_info = packed_info

        return packed_info

    def __str__(self):
        info_string = f'{self._cid},{self._name},{self._lastname},{self._packed_info}'
        return info_string


class ComPerson(Person):
    header = ['Cedula', 'Nombre', 'Apellido', 'Edad', 'Sexo', 'Estado_Civil', 'Grado_Academico']
    person_list = []

    def __init__(self, data):
        ComPerson.person_list.append(self)
        super().__init__(data)

    def unpack_data(self, packed_info: int):
        self._packed_info = packed_info

        if not packed_info & 1:
            self._grade = 'G'

        elif packed_info >> 1 & 1:
            self._grade = 'P'
        else:
            self._grade = 'B'

        if packed_info >> 2 & 1:
            self._civil_state = 'C'
        else:
            self._civil_state = 'S'

        if packed_info >> 3 & 1:
            self._sex = 'M'
        else:
            self._sex = 'F'

        self._age = packed_info >> 4

        return 'Unpacked'

    def __str__(self):
        info_string = f'''
    {self.header[0]}: {self._cid}
    {self.header[1]}: {self._name}
    {self.header[2]}: {self._lastname}
    {self.header[3]}: {self._age}
    {self.header[4]}: {self._sex}
    {self.header[5]}: {self._civil_state}
    {self.header[6]}: {self._grade}
    '''
        return info_string

    def get_perso(self):
        info_string = f'{self._cid},{self._name},{self._lastname},{self._packed_info}'
        return info_string
