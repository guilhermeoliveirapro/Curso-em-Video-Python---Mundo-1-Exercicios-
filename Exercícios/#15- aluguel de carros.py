dias = int(input('quantos dias alugados? '))
km = float(input('quantos km rodados? '))
p1 = (60*dias)
p2 = (0.15*km)
p3 = (p1 + p2)
print('o total a pagar é de R${:.2f}'.format(p3))
