print('COMPRE123')

senha = 123
login = 'Gui@'

my_login = input('Digite o login:')
my_senha = int(input('Digite sua senha:'))

if my_login == login and my_senha == senha:
    lista = ['Drone', 'Controle', 'Bateria', 'Carregador']
    meu_carrinho = []
    meu_total = []
    valores = [2500.00,500.00,250.00,200.00]
    print('Produtos')
    print(f''' Digite o ID do produto:
    0 - Drone
    1 - Controle
    2 - Bateria
    3 - Carregador
    ''')        

    escolha = input('Gostaria de fazer seu pedido? s/n: ')
    if escolha == 's':
        produto1 = int(input(">>"))
        produto2 = int(input(">>"))
        produto3 = int(input(">>"))
        meu_carrinho += (lista[produto1],lista[produto2],lista[produto3] )
        meu_total +=(valores[produto1],valores[produto2], valores[produto3])
        print('Carrinho:', meu_carrinho)
        print('Total')
        soma = sum(meu_total)
        print(f'R$ {soma:.2f}')
        print(f'''
    1 - PIX
    2 - Cartão de Credito
    3 - Cartão Débito                    

    ''')
        forma_pag =  input('Digite a forma de pagamento')
  
        if forma_pag:
            print('Pagamento efetuado com sucesso volte sempre!')  
    else:
        print('Pedido cancelado')
else:
    print('dados incorretos - Digite novamente')

