def calculadora():
    # Solicita a entrada dos números e da operação
    try:
        # Pede o primeiro número e o converte para float (permite decimais)
        num1 = float(input("Digite o primeiro número: "))
        
        # Pede o segundo número
        num2 = float(input("Digite o segundo número: "))
        
        # Pede a operação desejada
        operador = input("Escolha a operação (+, -, *, /): ")
        
    except ValueError:
        print("\n🚫 Erro: Por favor, digite números válidos.")
        return # Encerra a função em caso de erro de entrada

    # Realiza o cálculo baseado no operador
    
    if operador == '+':
        resultado = num1 + num2
    
    elif operador == '-':
        resultado = num1 - num2
        
    elif operador == '*':
        resultado = num1 * num2
        
    elif operador == '/':
        # Condição de segurança: verifica se o divisor não é zero
        if num2 != 0:
            resultado = num1 / num2
        else:
            # Trata o erro de divisão por zero
            print("\n🚫 Erro: Não é possível dividir por zero.")
            return
            
    else:
        # Trata o erro se o operador for inválido
        print("\n🚫 Erro: Operador inválido. Use apenas +, -, * ou /.")
        return

    # 3. Exibe o resultado
    print(f"\n--- Resultado ---")
    # Exibe a operação e o resultado arredondado para duas casas decimais
    print(f"{num1} {operador} {num2} = **{round(resultado, 2)}**")
    print(f"-----------------")

# Chama a função para iniciar a calculadora
calculadora()