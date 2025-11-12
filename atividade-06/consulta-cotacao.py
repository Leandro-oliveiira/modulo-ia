import requests
import json

def consultar_cotacao():
    """
    Solicita uma moeda ao usuário, consulta sua cotação em relação ao BRL
    e exibe os detalhes. Trata erros de requisição ou moedas inválidas.
    """
    print("--- 💸 Consultor de Cotação de Moedas ---")
    
    # Solicita a moeda ao usuário
    moeda = input("Digite o código da moeda (ex: USD para Dólar, EUR para Euro): ").strip().upper()
    
    # Validação simples para garantir que a entrada não está vazia
    if not moeda:
        print("\n❌ Falha: Você deve digitar um código de moeda.")
        return
        
    # URL da API Awesome API
    # O formato URL é: awesomeapi.com.br/json/last/{MOEDA}-BRL
    API_URL = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    
    print(f"\n🔎 Buscando cotação de {moeda} em BRL...")
    
    try:
        # Faz a requisição GET para a API
        resposta = requests.get(API_URL)
        
        # Verifica se a requisição HTTP foi bem-sucedida (Status code 200)
        # Se não for 200, lança um erro e cai no 'except requests.exceptions.RequestException'
        resposta.raise_for_status()
        
        # Converte a resposta JSON em um dicionário Python
        dados = resposta.json()
        
        # Verifica se a moeda foi encontrada
        # A API retorna um erro específico (ex: 404) ou um dicionário vazio/simples de erro se a moeda for inválida
        chave_moeda = moeda + "BRL"
        if chave_moeda not in dados:
            print("\n-------------------------------------------")
            print(f"❌ Falha: A moeda **{moeda}** não foi encontrada ou é inválida.")
            print("Verifique se o código da moeda está correto (ex: USD, EUR, BTC).")
            print("-------------------------------------------\n")
            return
            
        # Extrai as informações desejadas
        cotacao = dados[chave_moeda]
        
        # Converte valores para float para formatação
        valor_atual = float(cotacao['bid'])
        valor_maximo = float(cotacao['high'])
        valor_minimo = float(cotacao['low'])
        
        # Extrai a data/hora e formata
        timestamp = int(cotacao['timestamp'])
        from datetime import datetime
        data_atualizacao = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')
        
        # Exibe os resultados
        print("\n-------------------------------------------")
        print(f"✅ Cotação **{cotacao['name']}** Encontrada!")
        print(f"Valor Atual de Compra: **R$ {valor_atual:.4f}**")
        print(f"Máxima do Dia (High): **R$ {valor_maximo:.4f}**")
        print(f"Mínima do Dia (Low): **R$ {valor_minimo:.4f}**")
        print(f"Última Atualização: **{data_atualizacao}**")
        print("-------------------------------------------\n")
        
    # Trata Erros de Conexão ou HTTP 
    except requests.exceptions.RequestException as e:
        # Captura erros de rede 
        print("\n-------------------------------------------")
        print("❌ Falha na conexão com a API.")
        print("Verifique sua conexão com a internet.")
        print(f"Detalhes do Erro: {e}")
        print("-------------------------------------------\n")
    except Exception as e:
        # Trata outros erros inesperados (como falha na conversão de dados)
        print(f"Ocorreu um erro inesperado: {e}")

# Executa a função principal
consultar_cotacao()