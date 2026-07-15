import time

from model.entidades.resultado_do_treinamento import ResultadoDoTreinamento
from services.constantes import Constantes
from services.gerenciador_de_regressao_logistica import GerenciadorDeRegressaoLogistica


class GerenciadorSteepestDescent:

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

        if(learningRate <= Constantes.QUANTIDADE_NULA):
            return None

        elif(tolerancia < Constantes.QUANTIDADE_NULA):
            return None

        elif(numeroMaximoDeIteracoes <= Constantes.QUANTIDADE_NULA):
            return None

        listaDaFuncaoObjetivo = []
        listaDaNormaDoGradiente = []
        listaDaAcuracia = []
        quantidadeDeIteracoes = Constantes.QUANTIDADE_NULA
        motivoDaParada = Constantes.MOTIVO_DA_PARADA_POR_NUMERO_MAXIMO_DE_ITERACOES
        funcaoObjetivoAnterior = None
        tempoInicial = time.perf_counter()

        while(quantidadeDeIteracoes < numeroMaximoDeIteracoes):
            funcaoObjetivo = GerenciadorDeRegressaoLogistica.retornarFuncaoObjetivo(modeloLogistico, listaDeEntradasNormalizadas, listaDeSaidasEsperadas)
            listaDoGradienteDosPesos = GerenciadorDeRegressaoLogistica.retornarGradienteDosPesos(modeloLogistico, listaDeEntradasNormalizadas, listaDeSaidasEsperadas)
            gradienteDoVies = GerenciadorDeRegressaoLogistica.retornarGradienteDoVies(modeloLogistico, listaDeEntradasNormalizadas, listaDeSaidasEsperadas)
            normaDoGradiente = GerenciadorDeRegressaoLogistica.retornarNormaDoGradiente(listaDoGradienteDosPesos, gradienteDoVies)
            acuracia = GerenciadorDeRegressaoLogistica.retornarAcuracia(modeloLogistico, listaDeEntradasNormalizadas, listaDeSaidasEsperadas)

            if(funcaoObjetivo is None):
                return None

            elif(listaDoGradienteDosPesos is None):
                return None

            elif(gradienteDoVies is None):
                return None

            elif(normaDoGradiente is None):
                return None

            elif(acuracia is None):
                return None

            listaDaFuncaoObjetivo.append(funcaoObjetivo)
            listaDaNormaDoGradiente.append(normaDoGradiente)
            listaDaAcuracia.append(acuracia)

            if(normaDoGradiente <= tolerancia):
                motivoDaParada = Constantes.MOTIVO_DA_PARADA_POR_NORMA_DO_GRADIENTE
                break

            if(funcaoObjetivoAnterior is not None):
                variacaoDaFuncaoObjetivo = abs(funcaoObjetivoAnterior - funcaoObjetivo)

                if(variacaoDaFuncaoObjetivo <= tolerancia):
                    motivoDaParada = Constantes.MOTIVO_DA_PARADA_POR_VARIACAO_DA_FUNCAO_OBJETIVO
                    break

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

            funcaoObjetivoAnterior = funcaoObjetivo
            quantidadeDeIteracoes = quantidadeDeIteracoes + Constantes.INCREMENTO_UNITARIO

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