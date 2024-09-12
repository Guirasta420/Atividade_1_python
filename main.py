from mostrar_valor import *
from forma_de_pagamneto import *

def escolher_produto():
    lista = ['Maça', 'Banana', 'Laranja', 'Uva']
    carrinho = []
    total = []
    valores = [5.00,5.00,3.00,2.50]
    print('''
        0: Maçã
        1: Banana
        2: Laranja
        3: Uva
    ''')
    escolha = input('Gostaria de fazer seu pedido? s/n: ')
    while escolha == 's':
        produto1 = int(input(">>"))
        produto2 = int(input(">>"))
        produto3 = int(input(">>"))
        carrinho += (lista[produto1],lista[produto2],lista[produto3] )
        total +=(valores[produto1],valores[produto2], valores[produto3])
        print('Carrinho:', carrinho)
        print('Total')
        soma = sum(total)
        print(f'R$ {soma:.2f}')
        forma_de_pagamento()
        print('Agradecemos seu pedido!!')
    else:
        print('Opção invalida')
  


escolher_produto()        
       









