import math
a = int(input("Cateto oposto: "))
b = int(input("Cateto adjacente: "))
hipo = math.hypot(a,b)
print('A hipotenusa desses catetos é: {:.1f}cm'.format(hipo))
