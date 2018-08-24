import random
n1 = str(input('Digite o nome do 1º aluno: '))
n2 = str(input('Digite o nome do 2º aluno: '))
n3 = str(input('Digite o nome do 3º aluno: '))
n4 = str(input('Digite o nome do 4º aluno: '))
sorteio = random.choice([n1, n2, n3, n4])
print(sorteio)