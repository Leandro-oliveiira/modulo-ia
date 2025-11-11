# Calculadora de consumo de combustível

# Distância total percorrida em quilômetros (km)
distancia_percorrida = 300 

# Quantidade total de combustível gasto em litros (L)
combustivel_gasto = 25 

# A fórmula do consumo médio é: Distância / Combustível Gasto
consumo_medio = distancia_percorrida / combustivel_gasto

# Arredondar o resultado
# A função round() serve para arredondar o consumo médio para duas casas decimais
consumo_arredondado = round(consumo_medio, 2)

# Exibir os resultados

# Imprime os dados de entrada
print(f"--- Dados da Viagem ---")
print(f"Distância Percorrida: {distancia_percorrida} km")
print(f"Combustível Gasto: {combustivel_gasto} L")

# Imprime o resultado final (Consumo Médio)
print(f"-----------------------")
print(f"O Consumo Médio do Veículo foi de: {consumo_arredondado} km/l")
print(f"-----------------------")