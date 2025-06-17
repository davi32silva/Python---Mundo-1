dias = int(input('Quantos dias alugados: '))
km = float(input('Quilomêtros Rodados: '))
aluguel = (dias * 60) + (km * 0.15)
print('Valor total: R${}'.format(aluguel))