class ClasseC():
    def au(self):
        print('Carla')

class ClasseB():
    def au(self):
        print('Beatriz')

class ClasseF(ClasseC, ClasseB):
    def imprimir(self):
        print('Au')

a=ClasseF()
a.au()