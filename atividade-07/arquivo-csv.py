import pandas as pd
import os

def analisar_desempenho_csv(nome_arquivo):
    """
    Lê um arquivo CSV, calcula e exibe a média e o desvio padrão da 
    coluna 'tempo_execucao', e trata erros.
    """
    print(f"--- 📈 Analisando o arquivo: {nome_arquivo} ---")
    
    try:
        # Tenta ler o arquivo CSV
        # O 'pd.read_csv()' lê o arquivo e o transforma em um DataFrame
        df = pd.read_csv(nome_arquivo)
        
        # Verifica se a coluna 'tempo_execucao' existe
        COLUNA_ALVO = 'tempo_execucao'
        if COLUNA_ALVO not in df.columns:
            print("\n-------------------------------------------")
            print(f"❌ Falha na Análise: A coluna **'{COLUNA_ALVO}'** não foi encontrada no arquivo.")
            print(f"Colunas disponíveis: {list(df.columns)}")
            print("-------------------------------------------\n")
            return
            
        # Garante que os dados da coluna são numéricos 
        # O .loc[] seleciona todas as linhas e apenas a coluna alvo
        df.loc[:, COLUNA_ALVO] = pd.to_numeric(df[COLUNA_ALVO], errors='coerce')
        
        # Remove linhas com valores não numéricos (NaN) que foram criados na conversão
        df_limpo = df.dropna(subset=[COLUNA_ALVO])
        
        # Calcula a Média e o Desvio Padrão
        # O .mean() calcula a média e o .std() calcula o desvio padrão da coluna
        media = df_limpo[COLUNA_ALVO].mean()
        desvio_padrao = df_limpo[COLUNA_ALVO].std()
        
        # Exibe os resultados
        print("\n-------------------------------------------")
        print("✅ Análise de Desempenho Concluída!")
        print(f"Coluna Analisada: **{COLUNA_ALVO}**")
        print(f"Média do Tempo de Execução: **{media:.2f} segundos**")
        print(f"Desvio Padrão: **{desvio_padrao:.2f} segundos**")
        print("\nO Desvio Padrão indica o quanto os tempos variam em torno da média.")
        print("-------------------------------------------\n")
        
    # Trata o Erro mais Comum: Arquivo Não Encontrado
    except FileNotFoundError:
        print("\n-------------------------------------------")
        print(f"❌ Erro de Leitura: O arquivo **'{nome_arquivo}'** não foi encontrado.")
        print("Certifique-se de que o arquivo está na mesma pasta que este programa Python.")
        print("-------------------------------------------\n")
        
    # Trata Outros Erros de Leitura (como problemas de codificação)
    except pd.errors.EmptyDataError:
        print("\n❌ Erro de Leitura: O arquivo CSV está vazio ou ilegível.")
    except Exception as e:
        print(f"\n❌ Ocorreu um erro inesperado: {e}")

# Define o nome do arquivo que queremos ler
NOME_ARQUIVO = 'dados_execucao.csv'

# Executa a função principal
analisar_desempenho_csv(NOME_ARQUIVO)