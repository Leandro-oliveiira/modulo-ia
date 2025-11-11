def calcular_media_turma():
    # Lista para armazenar as notas de todos os alunos da turma.
    notas_da_turma = []
    
    # Variável de controle para o loop
    adicionar_mais_notas = 'S'
    
    print("--- Registro de Notas da Turma ---")
    print("Digite 'S' para continuar e 'N' para encerrar a entrada de dados.")
    
    # Loop para registrar as notas
    
    # O loop 'while' continua executando enquanto o usuário digitar 'S'
    while adicionar_mais_notas.upper() == 'S':
        try:
            # Pede o nome do aluno
            nome_aluno = input("\nNome do aluno (ou 'N' para encerrar): ")
            
            # Se o usuário digitar 'N' ou 'n', encerra o loop de entrada
            if nome_aluno.upper() == 'N':
                break
                
            # Pede a nota do aluno e converte para float
            nota = float(input(f"Digite a nota final de {nome_aluno}: "))
            
            # Adiciona a nota à lista de notas da turma
            notas_da_turma.append(nota)
            
            print(f"✅ Nota de {nome_aluno} registrada com sucesso.")

        except ValueError:
            # Trata o erro se o usuário digitar algo que não seja um número para a nota
            print("\n🚫 Erro: Por favor, digite um número válido para a nota.")
            # O loop continuará, pedindo a próxima entrada
    
    # Calcula a Média
    
    # Verifica se alguma nota foi inserida antes de tentar calcular
    total_alunos = len(notas_da_turma)
    
    if total_alunos > 0:
        # Soma todos os valores dentro da lista 'notas_da_turma'
        soma_das_notas = sum(notas_da_turma)
        
        # Calcula a média (Soma das Notas / Número de Alunos)
        media_turma = soma_das_notas / total_alunos
        
        # Exibi os resultados
        print("\n==================================")
        print("--- Resultado da Média da Turma ---")
        print(f"Total de alunos registrados: {total_alunos}")
        print(f"Soma total das notas: {round(soma_das_notas, 2)}")
        print(f"Média da Turma: **{round(media_turma, 2)}**")
        print("==================================")
    else:
        # Se a lista estiver vazia
        print("\n❌ Nenhuma nota foi registrada para calcular a média.")

# Inicia o programa
calcular_media_turma()