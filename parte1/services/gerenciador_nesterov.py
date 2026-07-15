import time

from model.entidades.modelo_logistico import ModeloLogistico
from model.entidades.resultado_do_treinamento import ResultadoDoTreinamento
from services.constantes import Constantes
from services.gerenciador_de_regressao_logistica import GerenciadorDeRegressaoLogistica


class GerenciadorNesterov:

    @staticmethod
    def retornarModeloAntecipado(modeloLogistico, listaDeVelocidadesDosPesos, velocidadeDoVies, beta):
        if(modeloLogistico is None):
            return None

        elif(listaDeVelocidadesDosPesos is None):
            return None

        listaDePesos = modeloLogistico.getListaDePesos()

        if(len(listaDePesos) != len(listaDeVelocidadesDosPesos)):
            return None

        listaDePesosAntecipados = []
        indiceDoPeso = Constantes.INDICE_INICIAL
        quantidadeDePesos = len(listaDePesos)

        while(indiceDoPeso < quantidadeDePesos):
            pesoAntecipado = listaDePesos[indiceDoPeso] + beta * listaDeVelocidadesDosPesos[indiceDoPeso]
            listaDePesosAntecipados.append(pesoAntecipado)
            indiceDoPeso = indiceDoPeso + Constantes.INCREMENTO_UNITARIO

        viesAntecipado = modeloLogistico.getVies() + beta * velocidadeDoVies

        return ModeloLogistico(listaDePesosAntecipados, viesAntecipado)

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
        beta = configuracaoDoTreinamento.getBeta()

        if(learningRate <= Constantes.QUANTIDADE_NULA):
            return None

        elif(tolerancia < Constantes.QUANTIDADE_NULA):
            return None

        elif(numeroMaximoDeIteracoes <= Constantes.QUANTIDADE_NULA):
            return None

        elif(beta < Constantes.QUANTIDADE_NULA):
            return None

        elif(beta >= Constantes.OCUPACAO_PRESENTE):
            return None

        quantidadeDePesos = len(modeloLogistico.getListaDePesos())
        listaDeVelocidadesDosPesos = []
        indiceDoPeso = Constantes.INDICE_INICIAL

        while(indiceDoPeso < quantidadeDePesos):
            listaDeVelocidadesDosPesos.append(Constantes.VALOR_INICIAL_DOS_PARAMETROS)
            indiceDoPeso = indiceDoPeso + Constantes.INCREMENTO_UNITARIO

        velocidadeDoVies = Constantes.VALOR_INICIAL_DOS_PARAMETROS
        listaDaFuncaoObjetivo = []
        listaDaNormaDoGradiente = []
        listaDaAcuracia = []
        quantidadeDeIteracoes = Constantes.QUANTIDADE_NULA
        funcaoObjetivoAnterior = None
        motivoDaParada = Constantes.MOTIVO_DA_PARADA_POR_NUMERO_MAXIMO_DE_ITERACOES
        tempoInicial = time.perf_counter()

        while(quantidadeDeIteracoes < numeroMaximoDeIteracoes):
            funcaoObjetivo = GerenciadorDeRegressaoLogistica.retornarFuncaoObjetivo(modeloLogistico, listaDeEntradasNormalizadas, listaDeSaidasEsperadas)
            acuracia = GerenciadorDeRegressaoLogistica.retornarAcuracia(modeloLogistico, listaDeEntradasNormalizadas, listaDeSaidasEsperadas)

            modeloAntecipado = GerenciadorNesterov.retornarModeloAntecipado(modeloLogistico, listaDeVelocidadesDosPesos, velocidadeDoVies, beta)

            if(modeloAntecipado is None):
                return None

            listaDoGradienteDosPesos = GerenciadorDeRegressaoLogistica.retornarGradienteDosPesos(modeloAntecipado, listaDeEntradasNormalizadas, listaDeSaidasEsperadas)
            gradienteDoVies = GerenciadorDeRegressaoLogistica.retornarGradienteDoVies(modeloAntecipado, listaDeEntradasNormalizadas, listaDeSaidasEsperadas)
            normaDoGradiente = GerenciadorDeRegressaoLogistica.retornarNormaDoGradiente(listaDoGradienteDosPesos, gradienteDoVies)

            if(funcaoObjetivo is None):
                return None

            elif(acuracia is None):
                return None

            elif(listaDoGradienteDosPesos is None):
                return None

            elif(gradienteDoVies is None):
                return None

            elif(normaDoGradiente is None):
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

            while(indiceDoPeso < quantidadeDePesos):
                velocidadeDoPeso = beta * listaDeVelocidadesDosPesos[indiceDoPeso] - learningRate * listaDoGradienteDosPesos[indiceDoPeso]
                novoPeso = listaDePesos[indiceDoPeso] + velocidadeDoPeso

                listaDeVelocidadesDosPesos[indiceDoPeso] = velocidadeDoPeso
                novaListaDePesos.append(novoPeso)

                indiceDoPeso = indiceDoPeso + Constantes.INCREMENTO_UNITARIO

            velocidadeDoVies = beta * velocidadeDoVies - learningRate * gradienteDoVies
            novoVies = modeloLogistico.getVies() + velocidadeDoVies

            modeloLogistico.setListaDePesos(novaListaDePesos)
            modeloLogistico.setVies(novoVies)

            funcaoObjetivoAnterior = funcaoObjetivo
            quantidadeDeIteracoes = quantidadeDeIteracoes + Constantes.INCREMENTO_UNITARIO

        tempoComputacional = time.perf_counter() - tempoInicial
        acuraciaFinal = GerenciadorDeRegressaoLogistica.retornarAcuracia(modeloLogistico, listaDeEntradasNormalizadas, listaDeSaidasEsperadas)

        if(acuraciaFinal is None):
            return None

        resultado = ResultadoDoTreinamento()

        resultado.setModeloLogistico(modeloLogistico)
        resultado.setListaDaFuncaoObjetivo(listaDaFuncaoObjetivo)
        resultado.setListaDaNormaDoGradiente(listaDaNormaDoGradiente)
        resultado.setListaDaAcuracia(listaDaAcuracia)
        resultado.setQuantidadeDeIteracoes(quantidadeDeIteracoes)
        resultado.setTempoComputacional(tempoComputacional)
        resultado.setAcuracia(acuraciaFinal)
        resultado.setMotivoDaParada(motivoDaParada)

        return resultado