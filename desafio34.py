salario = float(input('Qual é o seu salário? '))
if salario > 1250:
    aumento10 = salario + (salario * 0.10)
    print('Com um aumento de 10%, seu salário fica em R${}'.format(aumento10))
else:
    aumento15 = salario + (salario * 0.15)
    print('Com o aumento de 15%, o salário fica em R${}'.format(aumento15))
