import math

import numpy as np

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
    def retornarListaDeProbabilidades(modeloLogistico, listaDeEntradasNormalizadas):
        if(modeloLogistico is None):
            return None

        elif(listaDeEntradasNormalizadas is None):
            return None

        elif(len(listaDeEntradasNormalizadas) == Constantes.QUANTIDADE_NULA):
            return None

        listaDePesos = modeloLogistico.getListaDePesos()

        if(listaDePesos is None):
            return None

        try:
            matrizDeEntradas = np.asarray(listaDeEntradasNormalizadas, dtype=float)
            vetorDePesos = np.asarray(listaDePesos, dtype=float)

            if(matrizDeEntradas.ndim != Constantes.QUANTIDADE_DE_DIMENSOES_DA_MATRIZ):
                return None

            elif(vetorDePesos.ndim != Constantes.QUANTIDADE_DE_DIMENSOES_DO_VETOR):
                return None

            elif(matrizDeEntradas.shape[Constantes.INDICE_DA_QUANTIDADE_DE_COLUNAS] != vetorDePesos.shape[Constantes.INDICE_DA_QUANTIDADE_DE_LINHAS]):
                return None

            vetorDeCombinacoesLineares = matrizDeEntradas @ vetorDePesos
            vetorDeCombinacoesLineares = vetorDeCombinacoesLineares + modeloLogistico.getVies()

            vetorDeProbabilidades = np.empty_like(vetorDeCombinacoesLineares)
            vetorDeIndicesNaoNegativos = vetorDeCombinacoesLineares >= Constantes.QUANTIDADE_NULA
            vetorDeIndicesNegativos = np.logical_not(vetorDeIndicesNaoNegativos)

            vetorDeProbabilidades[vetorDeIndicesNaoNegativos] = 1.0 / (1.0 + np.exp(-vetorDeCombinacoesLineares[vetorDeIndicesNaoNegativos]))

            vetorDeExponenciais = np.exp(vetorDeCombinacoesLineares[vetorDeIndicesNegativos])
            vetorDeProbabilidades[vetorDeIndicesNegativos] = vetorDeExponenciais / (1.0 + vetorDeExponenciais)

            return vetorDeProbabilidades.tolist()

        except Exception:
            return None

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

        listaDeProbabilidades = GerenciadorDeRegressaoLogistica.retornarListaDeProbabilidades(modeloLogistico, listaDeEntradasNormalizadas)

        if(listaDeProbabilidades is None):
            return None

        try:
            vetorDeProbabilidades = np.asarray(listaDeProbabilidades, dtype=float)
            vetorDeSaidasEsperadas = np.asarray(listaDeSaidasEsperadas, dtype=float)

            vetorDeProbabilidades = np.clip(vetorDeProbabilidades, Constantes.MENOR_PROBABILIDADE_PERMITIDA, Constantes.MAIOR_PROBABILIDADE_PERMITIDA)

            vetorDePerdas = vetorDeSaidasEsperadas * np.log(vetorDeProbabilidades)
            vetorDePerdas = vetorDePerdas + (Constantes.OCUPACAO_PRESENTE - vetorDeSaidasEsperadas) * np.log(Constantes.OCUPACAO_PRESENTE - vetorDeProbabilidades)

            return float(-np.mean(vetorDePerdas))

        except Exception:
            return None

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

        listaDeProbabilidades = GerenciadorDeRegressaoLogistica.retornarListaDeProbabilidades(modeloLogistico, listaDeEntradasNormalizadas)

        if(listaDeProbabilidades is None):
            return None

        try:
            matrizDeEntradas = np.asarray(listaDeEntradasNormalizadas, dtype=float)
            vetorDeSaidasEsperadas = np.asarray(listaDeSaidasEsperadas, dtype=float)
            vetorDeProbabilidades = np.asarray(listaDeProbabilidades, dtype=float)

            vetorDeErros = vetorDeProbabilidades - vetorDeSaidasEsperadas
            vetorDoGradiente = matrizDeEntradas.T @ vetorDeErros
            vetorDoGradiente = vetorDoGradiente / matrizDeEntradas.shape[Constantes.INDICE_DA_QUANTIDADE_DE_LINHAS]

            return vetorDoGradiente.tolist()

        except Exception:
            return None

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

        listaDeProbabilidades = GerenciadorDeRegressaoLogistica.retornarListaDeProbabilidades(modeloLogistico, listaDeEntradasNormalizadas)

        if(listaDeProbabilidades is None):
            return None

        try:
            vetorDeProbabilidades = np.asarray(listaDeProbabilidades, dtype=float)
            vetorDeSaidasEsperadas = np.asarray(listaDeSaidasEsperadas, dtype=float)

            vetorDeErros = vetorDeProbabilidades - vetorDeSaidasEsperadas

            return float(np.mean(vetorDeErros))

        except Exception:
            return None

    @staticmethod
    def retornarNormaDoGradiente(listaDoGradienteDosPesos, gradienteDoVies):
        if(listaDoGradienteDosPesos is None):
            return None

        elif(gradienteDoVies is None):
            return None

        try:
            vetorDoGradiente = np.asarray(listaDoGradienteDosPesos, dtype=float)
            somaDosQuadrados = np.dot(vetorDoGradiente, vetorDoGradiente)
            somaDosQuadrados = somaDosQuadrados + gradienteDoVies * gradienteDoVies

            return float(math.sqrt(somaDosQuadrados))

        except Exception:
            return None

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

        listaDeProbabilidades = GerenciadorDeRegressaoLogistica.retornarListaDeProbabilidades(modeloLogistico, listaDeEntradasNormalizadas)

        if(listaDeProbabilidades is None):
            return None

        try:
            vetorDeProbabilidades = np.asarray(listaDeProbabilidades, dtype=float)
            vetorDeSaidasEsperadas = np.asarray(listaDeSaidasEsperadas, dtype=int)

            vetorDeClassesPrevistas = vetorDeProbabilidades >= Constantes.LIMIAR_DE_CLASSIFICACAO
            vetorDeClassesPrevistas = vetorDeClassesPrevistas.astype(int)

            return float(np.mean(vetorDeClassesPrevistas == vetorDeSaidasEsperadas))

        except Exception:
            return None