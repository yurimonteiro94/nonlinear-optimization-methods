class ResultadoOtimizacao:

    def __init__(self):
        self.__pontoFinal = None
        self.__listaDePontos = []
        self.__listaDaFuncaoObjetivo = []
        self.__listaDaNormaDoGradiente = []
        self.__quantidadeDeIteracoes = 0
        self.__tempoComputacional = 0.0
        self.__motivoDaParada = ""

    def getPontoFinal(self):
        return self.__pontoFinal

    def setPontoFinal(self, pontoFinal):
        self.__pontoFinal = pontoFinal

    def getListaDePontos(self):
        return self.__listaDePontos

    def setListaDePontos(self, listaDePontos):
        self.__listaDePontos = listaDePontos

    def getListaDaFuncaoObjetivo(self):
        return self.__listaDaFuncaoObjetivo

    def setListaDaFuncaoObjetivo(self, listaDaFuncaoObjetivo):
        self.__listaDaFuncaoObjetivo = listaDaFuncaoObjetivo

    def getListaDaNormaDoGradiente(self):
        return self.__listaDaNormaDoGradiente

    def setListaDaNormaDoGradiente(self, listaDaNormaDoGradiente):
        self.__listaDaNormaDoGradiente = listaDaNormaDoGradiente

    def getQuantidadeDeIteracoes(self):
        return self.__quantidadeDeIteracoes

    def setQuantidadeDeIteracoes(self, quantidadeDeIteracoes):
        self.__quantidadeDeIteracoes = quantidadeDeIteracoes

    def getTempoComputacional(self):
        return self.__tempoComputacional

    def setTempoComputacional(self, tempoComputacional):
        self.__tempoComputacional = tempoComputacional

    def getMotivoDaParada(self):
        return self.__motivoDaParada

    def setMotivoDaParada(self, motivoDaParada):
        self.__motivoDaParada = motivoDaParada