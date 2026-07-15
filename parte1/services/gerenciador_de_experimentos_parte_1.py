from model.entidades.configuracao_do_treinamento import ConfiguracaoDoTreinamento
from model.entidades.modelo_logistico import ModeloLogistico
from services.constantes import Constantes
from services.gerenciador_de_regressao_logistica import GerenciadorDeRegressaoLogistica
from services.gerenciador_momentum import GerenciadorMomentum
from services.gerenciador_nesterov import GerenciadorNesterov
from services.gerenciador_sgd import GerenciadorSGD
from services.gerenciador_steepest_descent import GerenciadorSteepestDescent


class GerenciadorDeExperimentosParte1:

    @staticmethod
    def retornarModeloInicial(quantidadeDePesos):
        if(quantidadeDePesos <= Constantes.QUANTIDADE_NULA):
            return None

        listaDePesos = []
        indiceDoPeso = Constantes.INDICE_INICIAL

        while(indiceDoPeso < quantidadeDePesos):
            listaDePesos.append(Constantes.VALOR_INICIAL_DOS_PARAMETROS)
            indiceDoPeso = indiceDoPeso + Constantes.INCREMENTO_UNITARIO

        return ModeloLogistico(listaDePesos, Constantes.VALOR_INICIAL_DOS_PARAMETROS)

    @staticmethod
    def retornarLinhaDoResultado(nomeDoMetodo, learningRate, tamanhoDoMiniBatch, beta, resultadoDoTreinamento, acuraciaDeTeste):
        if(nomeDoMetodo is None):
            return None

        elif(resultadoDoTreinamento is None):
            return None

        elif(acuraciaDeTeste is None):
            return None

        listaDaFuncaoObjetivo = resultadoDoTreinamento.getListaDaFuncaoObjetivo()

        if(listaDaFuncaoObjetivo is None):
            return None

        elif(len(listaDaFuncaoObjetivo) == Constantes.QUANTIDADE_NULA):
            return None

        funcaoObjetivoFinal = listaDaFuncaoObjetivo[-Constantes.INCREMENTO_UNITARIO]

        return [
            nomeDoMetodo,
            learningRate,
            tamanhoDoMiniBatch,
            beta,
            resultadoDoTreinamento.getQuantidadeDeIteracoes(),
            resultadoDoTreinamento.getTempoComputacional(),
            funcaoObjetivoFinal,
            resultadoDoTreinamento.getAcuracia(),
            acuraciaDeTeste,
            resultadoDoTreinamento
        ]

    @staticmethod
    def executarMetodo(nomeDoMetodo, listaDeEntradasDeTreinamento, listaDeSaidasDeTreinamento, listaDeEntradasDeTeste, listaDeSaidasDeTeste, learningRate, tamanhoDoMiniBatch, beta, numeroMaximoDeIteracoes):
        if(nomeDoMetodo is None):
            return None

        elif(listaDeEntradasDeTreinamento is None):
            return None

        elif(listaDeSaidasDeTreinamento is None):
            return None

        elif(listaDeEntradasDeTeste is None):
            return None

        elif(listaDeSaidasDeTeste is None):
            return None

        quantidadeDePesos = len(listaDeEntradasDeTreinamento[Constantes.INDICE_INICIAL])
        modelo = GerenciadorDeExperimentosParte1.retornarModeloInicial(quantidadeDePesos)

        if(modelo is None):
            return None

        configuracao = ConfiguracaoDoTreinamento(learningRate, Constantes.TOLERANCIA_PADRAO, numeroMaximoDeIteracoes, tamanhoDoMiniBatch, beta, Constantes.EMBARALHAR_AMOSTRAS_POR_PADRAO)

        if(nomeDoMetodo == Constantes.NOME_DO_METODO_STEEPEST_DESCENT):
            resultado = GerenciadorSteepestDescent.executar(modelo, listaDeEntradasDeTreinamento, listaDeSaidasDeTreinamento, configuracao)

        elif(nomeDoMetodo == Constantes.NOME_DO_METODO_SGD):
            resultado = GerenciadorSGD.executar(modelo, listaDeEntradasDeTreinamento, listaDeSaidasDeTreinamento, configuracao)

        elif(nomeDoMetodo == Constantes.NOME_DO_METODO_MOMENTUM):
            resultado = GerenciadorMomentum.executar(modelo, listaDeEntradasDeTreinamento, listaDeSaidasDeTreinamento, configuracao)

        elif(nomeDoMetodo == Constantes.NOME_DO_METODO_NESTEROV):
            resultado = GerenciadorNesterov.executar(modelo, listaDeEntradasDeTreinamento, listaDeSaidasDeTreinamento, configuracao)

        else:
            return None

        if(resultado is None):
            return None

        acuraciaDeTeste = GerenciadorDeRegressaoLogistica.retornarAcuracia(resultado.getModeloLogistico(), listaDeEntradasDeTeste, listaDeSaidasDeTeste)

        if(acuraciaDeTeste is None):
            return None

        return GerenciadorDeExperimentosParte1.retornarLinhaDoResultado(nomeDoMetodo, learningRate, tamanhoDoMiniBatch, beta, resultado, acuraciaDeTeste)

    @staticmethod
    def executarComparacaoDosMetodos(listaDeDados):
        if(listaDeDados is None):
            return None

        listaDeResultados = []

        listaDeNomesDosMetodos = [
            Constantes.NOME_DO_METODO_STEEPEST_DESCENT,
            Constantes.NOME_DO_METODO_SGD,
            Constantes.NOME_DO_METODO_MOMENTUM,
            Constantes.NOME_DO_METODO_NESTEROV
        ]

        indiceDoMetodo = Constantes.INDICE_INICIAL
        quantidadeDeMetodos = len(listaDeNomesDosMetodos)

        while(indiceDoMetodo < quantidadeDeMetodos):
            nomeDoMetodo = listaDeNomesDosMetodos[indiceDoMetodo]

            if(nomeDoMetodo == Constantes.NOME_DO_METODO_SGD):
                numeroMaximoDeIteracoes = Constantes.NUMERO_MAXIMO_DE_EPOCAS_DOS_EXPERIMENTOS_DO_SGD
            else:
                numeroMaximoDeIteracoes = Constantes.NUMERO_MAXIMO_DE_ITERACOES_DOS_EXPERIMENTOS

            linhaDoResultado = GerenciadorDeExperimentosParte1.executarMetodo(nomeDoMetodo, listaDeDados[Constantes.INDICE_DAS_ENTRADAS_DE_TREINAMENTO], listaDeDados[Constantes.INDICE_DAS_SAIDAS_DE_TREINAMENTO], listaDeDados[Constantes.INDICE_DAS_ENTRADAS_DE_TESTE], listaDeDados[Constantes.INDICE_DAS_SAIDAS_DE_TESTE], Constantes.LEARNING_RATE_PADRAO, Constantes.TAMANHO_DO_MINI_BATCH_PADRAO, Constantes.BETA_PADRAO, numeroMaximoDeIteracoes)

            if(linhaDoResultado is None):
                return None

            listaDeResultados.append(linhaDoResultado)
            indiceDoMetodo = indiceDoMetodo + Constantes.INCREMENTO_UNITARIO

        return listaDeResultados

    @staticmethod
    def executarExperimentosDeLearningRate(listaDeDados):
        if(listaDeDados is None):
            return None

        listaDeResultados = []
        indiceDoLearningRate = Constantes.INDICE_INICIAL
        quantidadeDeLearningRates = len(Constantes.listaDeLearningRatesDosExperimentos)

        while(indiceDoLearningRate < quantidadeDeLearningRates):
            learningRate = Constantes.listaDeLearningRatesDosExperimentos[indiceDoLearningRate]

            linhaDoResultado = GerenciadorDeExperimentosParte1.executarMetodo(Constantes.NOME_DO_METODO_STEEPEST_DESCENT, listaDeDados[Constantes.INDICE_DAS_ENTRADAS_DE_TREINAMENTO], listaDeDados[Constantes.INDICE_DAS_SAIDAS_DE_TREINAMENTO], listaDeDados[Constantes.INDICE_DAS_ENTRADAS_DE_TESTE], listaDeDados[Constantes.INDICE_DAS_SAIDAS_DE_TESTE], learningRate, Constantes.TAMANHO_DO_MINI_BATCH_PADRAO, Constantes.BETA_PADRAO, Constantes.NUMERO_MAXIMO_DE_ITERACOES_DOS_EXPERIMENTOS)

            if(linhaDoResultado is None):
                return None

            listaDeResultados.append(linhaDoResultado)
            indiceDoLearningRate = indiceDoLearningRate + Constantes.INCREMENTO_UNITARIO

        return listaDeResultados

    @staticmethod
    def executarExperimentosDeMiniBatch(listaDeDados):
        if(listaDeDados is None):
            return None

        listaDeResultados = []
        indiceDoMiniBatch = Constantes.INDICE_INICIAL
        quantidadeDeMiniBatches = len(Constantes.listaDeTamanhosDosMiniBatches)

        while(indiceDoMiniBatch < quantidadeDeMiniBatches):
            tamanhoDoMiniBatch = Constantes.listaDeTamanhosDosMiniBatches[indiceDoMiniBatch]

            linhaDoResultado = GerenciadorDeExperimentosParte1.executarMetodo(Constantes.NOME_DO_METODO_SGD, listaDeDados[Constantes.INDICE_DAS_ENTRADAS_DE_TREINAMENTO], listaDeDados[Constantes.INDICE_DAS_SAIDAS_DE_TREINAMENTO], listaDeDados[Constantes.INDICE_DAS_ENTRADAS_DE_TESTE], listaDeDados[Constantes.INDICE_DAS_SAIDAS_DE_TESTE], Constantes.LEARNING_RATE_PADRAO, tamanhoDoMiniBatch, Constantes.BETA_PADRAO, Constantes.NUMERO_MAXIMO_DE_EPOCAS_DOS_EXPERIMENTOS_DO_SGD)

            if(linhaDoResultado is None):
                return None

            listaDeResultados.append(linhaDoResultado)
            indiceDoMiniBatch = indiceDoMiniBatch + Constantes.INCREMENTO_UNITARIO

        return listaDeResultados

    @staticmethod
    def executarExperimentosDeBeta(listaDeDados, nomeDoMetodo):
        if(listaDeDados is None):
            return None

        elif(nomeDoMetodo is None):
            return None

        elif((nomeDoMetodo != Constantes.NOME_DO_METODO_MOMENTUM) and (nomeDoMetodo != Constantes.NOME_DO_METODO_NESTEROV)):
            return None

        listaDeResultados = []
        indiceDoBeta = Constantes.INDICE_INICIAL
        quantidadeDeBetas = len(Constantes.listaDeBetasDosExperimentos)

        while(indiceDoBeta < quantidadeDeBetas):
            beta = Constantes.listaDeBetasDosExperimentos[indiceDoBeta]

            linhaDoResultado = GerenciadorDeExperimentosParte1.executarMetodo(nomeDoMetodo, listaDeDados[Constantes.INDICE_DAS_ENTRADAS_DE_TREINAMENTO], listaDeDados[Constantes.INDICE_DAS_SAIDAS_DE_TREINAMENTO], listaDeDados[Constantes.INDICE_DAS_ENTRADAS_DE_TESTE], listaDeDados[Constantes.INDICE_DAS_SAIDAS_DE_TESTE], Constantes.LEARNING_RATE_PADRAO, Constantes.TAMANHO_DO_MINI_BATCH_PADRAO, beta, Constantes.NUMERO_MAXIMO_DE_ITERACOES_DOS_EXPERIMENTOS)

            if(linhaDoResultado is None):
                return None

            listaDeResultados.append(linhaDoResultado)
            indiceDoBeta = indiceDoBeta + Constantes.INCREMENTO_UNITARIO

        return listaDeResultados

    @staticmethod
    def executarTodosOsExperimentos(listaDeDados):
        listaDaComparacaoDosMetodos = GerenciadorDeExperimentosParte1.executarComparacaoDosMetodos(listaDeDados)
        listaDosLearningRates = GerenciadorDeExperimentosParte1.executarExperimentosDeLearningRate(listaDeDados)
        listaDosMiniBatches = GerenciadorDeExperimentosParte1.executarExperimentosDeMiniBatch(listaDeDados)
        listaDosBetasDoMomentum = GerenciadorDeExperimentosParte1.executarExperimentosDeBeta(listaDeDados, Constantes.NOME_DO_METODO_MOMENTUM)
        listaDosBetasDoNesterov = GerenciadorDeExperimentosParte1.executarExperimentosDeBeta(listaDeDados, Constantes.NOME_DO_METODO_NESTEROV)

        if(listaDaComparacaoDosMetodos is None):
            return None

        elif(listaDosLearningRates is None):
            return None

        elif(listaDosMiniBatches is None):
            return None

        elif(listaDosBetasDoMomentum is None):
            return None

        elif(listaDosBetasDoNesterov is None):
            return None

        return [
            listaDaComparacaoDosMetodos,
            listaDosLearningRates,
            listaDosMiniBatches,
            listaDosBetasDoMomentum,
            listaDosBetasDoNesterov
        ]