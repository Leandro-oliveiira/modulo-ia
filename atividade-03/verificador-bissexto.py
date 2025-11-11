def verificar_ano_bissexto():
    # Solicita o ano do usuário
    try:
        # Pede o ano e converte para um número inteiro (int)
        ano = int(input("Digite o ano que deseja verificar (ex: 2024): "))
        
        # Garante que o ano seja um número positivo (ou zero, embora 0 não seja bissexto)
        if ano < 0:
            print("🚫 Por favor, digite um ano válido (não negativo).")
            return
            
    except ValueError:
        # Trata o erro caso o usuário digite algo que não seja um número
        print("🚫 Entrada inválida. Por favor, digite um número inteiro para o ano.")
        return

    # Aplica a Regra do Ano Bissexto (Lógica)
    
    # Condição Principal: (divisível por 4 E não divisível por 100) OU (divisível por 400)
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        # Se a condição acima for VERDADEIRA
        resultado = True
        
    else:
        # Se a condição for FALSA
        resultado = False
    
    
    #  Exibi o resultado
    
    print(f"\n--- Verificação do Ano {ano} ---")
    if resultado:
        print(f"✅ O ano {ano} **É UM ANO BISSEXTO**.")
        print("Isso significa que Fevereiro terá 29 dias.")
    else:
        print(f"❌ O ano {ano} **NÃO É UM ANO BISSEXTO**.")
        print("Isso significa que Fevereiro terá 28 dias.")
    print("---------------------------------")

# Executa a função principal do programa
verificar_ano_bissexto()