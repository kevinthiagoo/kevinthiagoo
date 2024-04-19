class disciplina():
    def __init__(self):
        self.d1 = (input('Digite a 1° disciplina: '))
        self.d2 = (input('Digite a 2° disciplina: '))
        self.d3 = (input('Digite a 3° disciplina: '))
        self.d4 = (input('Digite a 4° disciplina: '))
        self.d5 = (input('Digite a 5° disciplina: '))

    def dados(self):
        print('A sua 1° disciplina é: {}\nA sua 2° disciplina é: {}\nA sua 3° disciplina é: {}\nA sua 4° disciplina é: {}\nA sua 5° disciplina é: {}'.format(self.d1,self.d2,self.d3,self.d4,self.d5))

x = disciplina()
x.dados()