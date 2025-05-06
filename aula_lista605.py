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
##############
# crie um programa que le 6 valores inteiros e, em seguida, mostre na tela o valores lidos
# valores = []
# for i in range(6):
#     valor = int(input("insira valor: "))
#     valores.append(valor)

# for numero in valores:
#     print(numero)

#ler um conjunto de numeros reais, armazenando-os em lista e calcular o quadrado das componentes desta lista, armazenando em outra lista.os
#conjuntos têm 10 elementos cada.Imprimir todos os conjuntos

# num_reais = []
# num_quadrado = []
# for i in range(10):
#     num = float(input("Insira número real: "))
#     num_reais.append(num)

# for x in num_reais:
#     quadrado = x * x
#     num_quadrado.append(quadrado)
# print(num_reais)
# print(num_quadrado)
#tinha que sair do for

#3__Leia uma lista de 10 posições. Contar e escrever quantos valores pares ela possui.

# posicoes = []

# for i in range (10):
#     numero = int(input("Insira número: "))
#     posicoes.append(numero)

# print("a lista possui ", i, "posições")
# print(posicoes)

#4__Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá ser impresso o maior e o menor elemento do vetor.

# vetor = []

# for i in range(10):
#     elemento = int(input("insira elemento:"))
#     vetor.append(elemento)
# print("O maior elemento do vetor é: ",max(vetor))
# print("O menor elemento do vetor é: ",min(vetor))

# #5__Faça um programa que receba 6 números inteiros e mostre: 
#  Os números pares digitados; 
# A soma dos números pares digitados;
# Os números ímpares digitados; 
# A quantidade de números ímpares digitados;

# num_inteiro = []
# pares = []
# impares = []
# for i in range (6):
#     numero = int(input("insira número inteiro: "))
#     num_inteiro.append(numero)
# # pares = numero / 2
# print("os números pares digitados são: ")
# soma = 0
# for x in num_inteiro:
#     if x % 2 == 0:
#         par = x
#         soma = soma + x
#         pares.append(par)
#     else:
#         impar = x
#         impares.append(impar)
        
# print("Os números pares são: ",pares)
# print("Soma dos números pares: ",soma)
# print("Os números ímpares são: ",impares)
# print("Quatidade de números impares: ",len(impares))

#6__Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando elementos repetidos.

# numeros = []
# for i in range(20):
#     num = int(input(f"Digite o {i+1}º número inteiro: "))
#     numeros.append(num)

# sem_repetidos = []
# for num in numeros:
#     if num not in sem_repetidos:
#         sem_repetidos.append(num)

# print("\nNúmeros sem repetição:")
# print(sem_repetidos)














