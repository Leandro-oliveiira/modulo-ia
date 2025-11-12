import json
import os

def manipular_arquivo_json(nome_arquivo):
    """
    Cria um dicionário, salva-o em um arquivo JSON e depois lê o arquivo
    para exibir os dados. Trata erros de escrita e leitura.
    """
    print(f"--- 💾 Manipulador de JSON para **{nome_arquivo}** ---")
    
    # Dados para salvar 
    dados_pessoas = {
        "pessoa1": {
            "nome": "Ana Silva",
            "idade": 28,
            "cidade": "São Paulo"
        },
        "pessoa2": {
            "nome": "Bruno Costa",
            "idade": 35,
            "cidade": "Rio de Janeiro"
        },
        "pessoa3": {
            "nome": "Carla Lima",
            "idade": 22,
            "cidade": "Belo Horizonte"
        }
    }
    
    # ----------------------------------
    # PARTE 1: ESCREVER / SALVAR O ARQUIVO JSON
    # ----------------------------------
    
    try:
        # 'with open(...)' garante que o arquivo seja fechado automaticamente
        # 'w' significa que o arquivo será aberto para escrita (write)
        with open(nome_arquivo, 'w', encoding='utf8') as arquivo:
            
            # O 'json.dump()' converte o dicionário Python para a string JSON
            # e escreve no arquivo.
            # indent=4 formata o JSON para que fique legível
            json.dump(dados_pessoas, arquivo, indent=4)
            
        print("\n✅ Sucesso ao Salvar: Os dados foram escritos no arquivo JSON.")

    except IOError as e:
        # Captura erros de Input/Output, como permissão negada
        print("\n-------------------------------------------")
        print("❌ Falha ao Salvar o Arquivo.")
        print(f"Ocorreu um erro ao escrever no arquivo: {e}")
        print("Verifique as permissões da pasta.")
        print("-------------------------------------------\n")
        return
    except Exception as e:
        print(f"\n❌ Ocorreu um erro inesperado ao salvar: {e}")
        return

    # ----------------------------------
    # PARTE 2: LER O ARQUIVO JSON
    # ----------------------------------
    
    print("\n--- 📖 Lendo os Dados Salvos ---")
    
    try:
        # 'r' significa que o arquivo será aberto para leitura (read)
        with open(nome_arquivo, 'r', encoding='utf8') as arquivo:
            
            # O 'json.load()' lê o conteúdo do arquivo JSON e o converte
            # de volta para um dicionário Python.
            dados_lidos = json.load(arquivo)
            
        print("\n✅ Sucesso ao Ler: Dados recuperados do arquivo JSON.")
        print("-------------------------------------------------")
        
        # Exibe os dados lidos
        for chave, pessoa in dados_lidos.items():
            print(f"ID: {chave.upper()}")
            print(f"  Nome: {pessoa['nome']}")
            print(f"  Idade: {pessoa['idade']} anos")
            print(f"  Cidade: {pessoa['cidade']}")
            print("-" * 35)

    except FileNotFoundError:
        # Este erro é improvável de ocorrer aqui se a parte 1 funcionou,
        # mas é importante para um programa robusto.
        print("\n-------------------------------------------")
        print(f"❌ Erro de Leitura: O arquivo **'{nome_arquivo}'** não foi encontrado.")
        print("-------------------------------------------\n")
    except json.JSONDecodeError:
        # Caso o arquivo exista, mas esteja corrompido ou mal formatado
        print("\n❌ Erro de Decodificação: O arquivo JSON está ilegível ou inválido.")
    except Exception as e:
        print(f"\n❌ Ocorreu um erro inesperado ao ler: {e}")


# Define o nome do arquivo que será criado
NOME_ARQUIVO = 'pessoas.json'

# Executa a função principal
manipular_arquivo_json(NOME_ARQUIVO)