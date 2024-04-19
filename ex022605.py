class Regina:
    def robotica(self):
        print("A Professora Regina")
class Mychel():
    def robotica(self):
        print("O Professor Mychel")
class Professor(Regina,Mychel):
    def materia(self):
        print("As materias dos Professores")
a=Professor()
a.robotica()