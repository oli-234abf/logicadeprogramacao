#7. Desenvolva um programa que peça o valor de um produto e o valor
#pago pelo cliente. O algoritmo deve calcular e exibir o troco.


valor_Total = int(input("valor do produto: "))
valor_Pago = int(input("valor entregue: "))

restante = -(valor_Total - valor_Pago)

print( "o troco que deve ser devolvido ao cliente é: ",restante)
