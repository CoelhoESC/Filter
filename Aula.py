"""
filter - semelhante ao map, mas ele filtra os itens e os retorna
"""
from dados import pessoas, lista, produtos

novo_produto = filter(lambda x: x > 5, lista) # Retorna produtos com preço maior que 5
print(list(novo_produto))
print()

# Usando filter com dict
novo_produto = filter(lambda p: p['preco'] < 10, produtos)
for dicio in novo_produto:
    print(f"nome:{dicio['Nome']}, preço: {dicio['preco']}")
print()


def filtrar(pessoa):
    if pessoa['idade'] < 18:
        return True


menor_18 = filter(filtrar, pessoas)
for pessoas in menor_18:
    print(f"Nome:{pessoas['nome']}, idade: {pessoas['idade']}")
