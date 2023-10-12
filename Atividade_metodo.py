class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor} efetuado com sucesso. Novo saldo: R${self.saldo}')
        else:
            print('Valor de depósito inválido. O valor deve ser maior que zero.')

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f'Saque de R${valor} efetuado com sucesso. Novo saldo: R${self.saldo}')
            else:
                print('Saldo insuficiente. Saque não permitido.')
        else:
            print('Valor de saque inválido. O valor deve ser maior que zero.')

    def ver_saldo(self):
        print(f'Saldo atual da conta de {self.titular}: R${self.saldo}')

# Exemplo de uso:
conta = ContaBancaria("Adriana")  # Criar uma conta para o titular 
conta.depositar(1000)         # Depositar R$1000
conta.ver_saldo()             # Verificar o saldo
conta.sacar(500)              # Sacar R$500
conta.ver_saldo()             # Verificar o saldo após o saque
conta.sacar(800)              # Tentativa de sacar mais do que o saldo