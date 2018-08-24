import math
cop = float(input('Comprimento do cateto oposto: '))
cad = float(input('Comprimento do cateto adjacente: '))
#hip = math.hypot(cop, cad)
hip = (cop ** 2 + cad ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}.'.format(hip))