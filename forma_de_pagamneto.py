def forma_de_pagamento(valor):
    print('''
          1 - Débito 
          2 - Crédito 
          3 - Pix 
          4- Dinheiro
          ''')
    escolha1 = input('>>')
    if escolha1 == '1':
        print('Pagamento via Débito')
    elif escolha1 == '2':
        print('Pagamento via Crédito')
    elif escolha1 == '3':
        print('Pagamento via Pix')
    elif escolha1 == '4':
        print('Pagamento via Dinheiro')
    else:
        print('Forma de pagamento inválida')

#forma_de_pagamento()