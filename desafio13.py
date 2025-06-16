s = float(input('Qual é o seu salário? '))
ns = s + (s * 0.15)
print('Com o aumento de 15%, o salário de R${:.2f} ficou em R${:.2f}'.format(s,ns))