#Este programa calcula o preço total de uma compra

#Solicita informações sobre o produto desejado
nome_produto = input("Digite o nome do Produto: ")
preco_unitario = float(input("Digite o valor unitário do Produto: "))
quantidade = int(input("Digite a quantidade de Produtos :"))

#Calcula o preço total de produtos
preco_total = preco_unitario * quantidade

#Exiba o resultado 
print(f"\nProduto: {nome_produto}")
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Total: R$ {preco_total: .2f}")