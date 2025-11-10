# Este programa calcula o volume de uma caixa retangular

# Solicita as dimensões da caixa ao usuário
comprimento = int(input("Digite o comprimento da caixa"))
largura = int(input("Digite o largura da caixa"))
altura = int(input("Digite o altura da caixa"))

# calcula o volume da caixa
volume = comprimento * largura * altura

# Exibe o resultado 
print(f"O volume da caixa é {volume} cm³")