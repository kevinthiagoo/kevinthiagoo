class pessoa():
        def __init__(self):
                self.nome = str(input('Digite o seu nome: '))
                self.idade = int(input('Digite a sua idade: '))
                self.escola = input('Digite a sua escola: ')

        def dados(self):
                print('Nome: ',self.nome,' Idade: ',self.idade,' Escola: ',self.escola)

stu=pessoa()
stu.dados()
