# Este programa soma dois numeros inseridos pelo usuário

# Solicita ao usuário que insira dois números inteiros
numero1 = int(input("Digite um número inteiro"))
numero2 = int(input("Digite outro número inteiro"))

#calcula a soma dos números
soma = numero1 + numero2

#Exibe o resultado (formatado com f-string)
print(f"A soma de {numero1} + {numero2} é: {soma} ")