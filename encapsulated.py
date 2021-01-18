class Persons():
    header = 'Cedula,Nombre,Apellido,Edad,Sexo,Estado_Civil,Grado_Academico'

    def __init__(self, data):
        self._cid = data.cid
        self._name = data.name
        self._lastname = data.lastname
