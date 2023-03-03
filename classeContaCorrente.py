class ContaCorrente():

    def __init__(self, numeroConta, nomeCorrentista, saldoConta=0):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldoConta = saldoConta



    def alterarNome(self, novo_nome):
        self.nome = novo_nome
        return self.nome

    def deposito(self, valor_deposito):
        self.saldoConta += valor_deposito
        return self.saldoConta

    def saque(self, valor_saque):
        self.saldoConta -= valor_saque
        return self.saldoConta

CC1 = ContaCorrente(1, 'Joaquim da Silva', 300)

print(CC1.__dict__)

CC1.deposito(25)
print(CC1.__dict__)

CC1.saque(100)
print(CC1.__dict__)