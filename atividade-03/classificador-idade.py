# Classificador de idade

# garante que essa informação seja armazenada como um número inteiro.
idade = int(input("Por favor, digite sua idade: "))

# Estrutura de Decisão (if, elif, else)
if 0 <= idade <= 12:
    categoria = "Criança"
elif 13 <= idade <= 17:
    categoria = "Adolescente"
elif 18 <= idade <= 59:
    categoria = "Adulto"
elif idade >= 60:
    categoria = "Idoso"
else:
    categoria = "Idade inválida. Por favor, digite uma idade positiva."

# Exibi o resultado

# Imprime a classificação final para o usuário
print(f"\nSua idade é {idade} anos.")
print(f"Você se enquadra na categoria: **{categoria}**")

