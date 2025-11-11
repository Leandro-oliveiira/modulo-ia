# Calculadora IMC

# Pede o peso e converte para um número decimal (float), pois pesos geralmente têm vírgula.
peso = float(input("Digite seu peso em quilogramas (ex: 75.5): "))

# Pede a altura em metros e também converte para um número decimal.
altura = float(input("Digite sua altura em metros (ex: 1.70): "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Arredonda o resultado para duas casas decimais para uma melhor visualização
imc_arredondado = round(imc, 2)

# Classifica o IMC usando a estrutura if/elif/else
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"


# Exibir os resultados
print(f"\n--- Resultado do Cálculo de IMC ---")
print(f"Seu Peso: {peso} kg")
print(f"Sua Altura: {altura} m")
print(f"Seu IMC é: **{imc_arredondado}**")
print(f"Classificação: **{classificacao}**")
print(f"----------------------------------")