carro = float(input('Qual é a velocidade do carro? '))
if carro > 80:
    print("Você passou de 80km, será muito em R${}".format(carro * 7))
else:
    print("Obrigado! Volte sempre!")