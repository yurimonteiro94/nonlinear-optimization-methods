import os

import matplotlib.pyplot as plt
import numpy as np

from controller.controller_otimizacao_quadratica import ControllerOtimizacaoQuadratica
from services.constantes_parte_2 import ConstantesParte2


class ViewParte2:

    @staticmethod
    def salvarGraficoDeValores(listaDeValores, titulo, textoDoEixoY, caminhoDoArquivo):
        if(listaDeValores is None):
            return False

        elif(len(listaDeValores) == ConstantesParte2.QUANTIDADE_NULA):
            return False

        try:
            if(not os.path.exists(ConstantesParte2.PASTA_DOS_GRAFICOS)):
                os.makedirs(ConstantesParte2.PASTA_DOS_GRAFICOS)

            plt.figure()
            plt.plot(listaDeValores)
            plt.title(titulo)
            plt.xlabel(ConstantesParte2.TEXTO_DO_EIXO_DAS_ITERACOES)
            plt.ylabel(textoDoEixoY)
            plt.grid(True)
            plt.tight_layout()
            plt.savefig(caminhoDoArquivo)
            plt.close()

            return True

        except Exception:
            plt.close()
            return False

    @staticmethod
    def salvarGraficoComparativo(listaDeValoresDoSteepestDescent, listaDeValoresDoNewton, titulo, textoDoEixoY, caminhoDoArquivo):
        if(listaDeValoresDoSteepestDescent is None):
            return False

        elif(listaDeValoresDoNewton is None):
            return False

        try:
            plt.figure()
            plt.plot(listaDeValoresDoSteepestDescent, label=ConstantesParte2.NOME_DO_METODO_STEEPEST_DESCENT)
            plt.plot(listaDeValoresDoNewton, label=ConstantesParte2.NOME_DO_METODO_NEWTON)
            plt.title(titulo)
            plt.xlabel(ConstantesParte2.TEXTO_DO_EIXO_DAS_ITERACOES)
            plt.ylabel(textoDoEixoY)
            plt.grid(True)
            plt.legend()
            plt.tight_layout()
            plt.savefig(caminhoDoArquivo)
            plt.close()

            return True

        except Exception:
            plt.close()
            return False

    @staticmethod
    def salvarGraficoDaTrajetoria(funcaoQuadratica, resultadoOtimizacao, titulo, caminhoDoArquivo):
        if(funcaoQuadratica is None):
            return False

        elif(resultadoOtimizacao is None):
            return False

        listaDePontos = resultadoOtimizacao.getListaDePontos()

        if(listaDePontos is None):
            return False

        elif(len(listaDePontos) == ConstantesParte2.QUANTIDADE_NULA):
            return False

        elif(len(listaDePontos[ConstantesParte2.INDICE_INICIAL]) != ConstantesParte2.QUANTIDADE_DE_VARIAVEIS_PARA_GRAFICO_DE_TRAJETORIA):
            return False

        try:
            matrizDePontos = np.asarray(listaDePontos, dtype=float)
            listaDeValoresDeX1 = matrizDePontos[:, ConstantesParte2.INDICE_INICIAL]
            listaDeValoresDeX2 = matrizDePontos[:, ConstantesParte2.INDICE_DA_SEGUNDA_VARIAVEL]

            valorMinimoDeX1 = float(np.min(listaDeValoresDeX1) - ConstantesParte2.MARGEM_DO_GRAFICO_DE_TRAJETORIA)
            valorMaximoDeX1 = float(np.max(listaDeValoresDeX1) + ConstantesParte2.MARGEM_DO_GRAFICO_DE_TRAJETORIA)
            valorMinimoDeX2 = float(np.min(listaDeValoresDeX2) - ConstantesParte2.MARGEM_DO_GRAFICO_DE_TRAJETORIA)
            valorMaximoDeX2 = float(np.max(listaDeValoresDeX2) + ConstantesParte2.MARGEM_DO_GRAFICO_DE_TRAJETORIA)

            listaDoEixoX1 = np.linspace(valorMinimoDeX1, valorMaximoDeX1, ConstantesParte2.QUANTIDADE_DE_PONTOS_DO_CONTORNO)
            listaDoEixoX2 = np.linspace(valorMinimoDeX2, valorMaximoDeX2, ConstantesParte2.QUANTIDADE_DE_PONTOS_DO_CONTORNO)
            matrizDoEixoX1, matrizDoEixoX2 = np.meshgrid(listaDoEixoX1, listaDoEixoX2)
            matrizDosValoresDaFuncao = np.zeros_like(matrizDoEixoX1)

            indiceDaLinha = ConstantesParte2.INDICE_INICIAL
            quantidadeDeLinhas = matrizDoEixoX1.shape[ConstantesParte2.INDICE_INICIAL]

            while(indiceDaLinha < quantidadeDeLinhas):
                indiceDaColuna = ConstantesParte2.INDICE_INICIAL
                quantidadeDeColunas = matrizDoEixoX1.shape[ConstantesParte2.INDICE_DA_SEGUNDA_VARIAVEL]

                while(indiceDaColuna < quantidadeDeColunas):
                    ponto = [
                        matrizDoEixoX1[indiceDaLinha][indiceDaColuna],
                        matrizDoEixoX2[indiceDaLinha][indiceDaColuna]
                    ]

                    valorDaFuncao = ControllerOtimizacaoQuadratica.retornarValorDaFuncaoObjetivo(funcaoQuadratica, ponto)

                    if(valorDaFuncao is None):
                        return False

                    matrizDosValoresDaFuncao[indiceDaLinha][indiceDaColuna] = valorDaFuncao
                    indiceDaColuna = indiceDaColuna + ConstantesParte2.INCREMENTO_UNITARIO

                indiceDaLinha = indiceDaLinha + ConstantesParte2.INCREMENTO_UNITARIO

            plt.figure()
            plt.contour(matrizDoEixoX1, matrizDoEixoX2, matrizDosValoresDaFuncao, levels=ConstantesParte2.QUANTIDADE_DE_NIVEIS_DO_CONTORNO)
            plt.plot(listaDeValoresDeX1, listaDeValoresDeX2, marker="o")
            plt.title(titulo)
            plt.xlabel(ConstantesParte2.TEXTO_DO_EIXO_X_1)
            plt.ylabel(ConstantesParte2.TEXTO_DO_EIXO_X_2)
            plt.grid(True)
            plt.tight_layout()
            plt.savefig(caminhoDoArquivo)
            plt.close()

            return True

        except Exception:
            plt.close()
            return False

    @staticmethod
    def retornarTextoDoResumo(nomeDoMetodo, funcaoQuadratica, resultadoOtimizacao):
        if(nomeDoMetodo is None):
            return None

        elif(funcaoQuadratica is None):
            return None

        elif(resultadoOtimizacao is None):
            return None

        listaDaFuncaoObjetivo = resultadoOtimizacao.getListaDaFuncaoObjetivo()
        listaDaNormaDoGradiente = resultadoOtimizacao.getListaDaNormaDoGradiente()
        pontoOtimoAnalitico = ControllerOtimizacaoQuadratica.retornarPontoOtimo(funcaoQuadratica)
        numeroDeCondicao = ControllerOtimizacaoQuadratica.retornarNumeroDeCondicao(funcaoQuadratica)

        if(listaDaFuncaoObjetivo is None):
            return None

        elif(listaDaNormaDoGradiente is None):
            return None

        elif(len(listaDaFuncaoObjetivo) == ConstantesParte2.QUANTIDADE_NULA):
            return None

        texto = nomeDoMetodo + ConstantesParte2.QUEBRA_DE_LINHA
        texto = texto + ConstantesParte2.QUEBRA_DE_LINHA
        texto = texto + "Ponto final = " + str(resultadoOtimizacao.getPontoFinal()) + ConstantesParte2.QUEBRA_DE_LINHA
        texto = texto + "Ponto ótimo analítico = " + str(pontoOtimoAnalitico) + ConstantesParte2.QUEBRA_DE_LINHA
        texto = texto + "Função objetivo inicial = " + str(listaDaFuncaoObjetivo[ConstantesParte2.INDICE_INICIAL]) + ConstantesParte2.QUEBRA_DE_LINHA
        texto = texto + "Função objetivo final = " + str(listaDaFuncaoObjetivo[-ConstantesParte2.INCREMENTO_UNITARIO]) + ConstantesParte2.QUEBRA_DE_LINHA
        texto = texto + "Norma inicial do gradiente = " + str(listaDaNormaDoGradiente[ConstantesParte2.INDICE_INICIAL]) + ConstantesParte2.QUEBRA_DE_LINHA
        texto = texto + "Norma final do gradiente = " + str(listaDaNormaDoGradiente[-ConstantesParte2.INCREMENTO_UNITARIO]) + ConstantesParte2.QUEBRA_DE_LINHA
        texto = texto + "Quantidade de iterações = " + str(resultadoOtimizacao.getQuantidadeDeIteracoes()) + ConstantesParte2.QUEBRA_DE_LINHA
        texto = texto + "Tempo computacional em segundos = " + str(resultadoOtimizacao.getTempoComputacional()) + ConstantesParte2.QUEBRA_DE_LINHA
        texto = texto + "Número de condição da Hessiana = " + str(numeroDeCondicao) + ConstantesParte2.QUEBRA_DE_LINHA
        texto = texto + "Motivo da parada = " + str(resultadoOtimizacao.getMotivoDaParada()) + ConstantesParte2.QUEBRA_DE_LINHA

        return texto

    @staticmethod
    def salvarTexto(texto, caminhoDoArquivo):
        if(texto is None):
            return False

        elif(caminhoDoArquivo is None):
            return False

        try:
            if(not os.path.exists(ConstantesParte2.PASTA_DOS_RESULTADOS)):
                os.makedirs(ConstantesParte2.PASTA_DOS_RESULTADOS)

            arquivo = open(caminhoDoArquivo, ConstantesParte2.MODO_DE_ESCRITA, encoding=ConstantesParte2.CODIFICACAO_DOS_ARQUIVOS_DE_SAIDA)
            arquivo.write(texto)
            arquivo.close()

            return True

        except Exception:
            return False

    @staticmethod
    def apresentarTexto(texto):
        if(texto is None):
            return False

        print(texto)

        return True

    @staticmethod
    def salvarResultadosDoSteepestDescent(funcaoQuadratica, resultadoOtimizacao):
        texto = ViewParte2.retornarTextoDoResumo(ConstantesParte2.NOME_DO_METODO_STEEPEST_DESCENT, funcaoQuadratica, resultadoOtimizacao)

        if(texto is None):
            return False

        graficoDaFuncaoObjetivoFoiSalvo = ViewParte2.salvarGraficoDeValores(resultadoOtimizacao.getListaDaFuncaoObjetivo(), ConstantesParte2.TITULO_DO_GRAFICO_DA_FUNCAO_OBJETIVO_DO_STEEPEST_DESCENT, ConstantesParte2.TEXTO_DO_EIXO_DA_FUNCAO_OBJETIVO, ConstantesParte2.CAMINHO_DO_GRAFICO_DA_FUNCAO_OBJETIVO_DO_STEEPEST_DESCENT)

        graficoDaNormaDoGradienteFoiSalvo = ViewParte2.salvarGraficoDeValores(resultadoOtimizacao.getListaDaNormaDoGradiente(), ConstantesParte2.TITULO_DO_GRAFICO_DA_NORMA_DO_GRADIENTE_DO_STEEPEST_DESCENT, ConstantesParte2.TEXTO_DO_EIXO_DA_NORMA_DO_GRADIENTE, ConstantesParte2.CAMINHO_DO_GRAFICO_DA_NORMA_DO_GRADIENTE_DO_STEEPEST_DESCENT)

        graficoDaTrajetoriaFoiSalvo = ViewParte2.salvarGraficoDaTrajetoria(funcaoQuadratica, resultadoOtimizacao, ConstantesParte2.TITULO_DO_GRAFICO_DA_TRAJETORIA_DO_STEEPEST_DESCENT, ConstantesParte2.CAMINHO_DO_GRAFICO_DA_TRAJETORIA_DO_STEEPEST_DESCENT)

        resumoFoiSalvo = ViewParte2.salvarTexto(texto, ConstantesParte2.CAMINHO_DO_ARQUIVO_DE_RESULTADOS_DO_STEEPEST_DESCENT)
        resumoFoiApresentado = ViewParte2.apresentarTexto(texto)

        return graficoDaFuncaoObjetivoFoiSalvo and graficoDaNormaDoGradienteFoiSalvo and graficoDaTrajetoriaFoiSalvo and resumoFoiSalvo and resumoFoiApresentado

    @staticmethod
    def salvarResultadosDoNewton(funcaoQuadratica, resultadoOtimizacao):
        texto = ViewParte2.retornarTextoDoResumo(ConstantesParte2.NOME_DO_METODO_NEWTON, funcaoQuadratica, resultadoOtimizacao)

        if(texto is None):
            return False

        graficoDaFuncaoObjetivoFoiSalvo = ViewParte2.salvarGraficoDeValores(resultadoOtimizacao.getListaDaFuncaoObjetivo(), ConstantesParte2.TITULO_DO_GRAFICO_DA_FUNCAO_OBJETIVO_DO_NEWTON, ConstantesParte2.TEXTO_DO_EIXO_DA_FUNCAO_OBJETIVO, ConstantesParte2.CAMINHO_DO_GRAFICO_DA_FUNCAO_OBJETIVO_DO_NEWTON)

        graficoDaNormaDoGradienteFoiSalvo = ViewParte2.salvarGraficoDeValores(resultadoOtimizacao.getListaDaNormaDoGradiente(), ConstantesParte2.TITULO_DO_GRAFICO_DA_NORMA_DO_GRADIENTE_DO_NEWTON, ConstantesParte2.TEXTO_DO_EIXO_DA_NORMA_DO_GRADIENTE, ConstantesParte2.CAMINHO_DO_GRAFICO_DA_NORMA_DO_GRADIENTE_DO_NEWTON)

        graficoDaTrajetoriaFoiSalvo = ViewParte2.salvarGraficoDaTrajetoria(funcaoQuadratica, resultadoOtimizacao, ConstantesParte2.TITULO_DO_GRAFICO_DA_TRAJETORIA_DO_NEWTON, ConstantesParte2.CAMINHO_DO_GRAFICO_DA_TRAJETORIA_DO_NEWTON)

        resumoFoiSalvo = ViewParte2.salvarTexto(texto, ConstantesParte2.CAMINHO_DO_ARQUIVO_DE_RESULTADOS_DO_NEWTON)
        resumoFoiApresentado = ViewParte2.apresentarTexto(texto)

        return graficoDaFuncaoObjetivoFoiSalvo and graficoDaNormaDoGradienteFoiSalvo and graficoDaTrajetoriaFoiSalvo and resumoFoiSalvo and resumoFoiApresentado

    @staticmethod
    def salvarComparacao(resultadoDoSteepestDescent, resultadoDoNewton):
        if(resultadoDoSteepestDescent is None):
            return False

        elif(resultadoDoNewton is None):
            return False

        texto = "Comparação da Parte 2" + ConstantesParte2.QUEBRA_DE_LINHA
        texto = texto + ConstantesParte2.QUEBRA_DE_LINHA
        texto = texto + "Iterações do Steepest Descent = " + str(resultadoDoSteepestDescent.getQuantidadeDeIteracoes()) + ConstantesParte2.QUEBRA_DE_LINHA
        texto = texto + "Iterações do Newton = " + str(resultadoDoNewton.getQuantidadeDeIteracoes()) + ConstantesParte2.QUEBRA_DE_LINHA
        texto = texto + "Tempo do Steepest Descent = " + str(resultadoDoSteepestDescent.getTempoComputacional()) + ConstantesParte2.QUEBRA_DE_LINHA
        texto = texto + "Tempo do Newton = " + str(resultadoDoNewton.getTempoComputacional()) + ConstantesParte2.QUEBRA_DE_LINHA
        texto = texto + "O método de Newton utiliza a Hessiana e, para a função quadrática, alcança o ótimo em uma única atualização." + ConstantesParte2.QUEBRA_DE_LINHA
        texto = texto + "O Steepest Descent utiliza apenas o gradiente e pode apresentar trajetória em zigue-zague, principalmente em problemas mal condicionados." + ConstantesParte2.QUEBRA_DE_LINHA

        graficoDaFuncaoObjetivoFoiSalvo = ViewParte2.salvarGraficoComparativo(resultadoDoSteepestDescent.getListaDaFuncaoObjetivo(), resultadoDoNewton.getListaDaFuncaoObjetivo(), ConstantesParte2.TITULO_DO_GRAFICO_COMPARATIVO_DA_FUNCAO_OBJETIVO, ConstantesParte2.TEXTO_DO_EIXO_DA_FUNCAO_OBJETIVO, ConstantesParte2.CAMINHO_DO_GRAFICO_COMPARATIVO_DA_FUNCAO_OBJETIVO)

        graficoDaNormaDoGradienteFoiSalvo = ViewParte2.salvarGraficoComparativo(resultadoDoSteepestDescent.getListaDaNormaDoGradiente(), resultadoDoNewton.getListaDaNormaDoGradiente(), ConstantesParte2.TITULO_DO_GRAFICO_COMPARATIVO_DA_NORMA_DO_GRADIENTE, ConstantesParte2.TEXTO_DO_EIXO_DA_NORMA_DO_GRADIENTE, ConstantesParte2.CAMINHO_DO_GRAFICO_COMPARATIVO_DA_NORMA_DO_GRADIENTE)

        textoFoiSalvo = ViewParte2.salvarTexto(texto, ConstantesParte2.CAMINHO_DO_ARQUIVO_COMPARATIVO)
        textoFoiApresentado = ViewParte2.apresentarTexto(texto)

        return graficoDaFuncaoObjetivoFoiSalvo and graficoDaNormaDoGradienteFoiSalvo and textoFoiSalvo and textoFoiApresentado