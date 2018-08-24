valp = float(input('Digite o valor do produto: R$ '))
vdesc = float(input('Digite o desconto: % '))
valcd = valp - (valp * vdesc / 100)
print('O produco no valor de R$ {:.2f}, com desconto de {}%, agora custa R$ {:.2f}'.format(valp, vdesc, valcd))