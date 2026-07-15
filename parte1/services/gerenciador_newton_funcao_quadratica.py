import time

import numpy as np

from model.entidades.resultado_otimizacao import ResultadoOtimizacao
from services.constantes_parte_2 import ConstantesParte2
from services.gerenciador_funcao_quadratica import GerenciadorFuncaoQuadratica


class GerenciadorNewtonFuncaoQuadratica:

    @staticmethod
    def retornarDirecaoDeNewton(funcaoQuadratica, ponto):
        listaDoGradiente = GerenciadorFuncaoQuadratica.retornarGradiente(funcaoQuadratica, ponto)
        hessiana = GerenciadorFuncaoQuadratica.retornarHessiana(funcaoQuadratica)

        if(listaDoGradiente is None):
            return None

        elif(hessiana is None):
            return None

        try:
            vetorDoGradiente = np.asarray(listaDoGradiente, dtype=float)
            matrizHessiana = np.asarray(hessiana, dtype=float)
            direcaoDeNewton = np.linalg.solve(matrizHessiana, -vetorDoGradiente)

            return direcaoDeNewton.tolist()

        except Exception:
            return None

    @staticmethod
    def executar(funcaoQuadratica, pontoInicial, tolerancia, numeroMaximoDeIteracoes):
        if(not GerenciadorFuncaoQuadratica.funcaoQuadraticaEhValida(funcaoQuadratica)):
            return None

        elif(not GerenciadorFuncaoQuadratica.matrizEhPositivaDefinida(funcaoQuadratica.getMatrizA())):
            return None

        elif(not GerenciadorFuncaoQuadratica.pontoEhValido(funcaoQuadratica, pontoInicial)):
            return None

        elif(tolerancia < ConstantesParte2.QUANTIDADE_NULA):
            return None

        elif(numeroMaximoDeIteracoes <= ConstantesParte2.QUANTIDADE_NULA):
            return None

        try:
            vetorDoPonto = np.asarray(pontoInicial, dtype=float)
            listaDePontos = []
            listaDaFuncaoObjetivo = []
            listaDaNormaDoGradiente = []
            quantidadeDeIteracoes = ConstantesParte2.QUANTIDADE_NULA
            motivoDaParada = ConstantesParte2.MOTIVO_DA_PARADA_POR_NUMERO_MAXIMO_DE_ITERACOES
            tempoInicial = time.perf_counter()

            while(quantidadeDeIteracoes < numeroMaximoDeIteracoes):
                pontoAtual = vetorDoPonto.tolist()
                valorDaFuncaoObjetivo = GerenciadorFuncaoQuadratica.retornarValorDaFuncaoObjetivo(funcaoQuadratica, pontoAtual)
                normaDoGradiente = GerenciadorFuncaoQuadratica.retornarNormaDoGradiente(funcaoQuadratica, pontoAtual)

                if(valorDaFuncaoObjetivo is None):
                    return None

                elif(normaDoGradiente is None):
                    return None

                listaDePontos.append(pontoAtual)
                listaDaFuncaoObjetivo.append(valorDaFuncaoObjetivo)
                listaDaNormaDoGradiente.append(normaDoGradiente)

                if(normaDoGradiente <= tolerancia):
                    motivoDaParada = ConstantesParte2.MOTIVO_DA_PARADA_POR_NORMA_DO_GRADIENTE
                    break

                listaDaDirecaoDeNewton = GerenciadorNewtonFuncaoQuadratica.retornarDirecaoDeNewton(funcaoQuadratica, pontoAtual)

                if(listaDaDirecaoDeNewton is None):
                    motivoDaParada = ConstantesParte2.MOTIVO_DA_PARADA_POR_DIRECAO_INVALIDA
                    break

                vetorDaDirecaoDeNewton = np.asarray(listaDaDirecaoDeNewton, dtype=float)
                vetorDoPonto = vetorDoPonto + vetorDaDirecaoDeNewton

                quantidadeDeIteracoes = quantidadeDeIteracoes + ConstantesParte2.INCREMENTO_UNITARIO

            pontoFinal = vetorDoPonto.tolist()

            if((len(listaDePontos) == ConstantesParte2.QUANTIDADE_NULA) or (listaDePontos[-ConstantesParte2.INCREMENTO_UNITARIO] != pontoFinal)):
                valorFinalDaFuncaoObjetivo = GerenciadorFuncaoQuadratica.retornarValorDaFuncaoObjetivo(funcaoQuadratica, pontoFinal)
                normaFinalDoGradiente = GerenciadorFuncaoQuadratica.retornarNormaDoGradiente(funcaoQuadratica, pontoFinal)

                if(valorFinalDaFuncaoObjetivo is None):
                    return None

                elif(normaFinalDoGradiente is None):
                    return None

                listaDePontos.append(pontoFinal)
                listaDaFuncaoObjetivo.append(valorFinalDaFuncaoObjetivo)
                listaDaNormaDoGradiente.append(normaFinalDoGradiente)

                if(normaFinalDoGradiente <= tolerancia):
                    motivoDaParada = ConstantesParte2.MOTIVO_DA_PARADA_POR_NORMA_DO_GRADIENTE

            tempoComputacional = time.perf_counter() - tempoInicial

            resultado = ResultadoOtimizacao()
            resultado.setPontoFinal(pontoFinal)
            resultado.setListaDePontos(listaDePontos)
            resultado.setListaDaFuncaoObjetivo(listaDaFuncaoObjetivo)
            resultado.setListaDaNormaDoGradiente(listaDaNormaDoGradiente)
            resultado.setQuantidadeDeIteracoes(quantidadeDeIteracoes)
            resultado.setTempoComputacional(tempoComputacional)
            resultado.setMotivoDaParada(motivoDaParada)

            return resultado

        except Exception:
            return None