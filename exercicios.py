# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# numero1 = int(input("Digite um número inteiro: "))
# numero2 = int(input("Digite outro número inteiro: "))

# soma = numero1 + numero2
# print(f"A soma de {numero1} e {numero2} é {soma}.")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# numero = int(input("Digite um número inteiro: "))
# divisor = 5

# resto = numero % divisor
# print(f"O resto de {numero} por {divisor} é {resto}.")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# numero1 = int(input("Digite um número inteiro: "))
# numero2 = int(input("Digite outro número inteiro: "))

# multiplicacao = numero1 * numero2
# print(f"A multiplicação de {numero1} e {numero2} é {multiplicacao}.")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# numero1 = int(input("Digite um número inteiro: "))
# numero2 = int(input("Digite outro número inteiro: "))

# divisao = numero1 // numero2
# print(f"A divisão inteira de {numero1} e {numero2} é {divisao}.")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# try:
#     numero1 = float(input("Digite um número flutuante: "))
#     numero2 = float(input("Digite outro número flutuante: "))
#     media = (numero1 + numero2) / 2
#     print(f"A média de {numero1} e {numero2} é {media}.")
# except ValueError:
#     print("Digite apenas números validos.")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# código fraco
# palavra = input("Digite uma palavra: ")
# print(palavra.upper())

# codigo melhor
# palavra = input("Digite uma palavra: ")
# if isinstance(palavra, str):
#      print(palavra.upper())
# else:
#     print ("Erro: O input deve ser uma string.")
        

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# palavra = input("Digite uma palavra: ")
# if isinstance(palavra, str):
#      print(palavra.lower())
# else:
#     print ("Erro: O input deve ser uma string.")

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# frase = input("Digite uma frase: ")
# print(frase.strip())

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# data = input("Digite uma data no formato dd/mm/aaaa: ")
# data_list = data.split("/")
# print(f"O Dia digitado foi {data_list[0]}!")
# print(f"O Mês digitado foi {data_list[1]}!")
# print(f"O Ano digitado foi {data_list[2]}!")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# Exemplo de entrada
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.



# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação