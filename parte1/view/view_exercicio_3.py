import os

from services.constantes import Constantes
from view.view_exercicio_1 import ViewExercicio1


class ViewExercicio3:

    @staticmethod
    def salvarGraficos(resultadoDoTreinamento):
        if(resultadoDoTreinamento is None):
            return False

        graficoDaFuncaoObjetivoFoiSalvo = ViewExercicio1.salvarGrafico(resultadoDoTreinamento.getListaDaFuncaoObjetivo(), Constantes.TITULO_DO_GRAFICO_DA_FUNCAO_OBJETIVO_DO_MOMENTUM, Constantes.TEXTO_DO_EIXO_DAS_ITERACOES, Constantes.TEXTO_DO_EIXO_DA_FUNCAO_OBJETIVO, Constantes.CAMINHO_DO_GRAFICO_DA_FUNCAO_OBJETIVO_DO_MOMENTUM)

        graficoDaNormaDoGradienteFoiSalvo = ViewExercicio1.salvarGrafico(resultadoDoTreinamento.getListaDaNormaDoGradiente(), Constantes.TITULO_DO_GRAFICO_DA_NORMA_DO_GRADIENTE_DO_MOMENTUM, Constantes.TEXTO_DO_EIXO_DAS_ITERACOES, Constantes.TEXTO_DO_EIXO_DA_NORMA_DO_GRADIENTE, Constantes.CAMINHO_DO_GRAFICO_DA_NORMA_DO_GRADIENTE_DO_MOMENTUM)

        graficoDaAcuraciaFoiSalvo = ViewExercicio1.salvarGrafico(resultadoDoTreinamento.getListaDaAcuracia(), Constantes.TITULO_DO_GRAFICO_DA_ACURACIA_DO_MOMENTUM, Constantes.TEXTO_DO_EIXO_DAS_ITERACOES, Constantes.TEXTO_DO_EIXO_DA_ACURACIA, Constantes.CAMINHO_DO_GRAFICO_DA_ACURACIA_DO_MOMENTUM)

        return graficoDaFuncaoObjetivoFoiSalvo and graficoDaNormaDoGradienteFoiSalvo and graficoDaAcuraciaFoiSalvo

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

        texto = "Exercício 3 - Momentum\n"
        texto = texto + "\n"
        texto = texto + "Learning rate = " + str(configuracaoDoTreinamento.getLearningRate()) + "\n"
        texto = texto + "Beta = " + str(configuracaoDoTreinamento.getBeta()) + "\n"
        texto = texto + "Tolerância = " + str(configuracaoDoTreinamento.getTolerancia()) + "\n"
        texto = texto + "Quantidade de iterações = " + str(resultadoDoTreinamento.getQuantidadeDeIteracoes()) + "\n"
        texto = texto + "Motivo da parada = " + resultadoDoTreinamento.getMotivoDaParada() + "\n"
        texto = texto + "Função objetivo inicial = " + str(listaDaFuncaoObjetivo[Constantes.INDICE_INICIAL]) + "\n"
        texto = texto + "Função objetivo final = " + str(listaDaFuncaoObjetivo[-Constantes.INCREMENTO_UNITARIO]) + "\n"
        texto = texto + "Acurácia de treinamento = " + str(resultadoDoTreinamento.getAcuracia()) + "\n"
        texto = texto + "Acurácia de teste = " + str(acuraciaDeTeste) + "\n"
        texto = texto + "Tempo computacional em segundos = " + str(resultadoDoTreinamento.getTempoComputacional()) + "\n"

        return texto

    @staticmethod
    def salvarResumo(resultadoDoTreinamento, acuraciaDeTeste, configuracaoDoTreinamento):
        texto = ViewExercicio3.retornarTextoDoResumo(resultadoDoTreinamento, acuraciaDeTeste, configuracaoDoTreinamento)

        if(texto is None):
            return False

        try:
            if(not os.path.exists(Constantes.PASTA_DOS_RESULTADOS)):
                os.makedirs(Constantes.PASTA_DOS_RESULTADOS)

            arquivo = open(Constantes.CAMINHO_DO_ARQUIVO_DE_RESULTADOS_DO_EXERCICIO_3, Constantes.MODO_DE_ESCRITA, encoding=Constantes.CODIFICACAO_DOS_ARQUIVOS_DE_SAIDA)
            arquivo.write(texto)
            arquivo.close()

            return True

        except Exception:
            return False

    @staticmethod
    def apresentarResumo(resultadoDoTreinamento, acuraciaDeTeste, configuracaoDoTreinamento):
        texto = ViewExercicio3.retornarTextoDoResumo(resultadoDoTreinamento, acuraciaDeTeste, configuracaoDoTreinamento)

        if(texto is None):
            return False

        print(texto)

        return True