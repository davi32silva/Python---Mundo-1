viagem = float(input('Distância da Viagem: '))
if viagem >= 200:
    print('Total: R${}'.format(viagem * 0.45))
elif viagem < 200:
    print('Total: R${}'.format(viagem * 0.50))
