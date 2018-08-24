km = float(input('KM rodados: '))
dias = int(input('Dias aluguel: '))
valor = (km * 0.15) + (dias * 60)
print('O valor total do aluguel de {} dias, mais {}km rodas é R$ {:.2f}'.format(dias, km, valor))