#06/05/2025--Lista
# n1 = float(input("Insira nota aluno 1: "))
# n2 = float(input("Insira nota aluno 2: "))
# n3 = float(input("Insira nota aluno 3: "))
# n4 = float(input("Insira nota aluno 4: "))
# n5 = float(input("Insira nota aluno 5: "))

# media = (n1+n2+n3+n4+n5)/5
# if n1 > media:
#     print("Maior que a media", n1)
# if n2 > media:
#     print("Maior que a media", n2)
# if n3 > media:
#     print("Maior que a media", n3)
# if n4 > media:
#     print("Maior que a media", n4)
# if n5 > media:
#     print("Maior que a media", n5)

#listas de declaração
# compras =["miojo","Ovo","leite","Pão"]
# print(compras[0])
# print(compras[1])
# len(compras)

# #utilizando os elementos da lista
# for x in compras:
#     print(x)

# for i in range(len(compras)):
#     print(compras[1])

#Atividade: faça um programa que possua um vetor denominado A que armazene 6 números inteiros.
# A = [1,2,3,4,5,6]

#a__Atribua os seguintes valores a esse vetor:1,0,5,-2,-5,7

# A = [1,0,5,-2,-5,7]

# #b__Armazene em uma variavel inteira (simples) a soma entre os valores da posiçaõ 0,1,5

# soma = A[0] + A[1] + A[5]
# print(soma)
# #modifique o vetor na posição 4, atribuindo valor de 100

# A[4] = 100

# for x in A:
#     print(x)

#d__mostre na tela cada valor do Vetor A, umn em cada linha

#ERRADO:
# print(A[0])
# print(A[1])
# print(A[2])
# print(A[3])
# print(A[4])
# print(A[5])

#leias as notas de uma turma de uma turma de cinco estudantes e depois imprima as notas que são maiores do que a média da turma
#MEU CÓDIGO:
# notas = []

# for i in range(5):
#     nota = float(input("insira nota: "))
#     notas.append(nota)

# soma = 0
# for x in notas:
#     soma = soma + x
# media = soma /len(notas)

# print("as notas são: ")
# for x in notas:
#     print(x)
#     if x > media:
#         print(x, "maior que a media")

# print("a media da nota dos cinco alunos: ",media)

#CODIGO DO PROFESSOR:
# notas = []

# for i in range(5):
#     nota = float(input("insira nota: "))
#     notas.append(nota)

# soma = 0
# for x in notas:
#     soma = soma + x
# media = soma /len(notas)

# for x in notas:
#     if x > media:
#         print( "nota maior que a media", x)

# print("a media da nota dos cinco alunos: ",media)

#Para uma lista contendo 5 números inteiros, formular um algorítimo que determine o maior elemento desta lista

# num = [1, 2, 3, 4, 5]

# # print(max(num))
# # print(min(num))

# maior = num [0]
# for x in num:
#     if x > maior:
#         maior = x
# print(maior)

# menor = num [0]
# for x in num:
#     if x < menor:
#         menor = x
# print(menor)

# crie um programa que le 6 valores inteiros e, em seguida, mostre na tela o valores lidos
# valores = []
# for i in range(6):
#     valor = int(input("insira valor: "))
#     valores.append(valor)

# for numero in valores:
#     print(numero)

#ler um conjunto de numeros reais, armazenando-os em lista e calcular o quadrado das componentes desta lista, armazenando em outra lista.os
#conjuntos têm 10 elementos cada.Imprimir todos os conjuntos

num_reais = []
num_quadrado = []
for i in range(10):
    num = float(input("Insira número real: "))
    num_reais.append(num)

for x in num_reais:
    quadrado = x * x
    num_quadrado.append(quadrado)
print(num_reais)
print(num_quadrado)
#tinha que sair do for








