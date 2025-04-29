quant_produtos = int(input("quantidade de produtos comprados: "))
preco = float(input("valor da compra: "))

total = quant_produtos * preco

if quant_produtos >= 10 and total > 100:
    desc = float(15)
    tot_final = float(total % desc)
    print("a compra foi no valor: ", total,"o desconto recebido: ",desc, " e o valor final da compra: ", tot_final)
elif quant_produtos >= 5 and total >= 50:
    desc = float(10)
    tot_final = float(total % desc)
    print("a compra foi no valor: ", total,"o desconto recebido: ",desc, " e o valor final da compra: ", tot_final)
else:
    print("não há desconto, o valor é: ",total)