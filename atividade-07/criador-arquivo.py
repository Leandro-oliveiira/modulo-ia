import os

def coletar_dados_pessoas():
    """
    Coleta nome, idade e cidade de várias pessoas e retorna uma lista de dicionários.
    """
    dados = []
    print("--- 📝 Coleta de Dados Pessoais ---")
    print("Digite 'sair' a qualquer momento no campo 'Nome' para parar a coleta.")
    
    while True:
        # Coleta o Nome
        nome = input("\nNome: ").strip()
        if nome.lower() == 'sair':
            break
        if not nome:
            print("Nome não pode ser vazio. Por favor, tente novamente.")
            continue
            
        # Coleta a Idade
        while True:
            try:
                idade_str = input("Idade: ").strip()
                if not idade_str:
                    print("Idade não pode ser vazia.")
                    continue
                idade = int(idade_str)
                if idade <= 0:
                    print("Idade deve ser um número positivo.")
                else:
                    break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro para a idade.")

        # Coleta a Cidade
        cidade = input("Cidade: ").strip()
        if not cidade:
            cidade = "Não Informada"
            
        # Adiciona os dados coletados à lista principal
        dados.append({"Nome": nome, "Idade": idade, "Cidade": cidade})
        
    return dados

def salvar_dados_em_arquivo(dados):
    """
    Recebe os dados e os salva em um arquivo de texto no formato tabular,
    tratando erros de escrita.
    """
    if not dados:
        print("\n🚫 Nenhum dado coletado para salvar.")
        return
        
    # Solicita o nome do arquivo ao usuário
    nome_arquivo = input("\nDigite o nome do arquivo para salvar (ex: Pessoas.txt): ").strip()
    if not nome_arquivo:
        nome_arquivo = "dados_salvos.txt" # Nome padrão se o usuário deixar vazio
        
    # Prepara o conteúdo tabular
    
    # Define os cabeçalhos das colunas
    cabecalho = ["Nome", "Idade", "Cidade"]
    
    # Define a largura das colunas para alinhamento (ajuste conforme necessário)
    # Por exemplo: Nome ocupa 20 espaços, Idade 5, Cidade 15
    largura_nome = 20
    largura_idade = 5
    largura_cidade = 15
    
    # Cria a linha do cabeçalho
    linha_cabecalho = f"{cabecalho[0]:<{largura_nome}} {cabecalho[1]:^{largura_idade}} {cabecalho[2]:<{largura_cidade}}\n"
    linha_separadora = "-" * (largura_nome + largura_idade + largura_cidade + 2) + "\n" # +2 para os espaços
    
    conteudo = linha_cabecalho + linha_separadora
    
    # Adiciona cada linha de dados ao conteúdo
    for pessoa in dados:
        linha = (
            f"{pessoa['Nome']:<{largura_nome}} "    # Alinha Nome à esquerda
            f"{pessoa['Idade']:^{largura_idade}} "  # Centraliza Idade
            f"{pessoa['Cidade']:<{largura_cidade}}\n" # Alinha Cidade à esquerda
        )
        conteudo += linha
        
    # Bloco try-except para salvar o arquivo e tratar erros
    try:
        # 'with open(...)' garante que o arquivo seja fechado automaticamente
        # 'w' significa que o arquivo será aberto para escrita (write)
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)
            
        print("\n-------------------------------------------")
        print(f"✅ Sucesso! Dados salvos em: **{nome_arquivo}**")
        print("-------------------------------------------\n")

    except IOError as e:
        # Captura erros de Input/Output, como permissão negada ou nome de arquivo inválido
        print("\n-------------------------------------------")
        print("❌ Falha ao Salvar o Arquivo.")
        print(f"Ocorreu um erro de I/O: {e}")
        print("Verifique as permissões da pasta ou se o nome do arquivo é válido.")
        print("-------------------------------------------\n")
    except Exception as e:
        # Trata outros erros inesperados
        print(f"\n❌ Ocorreu um erro inesperado: {e}")

# --- Execução do Programa ---

# Coleta os dados das pessoas
dados_para_salvar = coletar_dados_pessoas()

# Salva os dados coletados no arquivo
salvar_dados_em_arquivo(dados_para_salvar)