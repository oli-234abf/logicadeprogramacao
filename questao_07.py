#Peça ao usuário que digite sua idade e se tem um
#ingresso VIP (S ou N). A entrada é permitida se:
#a. A idade for maior ou igual a 18 ou se o usuário tiver um
#ingresso VIP.

idade = int(input("insira idade: "))
#ingresso_Vip = str(input("possui ingresso vip? "))
ingresso_Vip = input("possui ingresso vip? (S/N) ").strip().upper()
if idade >= 18 or ingresso_Vip == "S":
    print("entrada permitida")
else:
    print("Entrada proibida")