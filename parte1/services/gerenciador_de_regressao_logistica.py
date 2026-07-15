import math

from services.constantes import Constantes


class GerenciadorDeRegressaoLogistica:

    @staticmethod
    def retornarSigmoide(valor):
        if(valor >= Constantes.QUANTIDADE_NULA):
            exponencial = math.exp(-valor)
            return 1.0 / (1.0 + exponencial)

        exponencial = math.exp(valor)

        return exponencial / (1.0 + exponencial)

    @staticmethod
    def retornarProbabilidade(modeloLogistico, listaDeCaracteristicas):
        if(modeloLogistico is None):
            return None

        elif(listaDeCaracteristicas is None):
            return None

        listaDePesos = modeloLogistico.getListaDePesos()

        if(listaDePesos is None):
            return None

        elif(len(listaDePesos) != len(listaDeCaracteristicas)):
            return None

        soma = modeloLogistico.getVies()
        indice = Constantes.INDICE_INICIAL
        quantidadeDeCaracteristicas = len(listaDeCaracteristicas)

        while(indice < quantidadeDeCaracteristicas):
            soma = soma + listaDePesos[indice] * listaDeCaracteristicas[indice]
            indice = indice + Constantes.INCREMENTO_UNITARIO

        return GerenciadorDeRegressaoLogistica.retornarSigmoide(soma)

    @staticmethod
    def retornarClasse(modeloLogistico, listaDeCaracteristicas):
        probabilidade = GerenciadorDeRegressaoLogistica.retornarProbabilidade(modeloLogistico, listaDeCaracteristicas)

        if(probabilidade is None):
            return None

        if(probabilidade >= Constantes.LIMIAR_DE_CLASSIFICACAO):
            return Constantes.OCUPACAO_PRESENTE

        return Constantes.OCUPACAO_VAZIA

    @staticmethod
    def retornarFuncaoObjetivo(modeloLogistico, listaDeEntradasNormalizadas, listaDeSaidasEsperadas):
        if(modeloLogistico is None):
            return None

        elif(listaDeEntradasNormalizadas is None):
            return None

        elif(listaDeSaidasEsperadas is None):
            return None

        elif(len(listaDeEntradasNormalizadas) == Constantes.QUANTIDADE_NULA):
            return None

        elif(len(listaDeEntradasNormalizadas) != len(listaDeSaidasEsperadas)):
            return None

        soma = 0.0
        indice = Constantes.INDICE_INICIAL
        quantidadeDeAmostras = len(listaDeEntradasNormalizadas)

        while(indice < quantidadeDeAmostras):
            probabilidade = GerenciadorDeRegressaoLogistica.retornarProbabilidade(modeloLogistico, listaDeEntradasNormalizadas[indice])

            if(probabilidade is None):
                return None

            if(probabilidade < Constantes.MENOR_PROBABILIDADE_PERMITIDA):
                probabilidade = Constantes.MENOR_PROBABILIDADE_PERMITIDA

            elif(probabilidade > Constantes.MAIOR_PROBABILIDADE_PERMITIDA):
                probabilidade = Constantes.MAIOR_PROBABILIDADE_PERMITIDA

            saidaEsperada = listaDeSaidasEsperadas[indice]

            soma = soma - saidaEsperada * math.log(probabilidade)
            soma = soma - (Constantes.OCUPACAO_PRESENTE - saidaEsperada) * math.log(Constantes.OCUPACAO_PRESENTE - probabilidade)

            indice = indice + Constantes.INCREMENTO_UNITARIO

        return soma / quantidadeDeAmostras

    @staticmethod
    def retornarGradienteDosPesos(modeloLogistico, listaDeEntradasNormalizadas, listaDeSaidasEsperadas):
        if(modeloLogistico is None):
            return None

        elif(listaDeEntradasNormalizadas is None):
            return None

        elif(listaDeSaidasEsperadas is None):
            return None

        elif(len(listaDeEntradasNormalizadas) == Constantes.QUANTIDADE_NULA):
            return None

        elif(len(listaDeEntradasNormalizadas) != len(listaDeSaidasEsperadas)):
            return None

        listaDePesos = modeloLogistico.getListaDePesos()

        if(listaDePesos is None):
            return None

        quantidadeDePesos = len(listaDePesos)
        listaDoGradiente = []
        indiceDoPeso = Constantes.INDICE_INICIAL

        while(indiceDoPeso < quantidadeDePesos):
            listaDoGradiente.append(0.0)
            indiceDoPeso = indiceDoPeso + Constantes.INCREMENTO_UNITARIO

        quantidadeDeAmostras = len(listaDeEntradasNormalizadas)
        indiceDaAmostra = Constantes.INDICE_INICIAL

        while(indiceDaAmostra < quantidadeDeAmostras):
            listaDeCaracteristicas = listaDeEntradasNormalizadas[indiceDaAmostra]

            if(listaDeCaracteristicas is None):
                return None

            elif(len(listaDeCaracteristicas) != quantidadeDePesos):
                return None

            probabilidade = GerenciadorDeRegressaoLogistica.retornarProbabilidade(modeloLogistico, listaDeCaracteristicas)

            if(probabilidade is None):
                return None

            erro = probabilidade - listaDeSaidasEsperadas[indiceDaAmostra]
            indiceDoPeso = Constantes.INDICE_INICIAL

            while(indiceDoPeso < quantidadeDePesos):
                listaDoGradiente[indiceDoPeso] = listaDoGradiente[indiceDoPeso] + erro * listaDeCaracteristicas[indiceDoPeso]
                indiceDoPeso = indiceDoPeso + Constantes.INCREMENTO_UNITARIO

            indiceDaAmostra = indiceDaAmostra + Constantes.INCREMENTO_UNITARIO

        indiceDoPeso = Constantes.INDICE_INICIAL

        while(indiceDoPeso < quantidadeDePesos):
            listaDoGradiente[indiceDoPeso] = listaDoGradiente[indiceDoPeso] / quantidadeDeAmostras
            indiceDoPeso = indiceDoPeso + Constantes.INCREMENTO_UNITARIO

        return listaDoGradiente

    @staticmethod
    def retornarGradienteDoVies(modeloLogistico, listaDeEntradasNormalizadas, listaDeSaidasEsperadas):
        if(modeloLogistico is None):
            return None

        elif(listaDeEntradasNormalizadas is None):
            return None

        elif(listaDeSaidasEsperadas is None):
            return None

        elif(len(listaDeEntradasNormalizadas) == Constantes.QUANTIDADE_NULA):
            return None

        elif(len(listaDeEntradasNormalizadas) != len(listaDeSaidasEsperadas)):
            return None

        soma = 0.0
        quantidadeDeAmostras = len(listaDeEntradasNormalizadas)
        indiceDaAmostra = Constantes.INDICE_INICIAL

        while(indiceDaAmostra < quantidadeDeAmostras):
            probabilidade = GerenciadorDeRegressaoLogistica.retornarProbabilidade(modeloLogistico, listaDeEntradasNormalizadas[indiceDaAmostra])

            if(probabilidade is None):
                return None

            soma = soma + probabilidade - listaDeSaidasEsperadas[indiceDaAmostra]
            indiceDaAmostra = indiceDaAmostra + Constantes.INCREMENTO_UNITARIO

        return soma / quantidadeDeAmostras

    @staticmethod
    def retornarNormaDoGradiente(listaDoGradienteDosPesos, gradienteDoVies):
        if(listaDoGradienteDosPesos is None):
            return None

        elif(gradienteDoVies is None):
            return None

        somaDosQuadrados = gradienteDoVies * gradienteDoVies
        indiceDoPeso = Constantes.INDICE_INICIAL
        quantidadeDePesos = len(listaDoGradienteDosPesos)

        while(indiceDoPeso < quantidadeDePesos):
            somaDosQuadrados = somaDosQuadrados + listaDoGradienteDosPesos[indiceDoPeso] * listaDoGradienteDosPesos[indiceDoPeso]
            indiceDoPeso = indiceDoPeso + Constantes.INCREMENTO_UNITARIO

        return math.sqrt(somaDosQuadrados)

    @staticmethod
    def retornarAcuracia(modeloLogistico, listaDeEntradasNormalizadas, listaDeSaidasEsperadas):
        if(modeloLogistico is None):
            return None

        elif(listaDeEntradasNormalizadas is None):
            return None

        elif(listaDeSaidasEsperadas is None):
            return None

        elif(len(listaDeEntradasNormalizadas) == Constantes.QUANTIDADE_NULA):
            return None

        elif(len(listaDeEntradasNormalizadas) != len(listaDeSaidasEsperadas)):
            return None

        quantidadeDeAcertos = Constantes.QUANTIDADE_NULA
        quantidadeDeAmostras = len(listaDeEntradasNormalizadas)
        indiceDaAmostra = Constantes.INDICE_INICIAL

        while(indiceDaAmostra < quantidadeDeAmostras):
            classePrevista = GerenciadorDeRegressaoLogistica.retornarClasse(modeloLogistico, listaDeEntradasNormalizadas[indiceDaAmostra])

            if(classePrevista is None):
                return None

            if(classePrevista == listaDeSaidasEsperadas[indiceDaAmostra]):
                quantidadeDeAcertos = quantidadeDeAcertos + Constantes.INCREMENTO_UNITARIO

            indiceDaAmostra = indiceDaAmostra + Constantes.INCREMENTO_UNITARIO

        return quantidadeDeAcertos / quantidadeDeAmostras