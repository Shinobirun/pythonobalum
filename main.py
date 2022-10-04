
class Alumno():

    nombre = ''
    nota = 0

    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota



    def aprobo(self ):
        if self.nota > 6:
            print('La nota de ',self.nombre,' fue: ',self.nota,' aprobó')
        else:
            print('La nota de ',self.nombre,' fue: ',self.nota,' no aprobó')


alum1 = Alumno('Jorge',8)

alum1.aprobo()

alum2 = Alumno('Maria',4)

alum2.aprobo()