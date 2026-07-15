class ResultadoDoTreinamento:

    def __init__(self):
        self.__modeloLogistico = None
        self.__listaDaFuncaoObjetivo = []
        self.__listaDaNormaDoGradiente = []
        self.__listaDaAcuracia = []
        self.__quantidadeDeIteracoes = 0
        self.__tempoComputacional = 0.0
        self.__acuracia = 0.0
        self.__motivoDaParada = ""

    def getModeloLogistico(self):
        return self.__modeloLogistico

    def setModeloLogistico(self, modeloLogistico):
        self.__modeloLogistico = modeloLogistico

    def getListaDaFuncaoObjetivo(self):
        return self.__listaDaFuncaoObjetivo

    def setListaDaFuncaoObjetivo(self, listaDaFuncaoObjetivo):
        self.__listaDaFuncaoObjetivo = listaDaFuncaoObjetivo

    def getListaDaNormaDoGradiente(self):
        return self.__listaDaNormaDoGradiente

    def setListaDaNormaDoGradiente(self, listaDaNormaDoGradiente):
        self.__listaDaNormaDoGradiente = listaDaNormaDoGradiente

    def getListaDaAcuracia(self):
        return self.__listaDaAcuracia

    def setListaDaAcuracia(self, listaDaAcuracia):
        self.__listaDaAcuracia = listaDaAcuracia

    def getQuantidadeDeIteracoes(self):
        return self.__quantidadeDeIteracoes

    def setQuantidadeDeIteracoes(self, quantidadeDeIteracoes):
        self.__quantidadeDeIteracoes = quantidadeDeIteracoes

    def getTempoComputacional(self):
        return self.__tempoComputacional

    def setTempoComputacional(self, tempoComputacional):
        self.__tempoComputacional = tempoComputacional

    def getAcuracia(self):
        return self.__acuracia

    def setAcuracia(self, acuracia):
        self.__acuracia = acuracia

    def getMotivoDaParada(self):
        return self.__motivoDaParada

    def setMotivoDaParada(self, motivoDaParada):
        self.__motivoDaParada = motivoDaParada