class ContaInvestimento:

    def __int__(self, numeroConta, nomeCorrentista, taxaJuros, saldoConta=0.0):
        self.numeroConta = numeroConta
        self.nomeCorrentista = alterarNome(nomeCorrentista)
        self.taxaJuros = taxaJuros
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

    def adicionaJuros(self):
        self.saldoConta += (self.saldoConta * (self.taxaJuros / 100.0))




conta = ContaInvestimento(1, 'Roberto', 10)
conta.deposito(2000)
print(f'R$ {conta.saldoConta:.2f}')
conta.adicionaJuros()
print(f'R$ {conta.saldoConta:.2f}')
conta.adicionaJuros()
print(f'R$ {conta.saldoConta:.2f}')
conta.adicionaJuros()
print(f'R$ {conta.saldoConta:.2f}')
conta.adicionaJuros()
print(f'R$ {conta.saldoConta:.2f}')
conta.adicionaJuros()
print(f'R$ {conta.saldoConta:.2f}')
