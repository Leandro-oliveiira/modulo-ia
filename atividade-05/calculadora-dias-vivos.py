from datetime import date # Importa o módulo 'date' para trabalhar com datas

def calcular_dias_vivos():
    # Data de Nascimento do Usuário
    
    print("--- Calculadora de Dias de Vida ---")
    print("Por favor, digite sua data de nascimento.")
    
    try:
        # Pede o ano, o mês e o dia separadamente para facilitar a entrada
        ano = int(input("Ano (ex: 1990): "))
        mes = int(input("Mês (ex: 05): "))
        dia = int(input("Dia (ex: 28): "))
        
        # Cria um objeto de data com os dados do usuário
        data_nascimento = date(ano, mes, dia)
        
    except ValueError:
        # Trata o erro se o usuário digitar algo inválido (ex: mês 13)
        print("\n🚫 Erro: Por favor, digite datas válidas (números inteiros para ano, mês e dia).")
        return
        
    # Data Atual
    
    # date.today() pega a data do seu computador neste momento
    data_hoje = date.today()
    
    # Calcula a Diferença (Delta de Tempo)
    
    # Quando subtraímos duas datas, o resultado é um objeto 'timedelta'
    diferenca = data_hoje - data_nascimento
    
    # O objeto 'diferenca' tem um atributo chamado '.days' que nos dá o total
    # de dias nessa diferença
    dias_vivos = diferenca.days
    
    # Exibi o Resultado
    
    # Verifica se a data de nascimento é válida (não pode ser no futuro)
    if dias_vivos < 0:
        print("\n🤔 Sua data de nascimento não pode ser no futuro! Verifique a data.")
        return
        
    print("\n==============================================")
    print(f"Data de Nascimento Registrada: {data_nascimento.strftime('%d/%m/%Y')}")
    print(f"Data de Hoje: {data_hoje.strftime('%d/%m/%Y')}")
    print("----------------------------------------------")
    print(f"Você está vivo há um total de **{dias_vivos} dias**!")
    print("==============================================")

# Inicia o programa
calcular_dias_vivos()