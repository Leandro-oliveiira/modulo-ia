import random
import string

def gerar_senha_segura():
    """
    Gera uma senha aleatória com letras, números e símbolos,
    onde o tamanho é definido pelo usuário.
    """
    print("--- Gerador de Senhas Seguras ---")
    
    # Solicita o tamanho da senha ao usuário
    while True:
        try:
            tamanho = int(input("Digite o tamanho desejado para a senha (ex: 12): "))            
            if tamanho < 4:
                print("O tamanho mínimo da senha deve ser 4 para garantir a inclusão de todos os tipos de caracteres.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    
    # Define os conjuntos de caracteres 
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation
    
    # Todos os caracteres possíveis para a senha
    todos_caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos
    
    # Garante que a senha contenha pelo menos 1 de cada tipo
    # Isso aumenta a segurança e garante que a senha atenda aos requisitos
    senha = []
    
    # Adiciona pelo menos um de cada tipo usando random.choice()
    senha.append(random.choice(letras_maiusculas))
    senha.append(random.choice(letras_minusculas))
    senha.append(random.choice(numeros))
    senha.append(random.choice(simbolos))
    
    # Preenche o restante da senha com caracteres aleatórios
    # O tamanho da senha já tem 4 caracteres, então preenchemos o restante
    for _ in range(tamanho - 4):
        senha.append(random.choice(todos_caracteres))
        
    # Mistura a lista de caracteres
    # garante que os 4 caracteres obrigatórios não estejam sempre no início
    random.shuffle(senha)
    
    # Converte a lista de caracteres em uma string
    senha_final = "".join(senha)
    
    # Exibe o resultado
    print("\n------------------------------------")
    print(f"✅ Senha Gerada: **{senha_final}**")
    print(f"Tamanho da Senha: {tamanho}")
    print("------------------------------------\n")

# Executa a função principal
gerar_senha_segura()