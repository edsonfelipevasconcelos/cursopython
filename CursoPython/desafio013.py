salario = float(input('Digite o Valor do salario atual: R$ '))
aumento = float(input('Digite o aumento em %: '))
nsalario = salario + (salario * aumento / 100)
print('O funcionário com o salário de R$ {:.2f}, e teve um aumento de {}%, agora receberá R$ {:.2f}.'.format(salario, aumento, nsalario))