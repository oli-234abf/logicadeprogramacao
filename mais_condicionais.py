#Escreva um programa que solicite ao usuário um número e,
#se o número for maior que 0, exiba "Número positivo.".

nota = float(input("informe nota: "))

if nota >=7:
    print("aprovado")
else:
    if nota >= 5:
        print("Recuperação")
    else:
        print("Reprovado")
        
#if nota >= 7:
#print ("Voce foi aprovado")
#elif nota >= 5
#print ("Voce fara prova final")
#else:
#print ("Voce foi reprovado")