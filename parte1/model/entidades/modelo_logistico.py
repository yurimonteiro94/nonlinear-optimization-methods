class ModeloLogistico:

    def __init__(self, listaDePesos, vies):
        self.__listaDePesos = listaDePesos
        self.__vies = vies

    def getListaDePesos(self):
        return self.__listaDePesos

    def setListaDePesos(self, listaDePesos):
        self.__listaDePesos = listaDePesos

    def getVies(self):
        return self.__vies

    def setVies(self, vies):
        self.__vies = vies