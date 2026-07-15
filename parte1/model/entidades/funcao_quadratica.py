class FuncaoQuadratica:

    def __init__(self, matrizA, vetorB, constanteC):
        self.__matrizA = matrizA
        self.__vetorB = vetorB
        self.__constanteC = constanteC

    def getMatrizA(self):
        return self.__matrizA

    def setMatrizA(self, matrizA):
        self.__matrizA = matrizA

    def getVetorB(self):
        return self.__vetorB

    def setVetorB(self, vetorB):
        self.__vetorB = vetorB

    def getConstanteC(self):
        return self.__constanteC

    def setConstanteC(self, constanteC):
        self.__constanteC = constanteC