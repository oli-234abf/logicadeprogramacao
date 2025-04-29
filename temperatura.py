#Crie um programa que leia uma temperatura em graus
#Celsius e a converta para Fahrenheit usando a fórmula:
#a. F=(C×9/5)+32
print("Olá! Converteremos temperatura de Celcius para Fahrenheit ")

T_Celcius = float(input("Informe temperatura em Celcius: "))

T_Fahrenheit = (T_Celcius*9/5)+32

print("A temperatura apresentada em Celcius em Fahrenheit é: ",T_Fahrenheit)