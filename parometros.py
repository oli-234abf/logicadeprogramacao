#Faça uma função que receba uma temperatura em graus celcius e retorne em Fahrenheit

def fahreneit(C):
    F = C* (9/5)+32
    return F
temp = float(input("Insira uma temperatura em Celcius: "))
print("Temperatura(F): ",fahreneit(temp))

# #Faça uma função quee recebe o número inteiro e devolve o dobro:

def dobro (a):
    d = a * 2
    return d
x = int(input("Insira um valor inteiro: "))
dx = dobro(x)
print(f"Dobro de {x}: {dx}")

#Faça uma função que receba tres números inteiros como parâmetro (representando horas, minutos e segundos).Retorne valores em segundos:
# def hora (h, m, s):
#     segundos = (3600*h)+ (60*m)+s
#     return segundos
# h = float(input("Insira hora"))
# print(" em segundos: ",hora(h))

#F-strings
preco = 49.9
print(f"Preço: R${preco:.2f}")

#declarção de funlçoes

def soma (lista):
    s = 0
    for x in lista:
        s = s + x
    return s
def media (lista):
    m = soma(lista)/len(lista)
    return m
    #o que é declarado em def só é reconhecido em def
m = media ([8,5,4])
print(m)

#Recursão:
#Uma função que chama ela mesma
#função para calcular o fatorial:
def fatorial (x):
    if x == 0:
        return 1
    else:
        return x * fatorial(x -1)
x = int(input("Insira um número: "))
print(f"O fatorial de {x} é: ",fatorial(x))

