#Escreva um programa que peça ao usuário para digitar uma
#senha. Se a senha digitada for "1234", exiba "Acesso
#permitido.", senão, exiba "Acesso negado.".

senha = int(input("digite senha: "))

if senha == 1234:
    print("Acesso permitido")
else:
    print("Acesso negado")