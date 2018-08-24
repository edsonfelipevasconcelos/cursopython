lp = float(input('Largura da parede: '))
ap = float(input('Altura da parede: '))
ar = lp * ap
lt = ar / 2
print('Sua parede tem a dimensão de {} X {} e sua área é {}M²'.format(lp, ap, ar))
print('Para pintar essa parede, voce precisará de {}L de tinta'.format(lt))
