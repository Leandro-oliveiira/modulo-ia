def verificar_senha():
    # Solicita a senha ao usuário
    senha = input("Crie sua senha: ")

    # Verifica os Critérios de Segurança

    # Critério A: Comprimento Mínimo (8 caracteres)
    # A função len() conta o número de caracteres na string (senha).
    tem_oito_caracteres = len(senha) >= 8

    # Critério B: Conter Pelo Menos Um Número
    tem_numero = False # Começa assumindo que não tem número
    
    # Percorre cada caractere dentro da senha
    for caractere in senha:
        # Verifica se o caractere atual é um dígito (número)
        if caractere.isdigit():
            tem_numero = True # Se encontrar um número, muda para True
            break # Interrompe o loop, pois a condição foi atendida

    # Exibi o Resultado
    
    print("\n--- Relatório de Segurança ---")

    # Verifica se AMBOS os critérios foram atendidos (usando 'and')
    if tem_oito_caracteres and tem_numero:
        print("✅ **SUCESSO!** A senha atende aos critérios básicos de segurança.")
        
    else:
        print("❌ **FALHA!** A senha não atende a todos os critérios. Motivos:")
        
        # Indica qual critério falhou
        if not tem_oito_caracteres:
            print("- A senha deve ter pelo menos 8 caracteres. (Atual: {} car.)".format(len(senha)))
            
        if not tem_numero:
            print("- A senha deve conter pelo menos um número.")
            
    print("------------------------------")

# Executa a função do verificador de senha
verificar_senha()