def palindromo_simples(texto):
    
    # Limpa e Padroniza o Texto
    
    # Colocamos tudo em minúsculas (ex: 'ArArA' vira 'arara')
    texto_limpo = texto.lower()
    
    # Removemos todos os espaços (ex: 'a base' vira 'abase')
    texto_limpo = texto_limpo.replace(" ", "")
    
    
    # Inverte o Texto
    
    # [::-1] inverte a ordem dos caracteres
    texto_invertido = texto_limpo[::-1]
    
    
    # Comparação
    
    # Comparamos o texto limpo com o texto invertido
    if texto_limpo == texto_invertido:
        # Se forem iguais, é palíndromo
        return "Sim"
    else:
        # Se forem diferentes, não é palíndromo
        return "Não"

# --- Exemplo de Uso ---

# Teste 1: Palíndromo
frase_teste1 = "Anotaram a data da maratona"
resultado1 = palindromo_simples(frase_teste1)

# Teste 2: Não Palíndromo
frase_teste2 = "Este nao e um palindromo"
resultado2 = palindromo_simples(frase_teste2)


print("--- Testando ---")
print(f"A frase '{frase_teste1}' é palíndromo? -> {resultado1}")
print(f"A frase '{frase_teste2}' é palíndromo? -> {resultado2}")