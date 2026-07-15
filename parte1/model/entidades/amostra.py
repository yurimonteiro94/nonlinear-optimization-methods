from datetime import datetime


class Amostra:

    def __init__(self, identificador, data, temperatura, umidade, luminosidade, co2, razaoDeUmidade, ocupacao):
        self.__identificador = None
        self.__data = None
        self.__temperatura = None
        self.__umidade = None
        self.__luminosidade = None
        self.__co2 = None
        self.__razaoDeUmidade = None
        self.__ocupacao = None

        self.setIdentificador(identificador)
        self.setData(data)
        self.setTemperatura(temperatura)
        self.setUmidade(umidade)
        self.setLuminosidade(luminosidade)
        self.setCo2(co2)
        self.setRazaoDeUmidade(razaoDeUmidade)
        self.setOcupacao(ocupacao)

    def getIdentificador(self):
        return self.__identificador

    def setIdentificador(self, identificador):
        self.__identificador = identificador

    def getData(self):
        return self.__data

    def setData(self, data):
        self.__data = data

    def getTemperatura(self):
        return self.__temperatura

    def setTemperatura(self, temperatura):
        self.__temperatura = temperatura

    def getUmidade(self):
        return self.__umidade

    def setUmidade(self, umidade):
        self.__umidade = umidade

    def getLuminosidade(self):
        return self.__luminosidade

    def setLuminosidade(self, luminosidade):
        self.__luminosidade = luminosidade

    def getCo2(self):
        return self.__co2

    def setCo2(self, co2):
        self.__co2 = co2

    def getRazaoDeUmidade(self):
        return self.__razaoDeUmidade

    def setRazaoDeUmidade(self, razaoDeUmidade):
        self.__razaoDeUmidade = razaoDeUmidade

    def getOcupacao(self):
        return self.__ocupacao

    def setOcupacao(self, ocupacao):
        self.__ocupacao = ocupacao