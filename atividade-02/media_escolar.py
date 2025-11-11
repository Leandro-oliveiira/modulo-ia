# Calculadora de Média Escolar

# Notas do aluno
nota1 = float(input("Digite a primeira nota"))
nota2 = float(input("Digite a segunda nota"))
nota3 = float(input("Digite a terceira nota"))

#Calculo da média
media = (nota1 + nota2 + nota3) / 3

# Exibição dos resultados
print(f"Notas do aluno")
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Nota 3: {nota3}")
print(f"A média final: {media: .2f}")

