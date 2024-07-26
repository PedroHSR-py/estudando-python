l = float(input('Largura da parede '))
a = float(input('Altura da parede '))
ar = a * l
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(l, a, ar))
lt = ar * 2
print('Para pintar essa parede, você precisará de {:.2f}l de tinta'.format(lt))