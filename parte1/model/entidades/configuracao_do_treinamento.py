class ConfiguracaoDoTreinamento:

    def __init__(self, learningRate, tolerancia, numeroMaximoDeIteracoes, tamanhoDoMiniBatch, beta, embaralharAmostras):
        self.__learningRate = learningRate
        self.__tolerancia = tolerancia
        self.__numeroMaximoDeIteracoes = numeroMaximoDeIteracoes
        self.__tamanhoDoMiniBatch = tamanhoDoMiniBatch
        self.__beta = beta
        self.__embaralharAmostras = embaralharAmostras

    def getLearningRate(self):
        return self.__learningRate

    def setLearningRate(self, learningRate):
        self.__learningRate = learningRate

    def getTolerancia(self):
        return self.__tolerancia

    def setTolerancia(self, tolerancia):
        self.__tolerancia = tolerancia

    def getNumeroMaximoDeIteracoes(self):
        return self.__numeroMaximoDeIteracoes

    def setNumeroMaximoDeIteracoes(self, numeroMaximoDeIteracoes):
        self.__numeroMaximoDeIteracoes = numeroMaximoDeIteracoes

    def getTamanhoDoMiniBatch(self):
        return self.__tamanhoDoMiniBatch

    def setTamanhoDoMiniBatch(self, tamanhoDoMiniBatch):
        self.__tamanhoDoMiniBatch = tamanhoDoMiniBatch

    def getBeta(self):
        return self.__beta

    def setBeta(self, beta):
        self.__beta = beta

    def getEmbaralharAmostras(self):
        return self.__embaralharAmostras

    def setEmbaralharAmostras(self, embaralharAmostras):
        self.__embaralharAmostras = embaralharAmostras