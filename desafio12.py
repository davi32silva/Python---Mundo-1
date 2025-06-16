preco = float(input("Valor do Produto: "))
desc = preco - (preco * 0.05)
print('Com o desconto de 5%, o valor de R${:.2f}, agora fica por R${:.2f}'.format(preco, desc))