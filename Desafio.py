CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite o seu nome: ")
if nome_usuario.isdigit():
    nome_usuario = input("Nome inválido. Digite o seu nome: ")
elif nome_usuario == "":
    nome_usuario = input("Nome inválido. Digite o seu nome: ")
elif nome_usuario.isspace():
    nome_usuario = input("Nome inválido. Digite o seu nome: ")
elif int(nome_usuario) <= 0:
    nome_usuario = input("Nome inválido. Digite o seu nome: ")
else:
    pass

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario_usuario = float(input("Digite o seu salario: "))
if salario_usuario <= 0:
    salario_usuario = float(input("Salário inválido. Digite o seu salario: "))
elif salario_usuario.isspace():
    salario_usuario = float(input("Salário inválido. Digite o seu salario: "))
else:
    pass

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus_usuario = float(input("Digite o seu bonus: "))

# 4) Calcule o valor do bônus final

valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor do bonus
print(f"O usuario {nome_usuario} possui o bonus de {valor_do_bonus}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?