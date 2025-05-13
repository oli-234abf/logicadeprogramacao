while True:
    N = int(input("insira N: "))
    if N > 0 and N % 2 == 0:
        break
    else:
        print("Número inválido")

for x in range(N+1):
    if x % 2 == 0:
        print (x)