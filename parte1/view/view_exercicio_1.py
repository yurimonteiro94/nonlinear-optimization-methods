import os

import matplotlib.pyplot as plt

from services.constantes import Constantes


class ViewExercicio1:

    @staticmethod
    def apresentarMensagem(mensagem):
        if(mensagem is None):
            return False

        print(mensagem)

        return True

    @staticmethod
    def salvarGrafico(listaDeValores, titulo, textoDoEixoX, textoDoEixoY, caminhoDoArquivo):
        if(listaDeValores is None):
            return False

        elif(titulo is None):
            return False

        elif(textoDoEixoX is None):
            return False

        elif(textoDoEixoY is None):
            return False

        elif(caminhoDoArquivo is None):
            return False

        elif(len(listaDeValores) == Constantes.QUANTIDADE_NULA):
            return False

        try:
            pastaDoArquivo = os.path.dirname(caminhoDoArquivo)

            if(not os.path.exists(pastaDoArquivo)):
                os.makedirs(pastaDoArquivo)

            listaDeIteracoes = []
            indice = Constantes.INDICE_INICIAL
            quantidadeDeValores = len(listaDeValores)

            while(indice < quantidadeDeValores):
                listaDeIteracoes.append(indice)
                indice = indice + Constantes.INCREMENTO_UNITARIO

            plt.figure()
            plt.plot(listaDeIteracoes, listaDeValores)
            plt.title(titulo)
            plt.xlabel(textoDoEixoX)
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
    def salvarGraficos(resultadoDoTreinamento):
        if(resultadoDoTreinamento is None):
            return False

        graficoDaFuncaoObjetivoFoiSalvo = ViewExercicio1.salvarGrafico(resultadoDoTreinamento.getListaDaFuncaoObjetivo(), Constantes.TITULO_DO_GRAFICO_DA_FUNCAO_OBJETIVO, Constantes.TEXTO_DO_EIXO_DAS_ITERACOES, Constantes.TEXTO_DO_EIXO_DA_FUNCAO_OBJETIVO, Constantes.CAMINHO_DO_GRAFICO_DA_FUNCAO_OBJETIVO)

        graficoDaNormaDoGradienteFoiSalvo = ViewExercicio1.salvarGrafico(resultadoDoTreinamento.getListaDaNormaDoGradiente(), Constantes.TITULO_DO_GRAFICO_DA_NORMA_DO_GRADIENTE, Constantes.TEXTO_DO_EIXO_DAS_ITERACOES, Constantes.TEXTO_DO_EIXO_DA_NORMA_DO_GRADIENTE, Constantes.CAMINHO_DO_GRAFICO_DA_NORMA_DO_GRADIENTE)

        graficoDaAcuraciaFoiSalvo = ViewExercicio1.salvarGrafico(resultadoDoTreinamento.getListaDaAcuracia(), Constantes.TITULO_DO_GRAFICO_DA_ACURACIA, Constantes.TEXTO_DO_EIXO_DAS_ITERACOES, Constantes.TEXTO_DO_EIXO_DA_ACURACIA, Constantes.CAMINHO_DO_GRAFICO_DA_ACURACIA)

        if(not graficoDaFuncaoObjetivoFoiSalvo):
            return False

        elif(not graficoDaNormaDoGradienteFoiSalvo):
            return False

        elif(not graficoDaAcuraciaFoiSalvo):
            return False

        return True

    @staticmethod
    def retornarTextoDoResumo(resultadoDoTreinamento, acuraciaDeTeste, configuracaoDoTreinamento):
        if(resultadoDoTreinamento is None):
            return None

        elif(acuraciaDeTeste is None):
            return None

        elif(configuracaoDoTreinamento is None):
            return None

        listaDaFuncaoObjetivo = resultadoDoTreinamento.getListaDaFuncaoObjetivo()
        listaDaNormaDoGradiente = resultadoDoTreinamento.getListaDaNormaDoGradiente()

        if(listaDaFuncaoObjetivo is None):
            return None

        elif(listaDaNormaDoGradiente is None):
            return None

        elif(len(listaDaFuncaoObjetivo) == Constantes.QUANTIDADE_NULA):
            return None

        elif(len(listaDaNormaDoGradiente) == Constantes.QUANTIDADE_NULA):
            return None

        funcaoObjetivoInicial = listaDaFuncaoObjetivo[Constantes.INDICE_INICIAL]
        funcaoObjetivoFinal = listaDaFuncaoObjetivo[-Constantes.INCREMENTO_UNITARIO]
        normaDoGradienteInicial = listaDaNormaDoGradiente[Constantes.INDICE_INICIAL]
        normaDoGradienteFinal = listaDaNormaDoGradiente[-Constantes.INCREMENTO_UNITARIO]

        texto = "Exercício 1 - Steepest Descent\n"
        texto = texto + "\n"
        texto = texto + "Learning rate = " + str(configuracaoDoTreinamento.getLearningRate()) + "\n"
        texto = texto + "Tolerância = " + str(configuracaoDoTreinamento.getTolerancia()) + "\n"
        texto = texto + "Número máximo de iterações = " + str(configuracaoDoTreinamento.getNumeroMaximoDeIteracoes()) + "\n"
        texto = texto + "Quantidade de iterações executadas = " + str(resultadoDoTreinamento.getQuantidadeDeIteracoes()) + "\n"
        texto = texto + "Motivo da parada = " + resultadoDoTreinamento.getMotivoDaParada() + "\n"
        texto = texto + "Função objetivo inicial = " + str(funcaoObjetivoInicial) + "\n"
        texto = texto + "Função objetivo final = " + str(funcaoObjetivoFinal) + "\n"
        texto = texto + "Norma inicial do gradiente = " + str(normaDoGradienteInicial) + "\n"
        texto = texto + "Norma final do gradiente = " + str(normaDoGradienteFinal) + "\n"
        texto = texto + "Acurácia de treinamento = " + str(resultadoDoTreinamento.getAcuracia()) + "\n"
        texto = texto + "Acurácia de teste = " + str(acuraciaDeTeste) + "\n"
        texto = texto + "Tempo computacional em segundos = " + str(resultadoDoTreinamento.getTempoComputacional()) + "\n"

        return texto

    @staticmethod
    def salvarResumo(resultadoDoTreinamento, acuraciaDeTeste, configuracaoDoTreinamento):
        textoDoResumo = ViewExercicio1.retornarTextoDoResumo(resultadoDoTreinamento, acuraciaDeTeste, configuracaoDoTreinamento)

        if(textoDoResumo is None):
            return False

        try:
            if(not os.path.exists(Constantes.PASTA_DOS_RESULTADOS)):
                os.makedirs(Constantes.PASTA_DOS_RESULTADOS)

            arquivo = open(Constantes.CAMINHO_DO_ARQUIVO_DE_RESULTADOS_DO_EXERCICIO_1, Constantes.MODO_DE_ESCRITA, encoding=Constantes.CODIFICACAO_DOS_ARQUIVOS_DE_SAIDA)
            arquivo.write(textoDoResumo)
            arquivo.close()

            return True

        except Exception:
            return False

    @staticmethod
    def apresentarResumo(resultadoDoTreinamento, acuraciaDeTeste, configuracaoDoTreinamento):
        textoDoResumo = ViewExercicio1.retornarTextoDoResumo(resultadoDoTreinamento, acuraciaDeTeste, configuracaoDoTreinamento)

        if(textoDoResumo is None):
            return False

        print(textoDoResumo)

        return True