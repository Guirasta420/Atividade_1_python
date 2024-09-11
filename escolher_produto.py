def escolher_produto():
    produtos = ('''
        1: Maçã
        2: Banana
        3: Laranja
        4: Uva
    ''')
    
    print("Escolha um produto:")
    escolha = int(input("Digite o número do produto desejado: "))
    
    if escolha in produtos:
        produto_escolhido = produtos[escolha]
        print(produto_escolhido)
    else:
        print("Produto inválido.")
        return escolher_produto()
