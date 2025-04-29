#Fac¸a um programa que determine o mostre os cinco primeiros multiplos de 3, conside- ´
#rando numeros maiores que 0.
# num = 1
# cont = 0
# while cont < 5:
#     if num % 3 == 0:
#         print(num)
#         cont = cont +1
#     num = num +1

#Fac¸a um programa que pec¸a ao usuario para digitar 10 valores e some-os.

##errado:
# cont = 1

# while cont< 10:
#     valor = int(input("insira valor: "))
    
#     cont = valor + 1
#     if cont == 10:
#         break
#     print(cont)
# print(cont,"fim do laço")##

for i in range(10):
    num = int(input("Insira numero: "))

soma = 0 
for i in range(10):
    num_02 = int(input("insira numero: "))
    soma = soma + num_02
print("Somatorio: ",soma)

cont = 0
while cont < 10:
    num = int(input("insira um número: "))
    cont = cont + 1
    























