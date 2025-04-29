#tipos de laço
#estrutura break
# print("estrutura break")
# a = int(input("Insira A: "))
# b = int(input("Insira B: "))

# while a <= b:
#     a = a + 1
#     if a == 5:
#         break
#     print(a)
# print("Fim do laço")

# #estrutura continue
# print("estrutura continue")

# a1_ = int(input("Insira A: "))
# b1_ = int(input("Insira B: "))
# while a <= b:
# 	a = a + 1
# 	if a == 5:
# 		continue
# 	print (a)
# print ("Fim do laco")

# #repeticao com teste no fim
# #while true significa que essa repeticao sempre vai ser verdadeira e essa repeticao vai ser quebrada com o break
# print("estrutura while true com teste")
# a2_ = int(input("Insira A: "))
# b2_ = int(input("Insira B: "))
# while True:
# 	print (a)
# 	a = a + 1
# 	if a > b:
# 		break
	
# print ("Fim do laco")

while True:
	nota = float(input("Insira nota: "))
	if nota >= 0 and nota<=10:
		break
	else:
		print("nota invalida!")
print("Nota valida")
