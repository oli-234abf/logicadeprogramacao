#4. Escreva um programa que peça ao usuário sua idade e
#exiba:
#a. "Criança" se for menor que 12 anos
#b. "Adolescente" se for entre 12 e 17 anos
#c. "Adulto" se for 18 anos ou mais

idade_usuario = int(input("informe idade: "))

if idade_usuario >= 18:
    print("Adulto")
elif idade_usuario>=12:
    print("Adolecente")
else:
    print("Criança")