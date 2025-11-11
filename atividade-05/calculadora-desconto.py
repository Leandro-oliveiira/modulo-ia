def calcular_preco_com_desconto():
    # Interação com o usuário: Pedir os valores
    
    try:
        # Pede o preço original do produto (ex: 150.00)
        preco_original = float(input("Digite o preço original do produto (R$): "))
        
        # Pede a porcentagem de desconto (ex: 10 para 10%)
        porcentagem_desconto = float(input("Digite a porcentagem de desconto a aplicar (Ex: 15): "))
        
    except ValueError:
        print("\n🚫 Erro: Por favor, digite valores numéricos válidos.")
        return # Encerra a função se a entrada for inválida

    # Cálculo do Desconto 
    
    # Converte a porcentagem para um fator decimal. Ex: 15 / 100 = 0.15
    fator_desconto = porcentagem_desconto / 100
    
    # Calcula o valor exato do desconto em Reais (R$).
    valor_do_desconto = preco_original * fator_desconto
    
    # Cálculo do Preço Final 
    
    # Subtrai o valor do desconto do preço original.
    preco_final = preco_original - valor_do_desconto
    
    # Formatação e Exibição 
    
    # Arredonda todos os resultados para 2 casas decimais (centavos)
    preco_final_arredondado = round(preco_final, 2)
    valor_do_desconto_arredondado = round(valor_do_desconto, 2)
    
    print("\n--- Detalhes do Desconto ---")
    print(f"Preço Original: R$ {preco_original:.2f}")
    print(f"Desconto Aplicado: {porcentagem_desconto}%")
    
    print("----------------------------")
    print(f"Valor do Desconto: R$ {valor_do_desconto_arredondado:.2f}")
    print(f"Preço Final com Desconto: **R$ {preco_final_arredondado:.2f}**")
    print("----------------------------")

# Chama a função para iniciar 
calcular_preco_com_desconto()