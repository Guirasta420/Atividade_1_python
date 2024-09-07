class ContaBancaria:
    def __init__(self, numero_conta, saldo=0.0):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.extrato = []

    def deposito(self, valor):
        if valor <= 0:
            print("O valor do depósito deve ser positivo.")
            return
        self.saldo += valor
        self.extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

    def saque(self, valor):
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
            return
        if valor > self.saldo:
            print("Saldo insuficiente para o saque.")
            return
        self.saldo -= valor
        self.extrato.append(f"Saque: R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def extrato_conta(self):
        print("\nExtrato da Conta")
        for transacao in self.extrato:
            print(transacao)
        print(f"Saldo atual: R$ {self.saldo:.2f}")

# Função para interagir com o usuário
def menu():
    conta = ContaBancaria(numero_conta="123456")
    
    while True:
        print("\nMenu:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1/2/3/4): ")
        
        if opcao == '1':
            valor = float(input("Digite o valor do depósito: R$ "))
            conta.deposito(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor do saque: R$ "))
            conta.saque(valor)
        elif opcao == '3':
            conta.extrato_conta()
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

