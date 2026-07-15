import os

import matplotlib.pyplot as plt

from services.constantes import Constantes


class ViewComparacaoParte1:

    @staticmethod
    def retornarTextoDaLinhaCsv(linhaDoResultado):
        if(linhaDoResultado is None):
            return None

        texto = str(linhaDoResultado[Constantes.INDICE_DO_NOME_DO_METODO_NO_RESULTADO])
        texto = texto + Constantes.DELIMITADOR_CSV + str(linhaDoResultado[Constantes.INDICE_DO_LEARNING_RATE_NO_RESULTADO])
        texto = texto + Constantes.DELIMITADOR_CSV + str(linhaDoResultado[Constantes.INDICE_DO_MINI_BATCH_NO_RESULTADO])
        texto = texto + Constantes.DELIMITADOR_CSV + str(linhaDoResultado[Constantes.INDICE_DO_BETA_NO_RESULTADO])
        texto = texto + Constantes.DELIMITADOR_CSV + str(linhaDoResultado[Constantes.INDICE_DAS_ITERACOES_NO_RESULTADO])
        texto = texto + Constantes.DELIMITADOR_CSV + str(linhaDoResultado[Constantes.INDICE_DO_TEMPO_NO_RESULTADO])
        texto = texto + Constantes.DELIMITADOR_CSV + str(linhaDoResultado[Constantes.INDICE_DA_FUNCAO_OBJETIVO_FINAL_NO_RESULTADO])
        texto = texto + Constantes.DELIMITADOR_CSV + str(linhaDoResultado[Constantes.INDICE_DA_ACURACIA_DE_TREINAMENTO_NO_RESULTADO])
        texto = texto + Constantes.DELIMITADOR_CSV + str(linhaDoResultado[Constantes.INDICE_DA_ACURACIA_DE_TESTE_NO_RESULTADO])

        return texto

    @staticmethod
    def salvarTabela(listaDeResultados, caminhoDoArquivo):
        if(listaDeResultados is None):
            return False

        elif(caminhoDoArquivo is None):
            return False

        elif(len(listaDeResultados) == Constantes.QUANTIDADE_NULA):
            return False

        try:
            if(not os.path.exists(Constantes.PASTA_DOS_RESULTADOS)):
                os.makedirs(Constantes.PASTA_DOS_RESULTADOS)

            arquivo = open(caminhoDoArquivo, Constantes.MODO_DE_ESCRITA, encoding=Constantes.CODIFICACAO_DOS_ARQUIVOS_DE_SAIDA)
            arquivo.write(Constantes.CABECALHO_DA_TABELA_COMPARATIVA + Constantes.QUEBRA_DE_LINHA)

            indiceDoResultado = Constantes.INDICE_INICIAL
            quantidadeDeResultados = len(listaDeResultados)

            while(indiceDoResultado < quantidadeDeResultados):
                textoDaLinha = ViewComparacaoParte1.retornarTextoDaLinhaCsv(listaDeResultados[indiceDoResultado])

                if(textoDaLinha is None):
                    arquivo.close()
                    return False

                arquivo.write(textoDaLinha + Constantes.QUEBRA_DE_LINHA)
                indiceDoResultado = indiceDoResultado + Constantes.INCREMENTO_UNITARIO

            arquivo.close()

            return True

        except Exception:
            return False

    @staticmethod
    def salvarGraficoDeCurvas(listaDeResultados, titulo, textoDoEixoX, textoDoEixoY, caminhoDoArquivo, usarAcuracia):
        if(listaDeResultados is None):
            return False

        elif(titulo is None):
            return False

        elif(caminhoDoArquivo is None):
            return False

        elif(len(listaDeResultados) == Constantes.QUANTIDADE_NULA):
            return False

        try:
            if(not os.path.exists(Constantes.PASTA_DOS_GRAFICOS)):
                os.makedirs(Constantes.PASTA_DOS_GRAFICOS)

            plt.figure()

            indiceDoResultado = Constantes.INDICE_INICIAL
            quantidadeDeResultados = len(listaDeResultados)

            while(indiceDoResultado < quantidadeDeResultados):
                linhaDoResultado = listaDeResultados[indiceDoResultado]
                resultadoDoTreinamento = linhaDoResultado[Constantes.INDICE_DO_RESULTADO_DO_TREINAMENTO]

                if(usarAcuracia):
                    listaDeValores = resultadoDoTreinamento.getListaDaAcuracia()
                else:
                    listaDeValores = resultadoDoTreinamento.getListaDaFuncaoObjetivo()

                nomeDaCurva = str(linhaDoResultado[Constantes.INDICE_DO_NOME_DO_METODO_NO_RESULTADO])

                if(linhaDoResultado[Constantes.INDICE_DO_NOME_DO_METODO_NO_RESULTADO] == Constantes.NOME_DO_METODO_STEEPEST_DESCENT):
                    nomeDaCurva = nomeDaCurva + " - lr " + str(linhaDoResultado[Constantes.INDICE_DO_LEARNING_RATE_NO_RESULTADO])

                elif(linhaDoResultado[Constantes.INDICE_DO_NOME_DO_METODO_NO_RESULTADO] == Constantes.NOME_DO_METODO_SGD):
                    nomeDaCurva = nomeDaCurva + " - batch " + str(linhaDoResultado[Constantes.INDICE_DO_MINI_BATCH_NO_RESULTADO])

                else:
                    nomeDaCurva = nomeDaCurva + " - beta " + str(linhaDoResultado[Constantes.INDICE_DO_BETA_NO_RESULTADO])

                plt.plot(listaDeValores, label=nomeDaCurva)
                indiceDoResultado = indiceDoResultado + Constantes.INCREMENTO_UNITARIO

            plt.title(titulo)
            plt.xlabel(textoDoEixoX)
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
    def retornarTextoDoResumo(listaDaComparacaoDosMetodos):
        if(listaDaComparacaoDosMetodos is None):
            return None

        elif(len(listaDaComparacaoDosMetodos) == Constantes.QUANTIDADE_NULA):
            return None

        texto = "Resumo da Parte 1" + Constantes.QUEBRA_DE_LINHA
        texto = texto + Constantes.QUEBRA_DE_LINHA

        indiceDoResultado = Constantes.INDICE_INICIAL
        quantidadeDeResultados = len(listaDaComparacaoDosMetodos)

        melhorAcuraciaDeTeste = -1.0
        menorTempo = None
        nomeDoMetodoComMelhorAcuracia = Constantes.TEXTO_VAZIO
        nomeDoMetodoMaisRapido = Constantes.TEXTO_VAZIO

        while(indiceDoResultado < quantidadeDeResultados):
            linhaDoResultado = listaDaComparacaoDosMetodos[indiceDoResultado]
            nomeDoMetodo = linhaDoResultado[Constantes.INDICE_DO_NOME_DO_METODO_NO_RESULTADO]
            acuraciaDeTeste = linhaDoResultado[Constantes.INDICE_DA_ACURACIA_DE_TESTE_NO_RESULTADO]
            tempo = linhaDoResultado[Constantes.INDICE_DO_TEMPO_NO_RESULTADO]

            texto = texto + "Método = " + str(nomeDoMetodo) + Constantes.QUEBRA_DE_LINHA
            texto = texto + "Iterações ou épocas = " + str(linhaDoResultado[Constantes.INDICE_DAS_ITERACOES_NO_RESULTADO]) + Constantes.QUEBRA_DE_LINHA
            texto = texto + "Tempo = " + str(tempo) + Constantes.QUEBRA_DE_LINHA
            texto = texto + "Função objetivo final = " + str(linhaDoResultado[Constantes.INDICE_DA_FUNCAO_OBJETIVO_FINAL_NO_RESULTADO]) + Constantes.QUEBRA_DE_LINHA
            texto = texto + "Acurácia de treinamento = " + str(linhaDoResultado[Constantes.INDICE_DA_ACURACIA_DE_TREINAMENTO_NO_RESULTADO]) + Constantes.QUEBRA_DE_LINHA
            texto = texto + "Acurácia de teste = " + str(acuraciaDeTeste) + Constantes.QUEBRA_DE_LINHA
            texto = texto + Constantes.QUEBRA_DE_LINHA

            if(acuraciaDeTeste > melhorAcuraciaDeTeste):
                melhorAcuraciaDeTeste = acuraciaDeTeste
                nomeDoMetodoComMelhorAcuracia = nomeDoMetodo

            if((menorTempo is None) or (tempo < menorTempo)):
                menorTempo = tempo
                nomeDoMetodoMaisRapido = nomeDoMetodo

            indiceDoResultado = indiceDoResultado + Constantes.INCREMENTO_UNITARIO

        texto = texto + "Método com maior acurácia de teste = " + str(nomeDoMetodoComMelhorAcuracia) + Constantes.QUEBRA_DE_LINHA
        texto = texto + "Maior acurácia de teste = " + str(melhorAcuraciaDeTeste) + Constantes.QUEBRA_DE_LINHA
        texto = texto + "Método com menor tempo computacional = " + str(nomeDoMetodoMaisRapido) + Constantes.QUEBRA_DE_LINHA
        texto = texto + "Menor tempo computacional = " + str(menorTempo) + Constantes.QUEBRA_DE_LINHA

        return texto

    @staticmethod
    def salvarResumo(listaDaComparacaoDosMetodos):
        texto = ViewComparacaoParte1.retornarTextoDoResumo(listaDaComparacaoDosMetodos)

        if(texto is None):
            return False

        try:
            arquivo = open(Constantes.CAMINHO_DO_ARQUIVO_DO_RESUMO_DA_PARTE_1, Constantes.MODO_DE_ESCRITA, encoding=Constantes.CODIFICACAO_DOS_ARQUIVOS_DE_SAIDA)
            arquivo.write(texto)
            arquivo.close()

            return True

        except Exception:
            return False

    @staticmethod
    def apresentarResumo(listaDaComparacaoDosMetodos):
        texto = ViewComparacaoParte1.retornarTextoDoResumo(listaDaComparacaoDosMetodos)

        if(texto is None):
            return False

        print(texto)

        return True

    @staticmethod
    def salvarTodosOsResultados(listaDeExperimentos):
        if(listaDeExperimentos is None):
            return False

        listaDaComparacaoDosMetodos = listaDeExperimentos[0]
        listaDosLearningRates = listaDeExperimentos[1]
        listaDosMiniBatches = listaDeExperimentos[2]
        listaDosBetasDoMomentum = listaDeExperimentos[3]
        listaDosBetasDoNesterov = listaDeExperimentos[4]

        tabelaComparativaFoiSalva = ViewComparacaoParte1.salvarTabela(listaDaComparacaoDosMetodos, Constantes.CAMINHO_DO_ARQUIVO_DA_TABELA_COMPARATIVA)
        tabelaDeLearningRatesFoiSalva = ViewComparacaoParte1.salvarTabela(listaDosLearningRates, Constantes.CAMINHO_DO_ARQUIVO_DA_TABELA_DE_LEARNING_RATES)
        tabelaDeMiniBatchesFoiSalva = ViewComparacaoParte1.salvarTabela(listaDosMiniBatches, Constantes.CAMINHO_DO_ARQUIVO_DA_TABELA_DE_MINI_BATCHES)

        listaDeResultadosDosBetas = []
        listaDeResultadosDosBetas.extend(listaDosBetasDoMomentum)
        listaDeResultadosDosBetas.extend(listaDosBetasDoNesterov)

        tabelaDeBetasFoiSalva = ViewComparacaoParte1.salvarTabela(listaDeResultadosDosBetas, Constantes.CAMINHO_DO_ARQUIVO_DA_TABELA_DE_BETAS)

        graficoComparativoDaFuncaoObjetivoFoiSalvo = ViewComparacaoParte1.salvarGraficoDeCurvas(listaDaComparacaoDosMetodos, Constantes.TITULO_DO_GRAFICO_COMPARATIVO_DA_FUNCAO_OBJETIVO, Constantes.TEXTO_DO_EIXO_DAS_ITERACOES, Constantes.TEXTO_DO_EIXO_DA_FUNCAO_OBJETIVO, Constantes.CAMINHO_DO_GRAFICO_COMPARATIVO_DA_FUNCAO_OBJETIVO, False)

        graficoComparativoDaAcuraciaFoiSalvo = ViewComparacaoParte1.salvarGraficoDeCurvas(listaDaComparacaoDosMetodos, Constantes.TITULO_DO_GRAFICO_COMPARATIVO_DA_ACURACIA, Constantes.TEXTO_DO_EIXO_DAS_ITERACOES, Constantes.TEXTO_DO_EIXO_DA_ACURACIA, Constantes.CAMINHO_DO_GRAFICO_COMPARATIVO_DA_ACURACIA, True)

        graficoDosLearningRatesFoiSalvo = ViewComparacaoParte1.salvarGraficoDeCurvas(listaDosLearningRates, Constantes.TITULO_DO_GRAFICO_DOS_LEARNING_RATES, Constantes.TEXTO_DO_EIXO_DAS_ITERACOES, Constantes.TEXTO_DO_EIXO_DA_FUNCAO_OBJETIVO, Constantes.CAMINHO_DO_GRAFICO_DOS_LEARNING_RATES, False)

        graficoDosMiniBatchesFoiSalvo = ViewComparacaoParte1.salvarGraficoDeCurvas(listaDosMiniBatches, Constantes.TITULO_DO_GRAFICO_DOS_MINI_BATCHES, Constantes.TEXTO_DO_EIXO_DAS_EPOCAS, Constantes.TEXTO_DO_EIXO_DA_FUNCAO_OBJETIVO, Constantes.CAMINHO_DO_GRAFICO_DOS_MINI_BATCHES, False)

        graficoDosBetasDoMomentumFoiSalvo = ViewComparacaoParte1.salvarGraficoDeCurvas(listaDosBetasDoMomentum, Constantes.TITULO_DO_GRAFICO_DOS_BETAS_DO_MOMENTUM, Constantes.TEXTO_DO_EIXO_DAS_ITERACOES, Constantes.TEXTO_DO_EIXO_DA_FUNCAO_OBJETIVO, Constantes.CAMINHO_DO_GRAFICO_DOS_BETAS_DO_MOMENTUM, False)

        graficoDosBetasDoNesterovFoiSalvo = ViewComparacaoParte1.salvarGraficoDeCurvas(listaDosBetasDoNesterov, Constantes.TITULO_DO_GRAFICO_DOS_BETAS_DO_NESTEROV, Constantes.TEXTO_DO_EIXO_DAS_ITERACOES, Constantes.TEXTO_DO_EIXO_DA_FUNCAO_OBJETIVO, Constantes.CAMINHO_DO_GRAFICO_DOS_BETAS_DO_NESTEROV, False)

        resumoFoiSalvo = ViewComparacaoParte1.salvarResumo(listaDaComparacaoDosMetodos)
        resumoFoiApresentado = ViewComparacaoParte1.apresentarResumo(listaDaComparacaoDosMetodos)

        return tabelaComparativaFoiSalva and tabelaDeLearningRatesFoiSalva and tabelaDeMiniBatchesFoiSalva and tabelaDeBetasFoiSalva and graficoComparativoDaFuncaoObjetivoFoiSalvo and graficoComparativoDaAcuraciaFoiSalvo and graficoDosLearningRatesFoiSalvo and graficoDosMiniBatchesFoiSalvo and graficoDosBetasDoMomentumFoiSalvo and graficoDosBetasDoNesterovFoiSalvo and resumoFoiSalvo and resumoFoiApresentado