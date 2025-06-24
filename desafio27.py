nome= str(input('Qual é o seu nome completo? ')).strip()
separador = nome.split()
print('Primeiro nome: {}'.format(separador[0]))
print('Último nome: {}'.format(separador[len(separador) - 1]))