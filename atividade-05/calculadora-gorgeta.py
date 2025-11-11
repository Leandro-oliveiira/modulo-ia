def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    # Converter a porcentagem para um valor decimal
    # Exemplo: Se porcentagem_gorjeta for 10, o fator_gorjeta será 0.10
    fator_gorjeta = porcentagem_gorjeta / 100
    
    # Calcula o valor da gorjeta    
    valor_gorjeta = valor_conta * fator_gorjeta
    
    # Arredonda o resultado para duas casas decimais para representar dinheiro
    return round(valor_gorjeta, 2)


# Defini os valores de entrada
valor_total = 75.50 # Valor da conta em Reais
porcentagem_desejada = 15 # 15% de gorjeta

# Chama a função
gorjeta = calcular_gorjeta(valor_total, porcentagem_desejada)

# Exibi os resultados
print(f"Valor total da conta: R$ {valor_total:.2f}")
print(f"Porcentagem de gorjeta: {porcentagem_desejada}%")
print(f"O valor da gorjeta a ser deixada é: **R$ {gorjeta:.2f}**")

# Calcula o valor total a pagar
valor_total_a_pagar = valor_total + gorjeta
print(f"O valor final total a pagar é: R$ {valor_total_a_pagar:.2f}")