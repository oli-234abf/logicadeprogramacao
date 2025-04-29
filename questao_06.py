#Escreva um programa que peça ao usuário um ano
#e determine se ele é bissexto.
#a. Um ano é bissexto se for divisível por 4, mas não por
#100, a menos que seja divisível por 400.

ano = int(input("insira ano: "))

#resto_01 = ano%4
#resto_02 = ano%100
#resto_03 = ano%400

#print(resto_01,resto_02,resto_03)

#if res
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
