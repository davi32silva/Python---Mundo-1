nome = input("Qual é o seu nome? ").strip()
#Letras maiúsculas
print(nome.upper())
#Letras minúsculas
print(nome.lower())
#Quantidade de letras(Sem espaço)
print((len(nome) - nome.count(' ')))
#Quantidade de letras do Primeiro Nome
print(nome.find(' '))