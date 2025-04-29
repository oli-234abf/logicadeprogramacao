#Crie um programa que peça a idade do usuário e exiba quantos dias
#ele já viveu (considerando que um ano tem 365 dias).
nome = str(input("Seja bem-vindo "))
idade = int(input("por favor informe sua idade: "))

def calcular_dias_de_vida(idade):
    dias_por_ano = 365.25  # Considerando anos bissextos
    dias_de_vida = idade * dias_por_ano
    return int(dias_de_vida)


dias = calcular_dias_de_vida(idade)
print(f"Você viveu aproximadamente {dias} dias.")