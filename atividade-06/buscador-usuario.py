import requests
import json

def buscar_usuario_aleatorio():
    """
    Busca um usuário fictício aleatório da API e exibe suas informações.
    Trata erros de conexão.
    """
    # URL da API que retorna um usuário aleatório
    API_URL = "https://randomuser.me/api/"
    
    print("--- 🔎 Buscando Usuário Fictício... ---")
    
    try:
        # Faz a requisição GET para a API
        # O 'requests.get()' tenta se conectar e obter os dados
        resposta = requests.get(API_URL)
        
        # Verifica se a requisição foi bem-sucedida (Status code 200)
        # O método 'raise_for_status()' lança um erro HTTP se a resposta não for 200 OK
        resposta.raise_for_status()
        
        # Converte a resposta JSON em um dicionário Python
        dados = resposta.json()
        
        # A API retorna um dicionário com uma chave 'results' que é uma lista de usuários
        usuario = dados['results'][0]
        
        # Extrai as informações desejadas
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
        # Exibe os resultados
        print("\n----------------------------------")
        print("✅ Usuário Fictício Encontrado!")
        print(f"Nome: **{nome}**")
        print(f"E-mail: **{email}**")
        print(f"País: **{pais}**")
        print("----------------------------------\n")
        
    # Trata Erros de Conexão ou HTTP (Falha)
    except requests.exceptions.RequestException as e:
        # Este bloco captura qualquer erro de requisição, como:        
        print("\n----------------------------------")
        print("❌ Falha na conexão com a API.")
        print(f"Detalhes do Erro: {e}")
        print("Verifique sua conexão com a internet e a URL da API.")
        print("----------------------------------\n")
    except Exception as e:
        # Trata outros erros inesperados (como falha ao processar o JSON)
        print(f"Ocorreu um erro inesperado: {e}")

# Executa a função principal
buscar_usuario_aleatorio()