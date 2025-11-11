def conversor_temperatura():
    # Solicita a temperatura e as unidades
    try:
        # Pede o valor da temperatura e converte para um número decimal (float)
        temperatura = float(input("Digite o valor da temperatura: "))
        
        # Pede a unidade de origem e converte para maiúsculas para facilitar a comparação (ex: 'c' vira 'C')
        unidade_origem = input("Unidade de origem (C, F ou K): ").upper()
        
        # Pede a unidade de destino
        unidade_destino = input("Converter para (C, F ou K): ").upper()

    except ValueError:
        # Trata o erro caso o usuário digite um valor não numérico para a temperatura
        print("\n🚫 Erro: O valor da temperatura deve ser um número válido.")
        return # Encerra a função se houver erro

    # Verifica se a conversão é necessária (se as unidades forem diferentes)
    if unidade_origem == unidade_destino:
        print(f"\n✅ Resultado: {temperatura:.2f} {unidade_origem} (As unidades de origem e destino são as mesmas).")
        return

    # Realiza o cálculo da conversão
    
    # O Python fará as contas, então precisamos de uma variável para guardar o resultado
    temp_convertida = None
    
    # Conversões de Celsius (C)
    if unidade_origem == 'C':
        if unidade_destino == 'F':
            # C para F: (C * 9/5) + 32
            temp_convertida = (temperatura * 9/5) + 32
        elif unidade_destino == 'K':
            # C para K: C + 273.15
            temp_convertida = temperatura + 273.15
        
    # Conversões de Fahrenheit (F)
    elif unidade_origem == 'F':
        if unidade_destino == 'C':
            # F para C: (F - 32) * 5/9
            temp_convertida = (temperatura - 32) * 5/9
        elif unidade_destino == 'K':
            # F para K: (F - 32) * 5/9 + 273.15
            temp_convertida = (temperatura - 32) * 5/9 + 273.15
        
    # Conversões de Kelvin (K)
    elif unidade_origem == 'K':
        if unidade_destino == 'C':
            # K para C: K - 273.15
            temp_convertida = temperatura - 273.15
        elif unidade_destino == 'F':
            # K para F: (K - 273.15) * 9/5 + 32
            temp_convertida = (temperatura - 273.15) * 9/5 + 32
        
    # Exibe o resultado ou mensagem de erro

    if temp_convertida is not None:
        # Se a conversão foi realizada, exibe o resultado arredondado para 2 casas decimais
        print(f"\n--- Resultado da Conversão ---")
        print(f"{temperatura:.2f} {unidade_origem} é igual a **{temp_convertida:.2f} {unidade_destino}**")
        print(f"-----------------------------")
    else:
        # Se a variável temp_convertida ainda for None, é porque as unidades digitadas eram inválidas
        print("\n🚫 Erro: Unidades de temperatura inválidas. Use apenas C (Celsius), F (Fahrenheit) ou K (Kelvin).")

# Executa a função principal do programa
conversor_temperatura()