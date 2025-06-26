reta1 = float(input('Primeira Reta: '))
reta2 = float(input('Segunda Reta: '))
reta3 = float(input('Terceira reta: '))
if reta1 < reta2 + reta3 and reta2 > reta1 + reta3 and reta3 < reta1 + reta2:
    print('É possível formar um triângulo')
else:
    print('Não pode formar um triângulo')