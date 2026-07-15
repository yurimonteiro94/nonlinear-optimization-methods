import os

import matplotlib.pyplot as plt
import numpy as np

from controller.controller_otimizacao_quadratica import ControllerOtimizacaoQuadratica
from services.constantes_exercicio_5 import ConstantesExercicio5


class ViewExercicio5:

    @staticmethod
    def salvarGraficoDeValores(listaDeValores, titulo, textoDoEixoY, caminhoDoArquivo):
        if(listaDeValores is None):
            return False

        elif(len(listaDeValores) == ConstantesExercicio5.QUANTIDADE_NULA):
            return False

        elif(titulo is None):
            return False

        elif(caminhoDoArquivo is None):
            return False

        try:
            if(not os.path.exists(ConstantesExercicio5.PASTA_DOS_GRAFICOS)):
                os.makedirs(ConstantesExercicio5.PASTA_DOS_GRAFICOS)

            plt.figure()
            plt.plot(listaDeValores)
            plt.title(titulo)
            plt.xlabel(ConstantesExercicio5.TEXTO_DO_EIXO_DAS_ITERACOES)
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
    def salvarGraficoDasCoordenadas(listaDePontos, titulo, caminhoDoArquivo):
        if(listaDePontos is None):
            return False

        elif(len(listaDePontos) == ConstantesExercicio5.QUANTIDADE_NULA):
            return False

        try:
            matrizDePontos = np.asarray(listaDePontos, dtype=float)

            if(matrizDePontos.ndim != 2):
                return False

            quantidadeDeVariaveis = matrizDePontos.shape[1]
            indiceDaVariavel = ConstantesExercicio5.INDICE_INICIAL

            plt.figure()

            while(indiceDaVariavel < quantidadeDeVariaveis):
                listaDaCoordenada = matrizDePontos[:, indiceDaVariavel]
                nomeDaCoordenada = "x" + str(indiceDaVariavel + ConstantesExercicio5.INCREMENTO_UNITARIO)

                plt.plot(listaDaCoordenada, marker="o", label=nomeDaCoordenada)

                indiceDaVariavel = indiceDaVariavel + ConstantesExercicio5.INCREMENTO_UNITARIO

            plt.title(titulo)
            plt.xlabel(ConstantesExercicio5.TEXTO_DO_EIXO_DAS_ITERACOES)
            plt.ylabel(ConstantesExercicio5.TEXTO_DO_EIXO_DAS_COORDENADAS)
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
    def salvarGraficoComparativo(listaDeValoresDoSteepestDescent, listaDeValoresDoNewton, titulo, textoDoEixoY, caminhoDoArquivo):
        if(listaDeValoresDoSteepestDescent is None):
            return False

        elif(listaDeValoresDoNewton is None):
            return False

        elif(len(listaDeValoresDoSteepestDescent) == ConstantesExercicio5.QUANTIDADE_NULA):
            return False

        elif(len(listaDeValoresDoNewton) == ConstantesExercicio5.QUANTIDADE_NULA):
            return False

        try:
            plt.figure()

            plt.plot(
                listaDeValoresDoSteepestDescent,
                label=ConstantesExercicio5.NOME_DO_METODO_STEEPEST_DESCENT
            )

            plt.plot(
                listaDeValoresDoNewton,
                label=ConstantesExercicio5.NOME_DO_METODO_NEWTON
            )

            plt.title(titulo)
            plt.xlabel(ConstantesExercicio5.TEXTO_DO_EIXO_DAS_ITERACOES)
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
    def retornarTextoDoResumo(nomeDoMetodo, funcaoQuadratica, resultadoOtimizacao):
        if(nomeDoMetodo is None):
            return None

        elif(funcaoQuadratica is None):
            return None

        elif(resultadoOtimizacao is None):
            return None

        listaDaFuncaoObjetivo = resultadoOtimizacao.getListaDaFuncaoObjetivo()
        listaDaNormaDoGradiente = resultadoOtimizacao.getListaDaNormaDoGradiente()

        if(listaDaFuncaoObjetivo is None):
            return None

        elif(listaDaNormaDoGradiente is None):
            return None

        elif(len(listaDaFuncaoObjetivo) == ConstantesExercicio5.QUANTIDADE_NULA):
            return None

        pontoOtimo = ControllerOtimizacaoQuadratica.retornarPontoOtimo(funcaoQuadratica)
        numeroDeCondicao = ControllerOtimizacaoQuadratica.retornarNumeroDeCondicao(funcaoQuadratica)

        texto = "Exercício 5" + ConstantesExercicio5.QUEBRA_DE_LINHA
        texto = texto + nomeDoMetodo + ConstantesExercicio5.QUEBRA_DE_LINHA
        texto = texto + ConstantesExercicio5.QUEBRA_DE_LINHA

        texto = texto + "Ponto final = " + str(resultadoOtimizacao.getPontoFinal()) + ConstantesExercicio5.QUEBRA_DE_LINHA
        texto = texto + "Ponto ótimo analítico = " + str(pontoOtimo) + ConstantesExercicio5.QUEBRA_DE_LINHA
        texto = texto + "Função objetivo inicial = " + str(listaDaFuncaoObjetivo[ConstantesExercicio5.INDICE_INICIAL]) + ConstantesExercicio5.QUEBRA_DE_LINHA
        texto = texto + "Função objetivo final = " + str(listaDaFuncaoObjetivo[-ConstantesExercicio5.INCREMENTO_UNITARIO]) + ConstantesExercicio5.QUEBRA_DE_LINHA
        texto = texto + "Norma inicial do gradiente = " + str(listaDaNormaDoGradiente[ConstantesExercicio5.INDICE_INICIAL]) + ConstantesExercicio5.QUEBRA_DE_LINHA
        texto = texto + "Norma final do gradiente = " + str(listaDaNormaDoGradiente[-ConstantesExercicio5.INCREMENTO_UNITARIO]) + ConstantesExercicio5.QUEBRA_DE_LINHA
        texto = texto + "Quantidade de iterações = " + str(resultadoOtimizacao.getQuantidadeDeIteracoes()) + ConstantesExercicio5.QUEBRA_DE_LINHA
        texto = texto + "Tempo computacional em segundos = " + str(resultadoOtimizacao.getTempoComputacional()) + ConstantesExercicio5.QUEBRA_DE_LINHA
        texto = texto + "Número de condição da Hessiana = " + str(numeroDeCondicao) + ConstantesExercicio5.QUEBRA_DE_LINHA
        texto = texto + "Motivo da parada = " + str(resultadoOtimizacao.getMotivoDaParada()) + ConstantesExercicio5.QUEBRA_DE_LINHA

        return texto

    @staticmethod
    def salvarTexto(texto, caminhoDoArquivo):
        if(texto is None):
            return False

        elif(caminhoDoArquivo is None):
            return False

        try:
            if(not os.path.exists(ConstantesExercicio5.PASTA_DOS_RESULTADOS)):
                os.makedirs(ConstantesExercicio5.PASTA_DOS_RESULTADOS)

            arquivo = open(
                caminhoDoArquivo,
                ConstantesExercicio5.MODO_DE_ESCRITA,
                encoding=ConstantesExercicio5.CODIFICACAO_DOS_ARQUIVOS_DE_SAIDA
            )

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
        texto = ViewExercicio5.retornarTextoDoResumo(
            ConstantesExercicio5.NOME_DO_METODO_STEEPEST_DESCENT,
            funcaoQuadratica,
            resultadoOtimizacao
        )

        if(texto is None):
            return False

        graficoDaFuncaoObjetivoFoiSalvo = ViewExercicio5.salvarGraficoDeValores(
            resultadoOtimizacao.getListaDaFuncaoObjetivo(),
            ConstantesExercicio5.TITULO_DO_GRAFICO_DA_FUNCAO_OBJETIVO_DO_STEEPEST_DESCENT,
            ConstantesExercicio5.TEXTO_DO_EIXO_DA_FUNCAO_OBJETIVO,
            ConstantesExercicio5.CAMINHO_DO_GRAFICO_DA_FUNCAO_OBJETIVO_DO_STEEPEST_DESCENT
        )

        graficoDaNormaDoGradienteFoiSalvo = ViewExercicio5.salvarGraficoDeValores(
            resultadoOtimizacao.getListaDaNormaDoGradiente(),
            ConstantesExercicio5.TITULO_DO_GRAFICO_DA_NORMA_DO_GRADIENTE_DO_STEEPEST_DESCENT,
            ConstantesExercicio5.TEXTO_DO_EIXO_DA_NORMA_DO_GRADIENTE,
            ConstantesExercicio5.CAMINHO_DO_GRAFICO_DA_NORMA_DO_GRADIENTE_DO_STEEPEST_DESCENT
        )

        graficoDasCoordenadasFoiSalvo = ViewExercicio5.salvarGraficoDasCoordenadas(
            resultadoOtimizacao.getListaDePontos(),
            ConstantesExercicio5.TITULO_DO_GRAFICO_DAS_COORDENADAS_DO_STEEPEST_DESCENT,
            ConstantesExercicio5.CAMINHO_DO_GRAFICO_DAS_COORDENADAS_DO_STEEPEST_DESCENT
        )

        textoFoiSalvo = ViewExercicio5.salvarTexto(
            texto,
            ConstantesExercicio5.CAMINHO_DO_ARQUIVO_DO_RESULTADO_DO_STEEPEST_DESCENT
        )

        textoFoiApresentado = ViewExercicio5.apresentarTexto(texto)

        return graficoDaFuncaoObjetivoFoiSalvo and graficoDaNormaDoGradienteFoiSalvo and graficoDasCoordenadasFoiSalvo and textoFoiSalvo and textoFoiApresentado

    @staticmethod
    def salvarResultadosDoNewton(funcaoQuadratica, resultadoOtimizacao):
        texto = ViewExercicio5.retornarTextoDoResumo(
            ConstantesExercicio5.NOME_DO_METODO_NEWTON,
            funcaoQuadratica,
            resultadoOtimizacao
        )

        if(texto is None):
            return False

        graficoDaFuncaoObjetivoFoiSalvo = ViewExercicio5.salvarGraficoDeValores(
            resultadoOtimizacao.getListaDaFuncaoObjetivo(),
            ConstantesExercicio5.TITULO_DO_GRAFICO_DA_FUNCAO_OBJETIVO_DO_NEWTON,
            ConstantesExercicio5.TEXTO_DO_EIXO_DA_FUNCAO_OBJETIVO,
            ConstantesExercicio5.CAMINHO_DO_GRAFICO_DA_FUNCAO_OBJETIVO_DO_NEWTON
        )

        graficoDaNormaDoGradienteFoiSalvo = ViewExercicio5.salvarGraficoDeValores(
            resultadoOtimizacao.getListaDaNormaDoGradiente(),
            ConstantesExercicio5.TITULO_DO_GRAFICO_DA_NORMA_DO_GRADIENTE_DO_NEWTON,
            ConstantesExercicio5.TEXTO_DO_EIXO_DA_NORMA_DO_GRADIENTE,
            ConstantesExercicio5.CAMINHO_DO_GRAFICO_DA_NORMA_DO_GRADIENTE_DO_NEWTON
        )

        graficoDasCoordenadasFoiSalvo = ViewExercicio5.salvarGraficoDasCoordenadas(
            resultadoOtimizacao.getListaDePontos(),
            ConstantesExercicio5.TITULO_DO_GRAFICO_DAS_COORDENADAS_DO_NEWTON,
            ConstantesExercicio5.CAMINHO_DO_GRAFICO_DAS_COORDENADAS_DO_NEWTON
        )

        textoFoiSalvo = ViewExercicio5.salvarTexto(
            texto,
            ConstantesExercicio5.CAMINHO_DO_ARQUIVO_DO_RESULTADO_DO_NEWTON
        )

        textoFoiApresentado = ViewExercicio5.apresentarTexto(texto)

        return graficoDaFuncaoObjetivoFoiSalvo and graficoDaNormaDoGradienteFoiSalvo and graficoDasCoordenadasFoiSalvo and textoFoiSalvo and textoFoiApresentado

    @staticmethod
    def salvarComparacao(resultadoDoSteepestDescent, resultadoDoNewton):
        if(resultadoDoSteepestDescent is None):
            return False

        elif(resultadoDoNewton is None):
            return False

        texto = "Exercício 5 - Comparação" + ConstantesExercicio5.QUEBRA_DE_LINHA
        texto = texto + ConstantesExercicio5.QUEBRA_DE_LINHA

        texto = texto + "Iterações do Steepest Descent = " + str(resultadoDoSteepestDescent.getQuantidadeDeIteracoes()) + ConstantesExercicio5.QUEBRA_DE_LINHA
        texto = texto + "Iterações do Newton = " + str(resultadoDoNewton.getQuantidadeDeIteracoes()) + ConstantesExercicio5.QUEBRA_DE_LINHA
        texto = texto + "Tempo do Steepest Descent = " + str(resultadoDoSteepestDescent.getTempoComputacional()) + ConstantesExercicio5.QUEBRA_DE_LINHA
        texto = texto + "Tempo do Newton = " + str(resultadoDoNewton.getTempoComputacional()) + ConstantesExercicio5.QUEBRA_DE_LINHA
        texto = texto + "Função objetivo final do Steepest Descent = " + str(resultadoDoSteepestDescent.getListaDaFuncaoObjetivo()[-ConstantesExercicio5.INCREMENTO_UNITARIO]) + ConstantesExercicio5.QUEBRA_DE_LINHA
        texto = texto + "Função objetivo final do Newton = " + str(resultadoDoNewton.getListaDaFuncaoObjetivo()[-ConstantesExercicio5.INCREMENTO_UNITARIO]) + ConstantesExercicio5.QUEBRA_DE_LINHA
        texto = texto + ConstantesExercicio5.QUEBRA_DE_LINHA

        texto = texto + "O Steepest Descent utiliza somente o gradiente e tende a alternar direções nas regiões alongadas das curvas de nível." + ConstantesExercicio5.QUEBRA_DE_LINHA
        texto = texto + "O método de Newton incorpora a Hessiana e corrige a escala e o acoplamento entre as variáveis." + ConstantesExercicio5.QUEBRA_DE_LINHA
        texto = texto + "Para uma função quadrática com Hessiana constante e positiva definida, Newton alcança o ponto ótimo em uma única atualização, desconsiderando erros numéricos." + ConstantesExercicio5.QUEBRA_DE_LINHA

        graficoDaFuncaoObjetivoFoiSalvo = ViewExercicio5.salvarGraficoComparativo(
            resultadoDoSteepestDescent.getListaDaFuncaoObjetivo(),
            resultadoDoNewton.getListaDaFuncaoObjetivo(),
            ConstantesExercicio5.TITULO_DO_GRAFICO_COMPARATIVO_DA_FUNCAO_OBJETIVO,
            ConstantesExercicio5.TEXTO_DO_EIXO_DA_FUNCAO_OBJETIVO,
            ConstantesExercicio5.CAMINHO_DO_GRAFICO_COMPARATIVO_DA_FUNCAO_OBJETIVO
        )

        graficoDaNormaDoGradienteFoiSalvo = ViewExercicio5.salvarGraficoComparativo(
            resultadoDoSteepestDescent.getListaDaNormaDoGradiente(),
            resultadoDoNewton.getListaDaNormaDoGradiente(),
            ConstantesExercicio5.TITULO_DO_GRAFICO_COMPARATIVO_DA_NORMA_DO_GRADIENTE,
            ConstantesExercicio5.TEXTO_DO_EIXO_DA_NORMA_DO_GRADIENTE,
            ConstantesExercicio5.CAMINHO_DO_GRAFICO_COMPARATIVO_DA_NORMA_DO_GRADIENTE
        )

        textoFoiSalvo = ViewExercicio5.salvarTexto(
            texto,
            ConstantesExercicio5.CAMINHO_DO_ARQUIVO_DA_COMPARACAO
        )

        textoFoiApresentado = ViewExercicio5.apresentarTexto(texto)

        return graficoDaFuncaoObjetivoFoiSalvo and graficoDaNormaDoGradienteFoiSalvo and textoFoiSalvo and textoFoiApresentado