import requests
import json

def consultar_cep():
    """
    Solicita um CEP ao usuário, consulta a API ViaCEP e exibe o endereço.
    Trata erros de conexão ou CEPs inválidos.
    """
    print("--- 🌍 Consulta de Endereço por CEP ---")
    
    # Solicita o CEP ao usuário
    # Remove espaços ou hífens para garantir que o formato seja apenas números
    cep = input("Digite o CEP (apenas números, ex: 01001000): ").strip().replace("-", "")
    
    # Validação simples do formato do CEP (deve ter 8 dígitos)
    if len(cep) != 8 or not cep.isdigit():
        print("\n❌ Falha: O CEP deve conter exatamente 8 dígitos numéricos.")
        return
    
    # URL da API ViaCEP
    # O formato da URL é: viacep.com.br/ws/{CEP}/json/
    API_URL = f"https://viacep.com.br/ws/{cep}/json/"
    
    print(f"\n🔎 Buscando informações para o CEP: {cep}...")
    
    try:
        # Faz a requisição GET para a API
        resposta = requests.get(API_URL)
        
        # Verifica se a requisição HTTP foi bem-sucedida (Status code 200)
        # Se não for 200, lança um erro e cai no 'except requests.exceptions.RequestException'
        resposta.raise_for_status()
        
        # Converte a resposta JSON em um dicionário Python
        dados = resposta.json()
        
        # Verifica se o CEP foi encontrado 
        if 'erro' in dados and dados['erro']:
            print("\n-----------------------------------------")
            print(f"❌ Falha: O CEP **{cep}** não foi encontrado.")
            print("Verifique se o número do CEP está correto.")
            print("-----------------------------------------\n")
            return
            
        # Extrai as informações desejadas
        # Uso .get() para evitar erros caso a API retorne algum campo vazio
        logradouro = dados.get('logradouro', 'Não Informado')
        bairro = dados.get('bairro', 'Não Informado')
        cidade = dados.get('localidade', 'Não Informado')
        estado = dados.get('uf', 'Não Informado')
        
        # Exibe os resultados
        print("\n-----------------------------------------")
        print("✅ Endereço Encontrado!")
        print(f"Logradouro: **{logradouro}**")
        print(f"Bairro: **{bairro}**")
        print(f"Cidade: **{cidade}**")
        print(f"Estado (UF): **{estado}**")
        print("-----------------------------------------\n")
        
    # Trata Erros de Conexão ou HTTP (Falha)
    except requests.exceptions.RequestException as e:
        # Este bloco captura erros se houver problema na sua internet ou a API estiver fora do ar
        print("\n-----------------------------------------")
        print("❌ Falha na conexão com a API.")
        print("Verifique sua conexão com a internet.")
        print(f"Detalhes do Erro: {e}")
        print("-----------------------------------------\n")
    except Exception as e:
        # Trata outros erros inesperados
        print(f"Ocorreu um erro inesperado: {e}")

# Executa a função principal
consultar_cep()