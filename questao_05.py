#Peça ao usuário sua idade e exiba o preço do ingresso:
#a. Menos de 12 anos: R$10,00
#b. Entre 12 e 17 anos: R$15,00
#c. 18 anos ou mais: R$20,00

idade_usuario = int(input("Informe idade do usuário: "))

if idade_usuario >= 18:
    ingresso = float(20.00)
    print("O valor do ingresso é: ",ingresso)
elif idade_usuario >= 12:
    ingresso = float(15.00)
    print("O valor do ingresso é: ",ingresso)
else:
    ingresso = float(10.00)
    print("O valor do ingresso é: ",ingresso)