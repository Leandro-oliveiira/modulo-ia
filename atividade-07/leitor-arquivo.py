import os

def ler_arquivo_texto():
    """
    Solicita o nome do arquivo ao usuário, lê e exibe seu conteúdo linha por linha,
    e trata o erro de arquivo não encontrado.
    """
    print("--- 📚 Leitor de Arquivos de Texto ---")
    
    # Solicita o nome do arquivo ao usuário
    nome_arquivo = input("Digite o nome do arquivo de texto (ex: exemplo.txt): ").strip()
    
    # Bloco try-except para abrir o arquivo e tratar erros
    try:
        print(f"\n🔎 Conteúdo do arquivo **{nome_arquivo}**:")
        print("-----------------------------------")
        
        # O 'with open(...)' abre o arquivo e garante que ele será fechado
        # 'r' significa que o arquivo será aberto para leitura (read)
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            
            # Percorre e exibe cada linha
            # O laço 'for linha in arquivo:' percorre o arquivo linha por linha
            for numero_linha, linha in enumerate(arquivo, 1):
                # O .strip() remove espaços em branco e quebras de linha invisíveis
                print(f"Linha {numero_linha}: {linha.strip()}")
                
        print("-----------------------------------")
        print("✅ Leitura do arquivo concluída com sucesso!")
        
    except FileNotFoundError:
        # Trata o Erro mais Comum: Arquivo Não Encontrado
        print("\n-------------------------------------------")
        print(f"❌ Erro de Leitura: O arquivo **'{nome_arquivo}'** não foi encontrado.")
        print("Verifique se o arquivo está na mesma pasta que este programa e se o nome está correto.")
        print("-------------------------------------------\n")
        
    except Exception as e:
        # Trata outros erros inesperados (como problemas de permissão)
        print(f"\n❌ Ocorreu um erro inesperado: {e}")

# Executa a função principal
ler_arquivo_texto()