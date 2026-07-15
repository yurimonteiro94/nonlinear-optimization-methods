import random
import time

from model.entidades.resultado_do_treinamento import ResultadoDoTreinamento
from services.constantes import Constantes
from services.gerenciador_de_regressao_logistica import GerenciadorDeRegressaoLogistica


class GerenciadorSGD:

    @staticmethod
    def retornarListaDeIndicesEmbaralhados(quantidadeDeAmostras, numeroDaEpoca):
        if(quantidadeDeAmostras <= Constantes.QUANTIDADE_NULA):
            return None

        listaDeIndices = []
        indiceDaAmostra = Constantes.INDICE_INICIAL

        while(indiceDaAmostra < quantidadeDeAmostras):
            listaDeIndices.append(indiceDaAmostra)
            indiceDaAmostra = indiceDaAmostra + Constantes.INCREMENTO_UNITARIO

        geradorAleatorio = random.Random(Constantes.SEMENTE_ALEATORIA + numeroDaEpoca)
        geradorAleatorio.shuffle(listaDeIndices)

        return listaDeIndices

    @staticmethod
    def retornarMiniBatch(listaDeEntradas, listaDeSaidas, listaDeIndices, indiceInicial, indiceFinal):
        if(listaDeEntradas is None):
            return None

        elif(listaDeSaidas is None):
            return None

        elif(listaDeIndices is None):
            return None

        listaDeEntradasDoMiniBatch = []
        listaDeSaidasDoMiniBatch = []
        indice = indiceInicial

        while(indice < indiceFinal):
            indiceDaAmostra = listaDeIndices[indice]

            listaDeEntradasDoMiniBatch.append(listaDeEntradas[indiceDaAmostra])
            listaDeSaidasDoMiniBatch.append(listaDeSaidas[indiceDaAmostra])

            indice = indice + Constantes.INCREMENTO_UNITARIO

        return [listaDeEntradasDoMiniBatch, listaDeSaidasDoMiniBatch]

    @staticmethod
    def atualizarModelo(modeloLogistico, listaDeEntradasDoMiniBatch, listaDeSaidasDoMiniBatch, learningRate):
        listaDoGradienteDosPesos = GerenciadorDeRegressaoLogistica.retornarGradienteDosPesos(modeloLogistico, listaDeEntradasDoMiniBatch, listaDeSaidasDoMiniBatch)
        gradienteDoVies = GerenciadorDeRegressaoLogistica.retornarGradienteDoVies(modeloLogistico, listaDeEntradasDoMiniBatch, listaDeSaidasDoMiniBatch)

        if(listaDoGradienteDosPesos is None):
            return False

        elif(gradienteDoVies is None):
            return False

        listaDePesos = modeloLogistico.getListaDePesos()
        novaListaDePesos = []
        indiceDoPeso = Constantes.INDICE_INICIAL
        quantidadeDePesos = len(listaDePesos)

        while(indiceDoPeso < quantidadeDePesos):
            novoPeso = listaDePesos[indiceDoPeso] - learningRate * listaDoGradienteDosPesos[indiceDoPeso]
            novaListaDePesos.append(novoPeso)

            indiceDoPeso = indiceDoPeso + Constantes.INCREMENTO_UNITARIO

        novoVies = modeloLogistico.getVies() - learningRate * gradienteDoVies

        modeloLogistico.setListaDePesos(novaListaDePesos)
        modeloLogistico.setVies(novoVies)

        return True

    @staticmethod
    def executar(modeloLogistico, listaDeEntradasNormalizadas, listaDeSaidasEsperadas, configuracaoDoTreinamento):
        if(modeloLogistico is None):
            return None

        elif(listaDeEntradasNormalizadas is None):
            return None

        elif(listaDeSaidasEsperadas is None):
            return None

        elif(configuracaoDoTreinamento is None):
            return None

        elif(len(listaDeEntradasNormalizadas) == Constantes.QUANTIDADE_NULA):
            return None

        elif(len(listaDeEntradasNormalizadas) != len(listaDeSaidasEsperadas)):
            return None

        learningRate = configuracaoDoTreinamento.getLearningRate()
        tolerancia = configuracaoDoTreinamento.getTolerancia()
        numeroMaximoDeIteracoes = configuracaoDoTreinamento.getNumeroMaximoDeIteracoes()
        tamanhoDoMiniBatch = configuracaoDoTreinamento.getTamanhoDoMiniBatch()
        embaralharAmostras = configuracaoDoTreinamento.getEmbaralharAmostras()

        if(learningRate <= Constantes.QUANTIDADE_NULA):
            return None

        elif(tolerancia < Constantes.QUANTIDADE_NULA):
            return None

        elif(numeroMaximoDeIteracoes <= Constantes.QUANTIDADE_NULA):
            return None

        elif(tamanhoDoMiniBatch <= Constantes.QUANTIDADE_NULA):
            return None

        quantidadeDeAmostras = len(listaDeEntradasNormalizadas)
        listaDaFuncaoObjetivo = []
        listaDaNormaDoGradiente = []
        listaDaAcuracia = []
        quantidadeDeIteracoes = Constantes.QUANTIDADE_NULA
        motivoDaParada = Constantes.MOTIVO_DA_PARADA_POR_NUMERO_MAXIMO_DE_ITERACOES
        funcaoObjetivoAnterior = None
        tempoInicial = time.perf_counter()

        while(quantidadeDeIteracoes < numeroMaximoDeIteracoes):
            if(embaralharAmostras):
                listaDeIndices = GerenciadorSGD.retornarListaDeIndicesEmbaralhados(quantidadeDeAmostras, quantidadeDeIteracoes)
            else:
                listaDeIndices = list(range(quantidadeDeAmostras))

            indiceInicialDoMiniBatch = Constantes.INDICE_INICIAL

            while(indiceInicialDoMiniBatch < quantidadeDeAmostras):
                indiceFinalDoMiniBatch = indiceInicialDoMiniBatch + tamanhoDoMiniBatch

                if(indiceFinalDoMiniBatch > quantidadeDeAmostras):
                    indiceFinalDoMiniBatch = quantidadeDeAmostras

                miniBatch = GerenciadorSGD.retornarMiniBatch(listaDeEntradasNormalizadas, listaDeSaidasEsperadas, listaDeIndices, indiceInicialDoMiniBatch, indiceFinalDoMiniBatch)

                if(miniBatch is None):
                    return None

                modeloFoiAtualizado = GerenciadorSGD.atualizarModelo(modeloLogistico, miniBatch[Constantes.INDICE_DAS_ENTRADAS_DO_MINI_BATCH], miniBatch[Constantes.INDICE_DAS_SAIDAS_DO_MINI_BATCH], learningRate)

                if(not modeloFoiAtualizado):
                    return None

                indiceInicialDoMiniBatch = indiceFinalDoMiniBatch

            funcaoObjetivo = GerenciadorDeRegressaoLogistica.retornarFuncaoObjetivo(modeloLogistico, listaDeEntradasNormalizadas, listaDeSaidasEsperadas)
            listaDoGradienteDosPesos = GerenciadorDeRegressaoLogistica.retornarGradienteDosPesos(modeloLogistico, listaDeEntradasNormalizadas, listaDeSaidasEsperadas)
            gradienteDoVies = GerenciadorDeRegressaoLogistica.retornarGradienteDoVies(modeloLogistico, listaDeEntradasNormalizadas, listaDeSaidasEsperadas)
            normaDoGradiente = GerenciadorDeRegressaoLogistica.retornarNormaDoGradiente(listaDoGradienteDosPesos, gradienteDoVies)
            acuracia = GerenciadorDeRegressaoLogistica.retornarAcuracia(modeloLogistico, listaDeEntradasNormalizadas, listaDeSaidasEsperadas)

            if(funcaoObjetivo is None):
                return None

            elif(normaDoGradiente is None):
                return None

            elif(acuracia is None):
                return None

            listaDaFuncaoObjetivo.append(funcaoObjetivo)
            listaDaNormaDoGradiente.append(normaDoGradiente)
            listaDaAcuracia.append(acuracia)

            quantidadeDeIteracoes = quantidadeDeIteracoes + Constantes.INCREMENTO_UNITARIO

            if(normaDoGradiente <= tolerancia):
                motivoDaParada = Constantes.MOTIVO_DA_PARADA_POR_NORMA_DO_GRADIENTE
                break

            if(funcaoObjetivoAnterior is not None):
                variacaoDaFuncaoObjetivo = abs(funcaoObjetivoAnterior - funcaoObjetivo)

                if(variacaoDaFuncaoObjetivo <= tolerancia):
                    motivoDaParada = Constantes.MOTIVO_DA_PARADA_POR_VARIACAO_DA_FUNCAO_OBJETIVO
                    break

            funcaoObjetivoAnterior = funcaoObjetivo

        tempoComputacional = time.perf_counter() - tempoInicial
        acuraciaFinal = GerenciadorDeRegressaoLogistica.retornarAcuracia(modeloLogistico, listaDeEntradasNormalizadas, listaDeSaidasEsperadas)

        if(acuraciaFinal is None):
            return None

        resultadoDoTreinamento = ResultadoDoTreinamento()

        resultadoDoTreinamento.setModeloLogistico(modeloLogistico)
        resultadoDoTreinamento.setListaDaFuncaoObjetivo(listaDaFuncaoObjetivo)
        resultadoDoTreinamento.setListaDaNormaDoGradiente(listaDaNormaDoGradiente)
        resultadoDoTreinamento.setListaDaAcuracia(listaDaAcuracia)
        resultadoDoTreinamento.setQuantidadeDeIteracoes(quantidadeDeIteracoes)
        resultadoDoTreinamento.setTempoComputacional(tempoComputacional)
        resultadoDoTreinamento.setAcuracia(acuraciaFinal)
        resultadoDoTreinamento.setMotivoDaParada(motivoDaParada)

        return resultadoDoTreinamento