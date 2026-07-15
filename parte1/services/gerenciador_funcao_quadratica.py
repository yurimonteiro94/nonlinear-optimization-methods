import math

import numpy as np

from services.constantes import Constantes


class GerenciadorFuncaoQuadratica:

    @staticmethod
    def funcaoQuadraticaEhValida(funcaoQuadratica):
        if(funcaoQuadratica is None):
            return False

        matrizA = funcaoQuadratica.getMatrizA()
        vetorB = funcaoQuadratica.getVetorB()

        if(matrizA is None):
            return False

        elif(vetorB is None):
            return False

        try:
            matrizAConvertida = np.asarray(matrizA, dtype=float)
            vetorBConvertido = np.asarray(vetorB, dtype=float)

            if(matrizAConvertida.ndim != Constantes.QUANTIDADE_DE_DIMENSOES_DA_MATRIZ):
                return False

            elif(vetorBConvertido.ndim != Constantes.QUANTIDADE_DE_DIMENSOES_DO_VETOR):
                return False

            quantidadeDeLinhas = matrizAConvertida.shape[Constantes.INDICE_DA_QUANTIDADE_DE_LINHAS]
            quantidadeDeColunas = matrizAConvertida.shape[Constantes.INDICE_DA_QUANTIDADE_DE_COLUNAS]

            if(quantidadeDeLinhas != quantidadeDeColunas):
                return False

            elif(quantidadeDeLinhas != vetorBConvertido.shape[Constantes.INDICE_DA_QUANTIDADE_DE_LINHAS]):
                return False

            return True

        except Exception:
            return False

    @staticmethod
    def matrizEhSimetrica(matriz):
        if(matriz is None):
            return False

        try:
            matrizConvertida = np.asarray(matriz, dtype=float)

            if(matrizConvertida.ndim != Constantes.QUANTIDADE_DE_DIMENSOES_DA_MATRIZ):
                return False

            quantidadeDeLinhas = matrizConvertida.shape[Constantes.INDICE_DA_QUANTIDADE_DE_LINHAS]
            quantidadeDeColunas = matrizConvertida.shape[Constantes.INDICE_DA_QUANTIDADE_DE_COLUNAS]

            if(quantidadeDeLinhas != quantidadeDeColunas):
                return False

            return bool(np.allclose(matrizConvertida, matrizConvertida.T))

        except Exception:
            return False

    @staticmethod
    def matrizEhPositivaDefinida(matriz):
        if(not GerenciadorFuncaoQuadratica.matrizEhSimetrica(matriz)):
            return False

        try:
            matrizConvertida = np.asarray(matriz, dtype=float)
            listaDeAutovalores = np.linalg.eigvalsh(matrizConvertida)

            return bool(np.all(listaDeAutovalores > Constantes.TOLERANCIA_NUMERICA))

        except Exception:
            return False

    @staticmethod
    def pontoEhValido(funcaoQuadratica, ponto):
        if(not GerenciadorFuncaoQuadratica.funcaoQuadraticaEhValida(funcaoQuadratica)):
            return False

        elif(ponto is None):
            return False

        try:
            vetorDoPonto = np.asarray(ponto, dtype=float)

            if(vetorDoPonto.ndim != Constantes.QUANTIDADE_DE_DIMENSOES_DO_VETOR):
                return False

            quantidadeDeVariaveis = len(funcaoQuadratica.getVetorB())

            return bool(vetorDoPonto.shape[Constantes.INDICE_DA_QUANTIDADE_DE_LINHAS] == quantidadeDeVariaveis)

        except Exception:
            return False

    @staticmethod
    def retornarValorDaFuncaoObjetivo(funcaoQuadratica, ponto):
        if(not GerenciadorFuncaoQuadratica.pontoEhValido(funcaoQuadratica, ponto)):
            return None

        try:
            matrizA = np.asarray(funcaoQuadratica.getMatrizA(), dtype=float)
            vetorB = np.asarray(funcaoQuadratica.getVetorB(), dtype=float)
            vetorDoPonto = np.asarray(ponto, dtype=float)
            constanteC = float(funcaoQuadratica.getConstanteC())

            parcelaQuadratica = Constantes.METADE * vetorDoPonto.T @ matrizA @ vetorDoPonto
            parcelaLinear = vetorB.T @ vetorDoPonto

            return float(parcelaQuadratica + parcelaLinear + constanteC)

        except Exception:
            return None

    @staticmethod
    def retornarGradiente(funcaoQuadratica, ponto):
        if(not GerenciadorFuncaoQuadratica.pontoEhValido(funcaoQuadratica, ponto)):
            return None

        try:
            matrizA = np.asarray(funcaoQuadratica.getMatrizA(), dtype=float)
            vetorB = np.asarray(funcaoQuadratica.getVetorB(), dtype=float)
            vetorDoPonto = np.asarray(ponto, dtype=float)

            vetorDoGradiente = matrizA @ vetorDoPonto + vetorB

            return vetorDoGradiente.tolist()

        except Exception:
            return None

    @staticmethod
    def retornarNormaDoGradiente(funcaoQuadratica, ponto):
        listaDoGradiente = GerenciadorFuncaoQuadratica.retornarGradiente(funcaoQuadratica, ponto)

        if(listaDoGradiente is None):
            return None

        try:
            vetorDoGradiente = np.asarray(listaDoGradiente, dtype=float)

            return float(np.linalg.norm(vetorDoGradiente))

        except Exception:
            return None

    @staticmethod
    def retornarHessiana(funcaoQuadratica):
        if(not GerenciadorFuncaoQuadratica.funcaoQuadraticaEhValida(funcaoQuadratica)):
            return None

        try:
            matrizA = np.asarray(funcaoQuadratica.getMatrizA(), dtype=float)

            return matrizA.tolist()

        except Exception:
            return None

    @staticmethod
    def retornarNumeroDeCondicao(funcaoQuadratica):
        if(not GerenciadorFuncaoQuadratica.funcaoQuadraticaEhValida(funcaoQuadratica)):
            return None

        try:
            matrizA = np.asarray(funcaoQuadratica.getMatrizA(), dtype=float)
            numeroDeCondicao = np.linalg.cond(matrizA)

            if(not math.isfinite(numeroDeCondicao)):
                return None

            return float(numeroDeCondicao)

        except Exception:
            return None

    @staticmethod
    def retornarPontoOtimo(funcaoQuadratica):
        if(not GerenciadorFuncaoQuadratica.funcaoQuadraticaEhValida(funcaoQuadratica)):
            return None

        elif(not GerenciadorFuncaoQuadratica.matrizEhPositivaDefinida(funcaoQuadratica.getMatrizA())):
            return None

        try:
            matrizA = np.asarray(funcaoQuadratica.getMatrizA(), dtype=float)
            vetorB = np.asarray(funcaoQuadratica.getVetorB(), dtype=float)
            pontoOtimo = np.linalg.solve(matrizA, -vetorB)

            return pontoOtimo.tolist()

        except Exception:
            return None