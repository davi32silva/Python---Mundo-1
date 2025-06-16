valor = float(input('Qual é a distância em metros? '))
cm = valor / 100
mm = valor / 1000
print('Valor {:.2f} em cm: {:.2f}'.format(valor,cm))
print('Valor {:.2f} em mm: {:.2f}'.format(valor, mm))