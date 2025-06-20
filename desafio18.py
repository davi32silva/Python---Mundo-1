import math

angulo = int(input("Digite um ângulo: "))
seno = math.sin(angulo)
cos = math.cos(angulo)
tg = math.tan(angulo)
print('Seno: {:.2}.\nCosseno: {:.2f}.\nTangente: {:.2f}.\n'.format(seno,cos,tg))