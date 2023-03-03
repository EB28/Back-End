class criaBola():

    def __init__(self, cor, conferencia, material):
        self.cor = cor
        self.conferencia = conferencia
        self.material = material

    def setCor(self, cor):
        self.cor = cor

    def setConferencia(self, conferencia):
        self.conferencia = conferencia

    def setMaterial(self, material):
        self.material = material


    def Pula(self):
        print('A bola está pulando')

    def Rodar(self):
        print('A bola está rodando')