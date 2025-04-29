print("Bem vindo usuário")

nome_usuario = str(input("nome do usuário: "))
password_usuario = int(input("senha: "))

if nome_usuario == "adm" and password_usuario == 123:
    print("Acesso permitido ",nome_usuario)
else:
    print("Acesso negado")