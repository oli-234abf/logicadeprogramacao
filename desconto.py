#Escreva um programa que peça o preço de um produto
#e um percentual de desconto. O algoritmo deve calcular
#o valor final do produto após o desconto
preco_produto = float(input("preço do produto: "))
desconto = float(input("desconto: "))

p_desconto = -(desconto - preco_produto)

v_total = (p_desconto/preco_produto)*100

print("o produto tem ",v_total," de desconto")