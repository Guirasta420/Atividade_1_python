class ContaBancaria:
    def __init__(self, numero_conta, saldo=0.0):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.extrato = []
#SAQUE

def saque(saque, saldo ):
    saque = saldo - saque
    return saque 
#DEPOSITO

def deposito(deposito, saldo):
    deposito = deposito + saldo
    return deposito
#EXTRATO

def extrato(saldo):
    extrato = saldo
    return extrato
    
def banco():
        saldo = 15000
        print(f''' Escolha o ID da opção:
        0 - Fazer um saque
        1 - fazer um deposito
        2 - Ver Extrato
        3 - sair do sistema
        ''')
        escolha = input('>>')
        if escolha == '0': 
            valor_saque = float(input('Digite um valor de saque: '))
            saque1 = saque(valor_saque, saldo)          
            print(f'Valor Saque: R$', valor_saque, 'Valor restante na conta: R$', saque1)

        elif escolha == '1':
            valor_deposito = float(input('Digite um valor de deposito: '))
            deposito1 = deposito(valor_deposito, saldo)
            print(f'Valor Deposito: R$', valor_deposito, 'Valor adicionado a conta: R$', deposito1)

        elif escolha == '2':
            extrato1 = extrato(saldo)
            print (extrato1)
        else:
             print('Obrigado por fazer parte do Banco')
             
             


while True:
     banco()    


        
        
