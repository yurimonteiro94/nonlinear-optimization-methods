import os

from services.constantes import Constantes
from view.view_exercicio_1 import ViewExercicio1


class ViewExercicio2:

    @staticmethod
    def salvarGraficos(resultadoDoTreinamento):
        if(resultadoDoTreinamento is None):
            return False

        graficoDaFuncaoObjetivoFoiSalvo = ViewExercicio1.salvarGrafico(resultadoDoTreinamento.getListaDaFuncaoObjetivo(), Constantes.TITULO_DO_GRAFICO_DA_FUNCAO_OBJETIVO_DO_SGD, Constantes.TEXTO_DO_EIXO_DAS_ITERACOES, Constantes.TEXTO_DO_EIXO_DA_FUNCAO_OBJETIVO, Constantes.CAMINHO_DO_GRAFICO_DA_FUNCAO_OBJETIVO_DO_SGD)

        graficoDaAcuraciaFoiSalvo = ViewExercicio1.salvarGrafico(resultadoDoTreinamento.getListaDaAcuracia(), Constantes.TITULO_DO_GRAFICO_DA_ACURACIA_DO_SGD, Constantes.TEXTO_DO_EIXO_DAS_ITERACOES, Constantes.TEXTO_DO_EIXO_DA_ACURACIA, Constantes.CAMINHO_DO_GRAFICO_DA_ACURACIA_DO_SGD)

        if(not graficoDaFuncaoObjetivoFoiSalvo):
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

        if(listaDaFuncaoObjetivo is None):
            return None

        elif(len(listaDaFuncaoObjetivo) == Constantes.QUANTIDADE_NULA):
            return None

        texto = "Exercício 2 - Stochastic Gradient Descent\n"
        texto = texto + "\n"
        texto = texto + "Learning rate = " + str(configuracaoDoTreinamento.getLearningRate()) + "\n"
        texto = texto + "Tamanho do mini-batch = " + str(configuracaoDoTreinamento.getTamanhoDoMiniBatch()) + "\n"
        texto = texto + "Tolerância = " + str(configuracaoDoTreinamento.getTolerancia()) + "\n"
        texto = texto + "Número máximo de épocas = " + str(configuracaoDoTreinamento.getNumeroMaximoDeIteracoes()) + "\n"
        texto = texto + "Quantidade de épocas executadas = " + str(resultadoDoTreinamento.getQuantidadeDeIteracoes()) + "\n"
        texto = texto + "Motivo da parada = " + resultadoDoTreinamento.getMotivoDaParada() + "\n"
        texto = texto + "Função objetivo inicial = " + str(listaDaFuncaoObjetivo[Constantes.INDICE_INICIAL]) + "\n"
        texto = texto + "Função objetivo final = " + str(listaDaFuncaoObjetivo[-Constantes.INCREMENTO_UNITARIO]) + "\n"
        texto = texto + "Acurácia de treinamento = " + str(resultadoDoTreinamento.getAcuracia()) + "\n"
        texto = texto + "Acurácia de teste = " + str(acuraciaDeTeste) + "\n"
        texto = texto + "Tempo computacional em segundos = " + str(resultadoDoTreinamento.getTempoComputacional()) + "\n"

        return texto

    @staticmethod
    def salvarResumo(resultadoDoTreinamento, acuraciaDeTeste, configuracaoDoTreinamento):
        textoDoResumo = ViewExercicio2.retornarTextoDoResumo(resultadoDoTreinamento, acuraciaDeTeste, configuracaoDoTreinamento)

        if(textoDoResumo is None):
            return False

        try:
            if(not os.path.exists(Constantes.PASTA_DOS_RESULTADOS)):
                os.makedirs(Constantes.PASTA_DOS_RESULTADOS)

            arquivo = open(Constantes.CAMINHO_DO_ARQUIVO_DE_RESULTADOS_DO_EXERCICIO_2, Constantes.MODO_DE_ESCRITA, encoding=Constantes.CODIFICACAO_DOS_ARQUIVOS_DE_SAIDA)
            arquivo.write(textoDoResumo)
            arquivo.close()

            return True

        except Exception:
            return False

    @staticmethod
    def apresentarResumo(resultadoDoTreinamento, acuraciaDeTeste, configuracaoDoTreinamento):
        textoDoResumo = ViewExercicio2.retornarTextoDoResumo(resultadoDoTreinamento, acuraciaDeTeste, configuracaoDoTreinamento)

        if(textoDoResumo is None):
            return False

        print(textoDoResumo)

        return True