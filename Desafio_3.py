print('SEJA BEM VINDA(O) AO BANCO DO GUI')

print('FAÇA SEU LOGIN')

acesso_conta = 445500
acesso_senha = 251901
extrato = [3000]

for n in range(1,4):
    login_user = int(input('Digite sua conta: '))
    login_senha = int(input('Digite sua senha: '))
    if login_user == acesso_conta and login_senha == acesso_senha:
        print('Acesso confirmado')
        print(f''' Escolha o ID da opção:
      0 - Ver extrato
      1 - Fazer um deposito
      2 - fazer um saque
      3 - sair do sistema
      ''')
    lista = ['0 Ver extrato','1 Fazer um deposito', '2 Fazer um saque', '3 sair do sistema']
   
   # Deposito
    if lista == '1':
        deposito = float(input('Qual o valor que gostia de depositar? R$'))
        extrato.append(deposito)
        soma = sum(extrato)
        print('Deposito realizado com sucesso! valor total da conta:', soma)
   
   # Saque 
        
    elif lista == '2':
        saque = float(input('Qual o valor do saque? R$')) 
        if saque > extrato [0]:
            print('SEM SALDO')
            break
        subtracao = extrato[0] 
        resultado = subtracao - saque
        print('valor da conta atual R$', resultado)  
   
   # Saida
    elif lista == '3':
        sair = float(input('Obrigado por ter acessado ao Bando do Gui!!'))  
    
    # Extrato
    elif lista == '0':
        print(extrato)
        
else:
    print('Acesso negado') 
    if n == 3:
       print('Conta bloqueada')
     
      
n = input('digite enter para sair')

        

      

