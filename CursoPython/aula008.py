#import math
from math import sqrt, floor
num = int(input('Digite um numero: '))
raiz = sqrt(num)
#print('A raiz quadrada de {} é igual á {}'.format(num, math.ceil(raiz)))
#print('A raiz quadrada de {} é igual á {}'.format(num, math.floor(raiz)))
print('A raiz quadrada de {} é igual á {:.2f}'.format(num, floor(raiz)))
