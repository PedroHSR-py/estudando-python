p = float(input('Qual é o preço do produto? R$'))
d = p * 0.05
d1 = p - d
print('O produto que custava {}, na promoção com desconto de 5% vai custar {:.2f}'.format(p, d1))