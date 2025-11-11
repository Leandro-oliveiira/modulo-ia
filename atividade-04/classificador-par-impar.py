def classificar_numeros():
    # Variáveis para contabilizar os números
    contador_pares = 0
    contador_impares = 0
    
    print("--- Classificador de Números ---")
    print("Digite um número por vez. Digite 'fim' a qualquer momento para ver o resultado.")
    
    # O loop principal continua rodando até que o usuário digite 'fim'
    while True:
        entrada = input("Digite um número inteiro (ou 'fim'): ")
        
        # Condição de Saída do Loop
        if entrada.lower() == 'fim':
            break # Interrompe o loop e vai para a fase de resultados
            
        # Tratamento de Entrada e Classificação
        try:
            # Converte a entrada para um número inteiro
            numero = int(entrada)
            
            # Usa o operador MÓDULO (%) para verificar a paridade:
            # Se o resto da divisão por 2 for 0, o número é PAR.
            if numero % 2 == 0:
                print(f"-> {numero} é PAR.")
                contador_pares += 1 # Incrementa o contador de pares
            
            # Caso contrário, o número é ÍMPAR.
            else:
                print(f"-> {numero} é ÍMPAR.")
                contador_impares += 1 # Incrementa o contador de ímpares
                
        except ValueError:
            # Trata o erro se o usuário digitar algo que não é número nem "fim"
            print("🚫 Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")
            continue # Volta para o início do loop

    # Exibi o Resultado Final
    
    print("\n--- Resultado Final da Análise ---")
    
    if contador_pares == 0 and contador_impares == 0:
        print("Nenhum número válido foi inserido.")
    else:
        print(f"Total de Números Pares inseridos: **{contador_pares}**")
        print(f"Total de Números Ímpares inseridos: **{contador_impares}**")
        
    print("----------------------------------")

# Inicia o programa
classificar_numeros()