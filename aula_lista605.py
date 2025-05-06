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
A = [1,2,3,4,5,6]

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

notas = []

for i in range(5):
    nota = float(input("insira nota: "))
    notas.append(nota)

soma = 0
for x in notas:
    soma = soma + x
media = soma /len(notas)

for x in notas:
    print(x)
    print("a media das notas é: ",media)
