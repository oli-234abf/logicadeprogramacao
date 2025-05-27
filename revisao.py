#while:
print("Comando while:")
cont = 100 #basta mudar esse valor
while cont >= 0:#se atentar para a troca da sintaxe
    print(cont , end = " ") #end permite que continue printando na mesma linha
    cont -= 1

#atribuição composta
# print("Atribuição composta:")
# cont = 1
# soma = 1
# while cont < 10:
#     print(cont)
#     soma += cont

#range: lista com uma sequencia de números
# range(5)
print("Comando range:")
for x in range(10,51,2):
    print(x)

#comando break: quando eu quero parar o laço
print("Comando break:")
for x in range(10,-1,-1):
    if x == 4:
        break
    print(x)

#continue(break sai do laço e continua pra outra parte do laço)
print("Comando continue:")
for x in range(10,-1,-1):
    if x == 4:
        continue
    print(x)

#repeticação com teste no ínicio(ex.:while)
# repetição com teste no fim (não tem em python) 

#Declaração de listas: 
print("Lista declaração:")
compras = ["Miojo","Ovo","Leite","Pão"]
print(compras[0])
print(compras[1])
print(len(compras))

print("Lista de números:")
numeros = [8,6,9,11,1]
for x in numeros:
    if x%2 == 0:
         continue
    print(x)

#métodos sobre lista

numeros.sort()
print(numeros)
#ponto sort não repete valores

#append(sempre posiciona o número no final da lista):

print("append:")
numeros.append(18)
print(numeros)

#insert, posso escolher a posição:
print("Adicionando número 15 na posição 2:")
numeros.insert(2,15)
print(numeros)

#remove,remove o elemento que eu quero tirar
print("Removendo elemnto 11:")
numeros.remove(11)
print(numeros)

#pop(retira elemento pela posiçaõ)
print("tirando pela posição:")
numeros.pop(2)
print(numeros)

#exercicio
print("Exiba o número 9:")
print(numeros[3])

#leia 10 números do usuario:
print("Lendo 10 números do usuário:")
lista_num_usuario = []

for i in range(10):   
        x = int(input(f"Insira {i+1}º número: "))
        lista_num_usuario.append(x)
print(lista_num_usuario)
contagem = 0
for i in range(10):
     if i %3 == 0:
          contagem +=1
print(f"{contagem} números múltiplos de 3")

