import random
num = int(input("Qual é o número que eu pensei? "))
decisao = random.randint(1, 5)
if decisao == num:
    print('Você acertou! O número que eu pensei foi mesmo o {}'.format(num))
else:
    print('Você errou! O número que eu pensei foi {}'.format(decisao))

