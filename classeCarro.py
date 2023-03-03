import unittest

class Carro():
    def __init__(self, consumoCombustivel):
        self.consumoCombustivel = consumoCombustivel
        self.consumoCombustivel = 0

    def andar(self, km):
        consumo = self.consumoCombustivel * km
        self.consumoCombustivel -= consumo

    def obterGasolina(self):
        return self.consumoCombustivel

    def adicionandoGasolina(self, consumoCombustivel):
        self.consumoCombustivel += consumoCombustivel

def main():
    carrinho = Carro(10)
    carrinho.adicionandoGasolina(100)
    carrinho.andar(3)
    print(carrinho.obterGasolina())

class TesteCarro(unittest.TestCase):

    def setUp(self):
        self.carro = Carro(10)

    def test_verifica_se_abasteceu_100(self):
        self.carro.adicionandoGasolina(100)
        abastece = 100
        self.assertEqual(abastece, self.carro.obterGasolina())

    def test_move_3_resta_70_de_gasolina(self):
        self.carro.adicionandoGasolina(100)
        move = 3
        self.carro.andar(3)
        self.assertEqual(70, self.carro.obterGasolina())

if __name__ == '__main__':
    main()
    unittest.main()