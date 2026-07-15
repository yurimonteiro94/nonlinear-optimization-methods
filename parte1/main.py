from controller.controller_amostra import ControllerAmostra
from model.entidades.configuracao_do_treinamento import ConfiguracaoDoTreinamento
from model.entidades.modelo_logistico import ModeloLogistico
from services.constantes import Constantes
from services.gerenciador_de_experimentos_parte_1 import GerenciadorDeExperimentosParte1
from services.gerenciador_de_regressao_logistica import GerenciadorDeRegressaoLogistica
from services.gerenciador_momentum import GerenciadorMomentum
from services.gerenciador_nesterov import GerenciadorNesterov
from services.gerenciador_sgd import GerenciadorSGD
from services.gerenciador_steepest_descent import GerenciadorSteepestDescent
from view.view_comparacao_parte_1 import ViewComparacaoParte1
from view.view_exercicio_1 import ViewExercicio1
from view.view_exercicio_2 import ViewExercicio2
from view.view_exercicio_3 import ViewExercicio3
from view.view_exercicio_4 import ViewExercicio4


def retornarListaDePesosIniciais(quantidadeDePesos):
    if(quantidadeDePesos <= Constantes.QUANTIDADE_NULA):
        return None

    listaDePesos = []
    indiceDoPeso = Constantes.INDICE_INICIAL

    while(indiceDoPeso < quantidadeDePesos):
        listaDePesos.append(Constantes.VALOR_INICIAL_DOS_PARAMETROS)
        indiceDoPeso = indiceDoPeso + Constantes.INCREMENTO_UNITARIO

    return listaDePesos


def retornarDadosPreparados():
    if(not ControllerAmostra.carregarListaDeAmostrasDeTreinamento()):
        return None

    elif(not ControllerAmostra.carregarListaDeAmostrasDeTeste()):
        return None

    listaDeAmostrasDeTreinamento = ControllerAmostra.retornarListaDeAmostrasDeTreinamento()
    listaDeAmostrasDeTeste = ControllerAmostra.retornarListaDeAmostrasDeTeste()
    listaDeMedias = ControllerAmostra.retornarListaDeMedias(listaDeAmostrasDeTreinamento)
    listaDeDesviosPadrao = ControllerAmostra.retornarListaDeDesviosPadrao(listaDeAmostrasDeTreinamento, listaDeMedias)

    if(listaDeMedias is None):
        return None

    elif(listaDeDesviosPadrao is None):
        return None

    entradasDeTreinamento = ControllerAmostra.retornarListaDeEntradasNormalizadas(listaDeAmostrasDeTreinamento, listaDeMedias, listaDeDesviosPadrao)
    saidasDeTreinamento = ControllerAmostra.retornarListaDeSaidasEsperadas(listaDeAmostrasDeTreinamento)
    entradasDeTeste = ControllerAmostra.retornarListaDeEntradasNormalizadas(listaDeAmostrasDeTeste, listaDeMedias, listaDeDesviosPadrao)
    saidasDeTeste = ControllerAmostra.retornarListaDeSaidasEsperadas(listaDeAmostrasDeTeste)

    if(entradasDeTreinamento is None):
        return None

    elif(saidasDeTreinamento is None):
        return None

    elif(entradasDeTeste is None):
        return None

    elif(saidasDeTeste is None):
        return None

    return [entradasDeTreinamento, saidasDeTreinamento, entradasDeTeste, saidasDeTeste]


def retornarModeloLogisticoInicial(listaDeEntradas):
    quantidadeDePesos = len(listaDeEntradas[Constantes.INDICE_INICIAL])
    listaDePesos = retornarListaDePesosIniciais(quantidadeDePesos)

    if(listaDePesos is None):
        return None

    return ModeloLogistico(listaDePesos, Constantes.VALOR_INICIAL_DOS_PARAMETROS)


def retornarAcuraciaDeTeste(resultado, listaDeDados):
    if(resultado is None):
        return None

    return GerenciadorDeRegressaoLogistica.retornarAcuracia(resultado.getModeloLogistico(), listaDeDados[Constantes.INDICE_DAS_ENTRADAS_DE_TESTE], listaDeDados[Constantes.INDICE_DAS_SAIDAS_DE_TESTE])


def executarExercicio1(listaDeDados):
    modelo = retornarModeloLogisticoInicial(listaDeDados[Constantes.INDICE_DAS_ENTRADAS_DE_TREINAMENTO])
    configuracao = ConfiguracaoDoTreinamento(Constantes.LEARNING_RATE_PADRAO, Constantes.TOLERANCIA_PADRAO, Constantes.NUMERO_MAXIMO_DE_ITERACOES_PADRAO, Constantes.TAMANHO_DO_MINI_BATCH_PADRAO, Constantes.BETA_PADRAO, Constantes.EMBARALHAR_AMOSTRAS_POR_PADRAO)
    resultado = GerenciadorSteepestDescent.executar(modelo, listaDeDados[Constantes.INDICE_DAS_ENTRADAS_DE_TREINAMENTO], listaDeDados[Constantes.INDICE_DAS_SAIDAS_DE_TREINAMENTO], configuracao)

    if(resultado is None):
        return False

    acuraciaDeTeste = retornarAcuraciaDeTeste(resultado, listaDeDados)

    if(acuraciaDeTeste is None):
        return False

    return ViewExercicio1.salvarGraficos(resultado) and ViewExercicio1.salvarResumo(resultado, acuraciaDeTeste, configuracao) and ViewExercicio1.apresentarResumo(resultado, acuraciaDeTeste, configuracao)


def executarExercicio2(listaDeDados):
    modelo = retornarModeloLogisticoInicial(listaDeDados[Constantes.INDICE_DAS_ENTRADAS_DE_TREINAMENTO])
    configuracao = ConfiguracaoDoTreinamento(Constantes.LEARNING_RATE_PADRAO, Constantes.TOLERANCIA_PADRAO, Constantes.NUMERO_MAXIMO_DE_ITERACOES_DO_SGD, Constantes.TAMANHO_DO_MINI_BATCH_PADRAO, Constantes.BETA_PADRAO, Constantes.EMBARALHAR_AMOSTRAS_POR_PADRAO)
    resultado = GerenciadorSGD.executar(modelo, listaDeDados[Constantes.INDICE_DAS_ENTRADAS_DE_TREINAMENTO], listaDeDados[Constantes.INDICE_DAS_SAIDAS_DE_TREINAMENTO], configuracao)

    if(resultado is None):
        return False

    acuraciaDeTeste = retornarAcuraciaDeTeste(resultado, listaDeDados)

    if(acuraciaDeTeste is None):
        return False

    return ViewExercicio2.salvarGraficos(resultado) and ViewExercicio2.salvarResumo(resultado, acuraciaDeTeste, configuracao) and ViewExercicio2.apresentarResumo(resultado, acuraciaDeTeste, configuracao)


def executarExercicio3(listaDeDados):
    modelo = retornarModeloLogisticoInicial(listaDeDados[Constantes.INDICE_DAS_ENTRADAS_DE_TREINAMENTO])
    configuracao = ConfiguracaoDoTreinamento(Constantes.LEARNING_RATE_PADRAO, Constantes.TOLERANCIA_PADRAO, Constantes.NUMERO_MAXIMO_DE_ITERACOES_DO_MOMENTUM, Constantes.TAMANHO_DO_MINI_BATCH_PADRAO, Constantes.BETA_PADRAO, Constantes.EMBARALHAR_AMOSTRAS_POR_PADRAO)
    resultado = GerenciadorMomentum.executar(modelo, listaDeDados[Constantes.INDICE_DAS_ENTRADAS_DE_TREINAMENTO], listaDeDados[Constantes.INDICE_DAS_SAIDAS_DE_TREINAMENTO], configuracao)

    if(resultado is None):
        return False

    acuraciaDeTeste = retornarAcuraciaDeTeste(resultado, listaDeDados)

    if(acuraciaDeTeste is None):
        return False

    return ViewExercicio3.salvarGraficos(resultado) and ViewExercicio3.salvarResumo(resultado, acuraciaDeTeste, configuracao) and ViewExercicio3.apresentarResumo(resultado, acuraciaDeTeste, configuracao)


def executarExercicio4(listaDeDados):
    modelo = retornarModeloLogisticoInicial(listaDeDados[Constantes.INDICE_DAS_ENTRADAS_DE_TREINAMENTO])
    configuracao = ConfiguracaoDoTreinamento(Constantes.LEARNING_RATE_PADRAO, Constantes.TOLERANCIA_PADRAO, Constantes.NUMERO_MAXIMO_DE_ITERACOES_DO_NESTEROV, Constantes.TAMANHO_DO_MINI_BATCH_PADRAO, Constantes.BETA_PADRAO, Constantes.EMBARALHAR_AMOSTRAS_POR_PADRAO)
    resultado = GerenciadorNesterov.executar(modelo, listaDeDados[Constantes.INDICE_DAS_ENTRADAS_DE_TREINAMENTO], listaDeDados[Constantes.INDICE_DAS_SAIDAS_DE_TREINAMENTO], configuracao)

    if(resultado is None):
        return False

    acuraciaDeTeste = retornarAcuraciaDeTeste(resultado, listaDeDados)

    if(acuraciaDeTeste is None):
        return False

    return ViewExercicio4.salvarGraficos(resultado) and ViewExercicio4.salvarResumo(resultado, acuraciaDeTeste, configuracao) and ViewExercicio4.apresentarResumo(resultado, acuraciaDeTeste, configuracao)


def executarExperimentosDaParte1(listaDeDados):
    listaDeExperimentos = GerenciadorDeExperimentosParte1.executarTodosOsExperimentos(listaDeDados)

    if(listaDeExperimentos is None):
        return False

    return ViewComparacaoParte1.salvarTodosOsResultados(listaDeExperimentos)


def apresentarResultadoDaExecucao(resultado, mensagemDeSucesso, mensagemDeErro):
    if(resultado):
        ViewExercicio1.apresentarMensagem(mensagemDeSucesso)
    else:
        ViewExercicio1.apresentarMensagem(mensagemDeErro)


def main():
    listaDeDados = retornarDadosPreparados()

    if(listaDeDados is None):
        ViewExercicio1.apresentarMensagem(Constantes.MENSAGEM_DE_ERRO_DE_PROCESSAMENTO)
        return

    apresentarResultadoDaExecucao(executarExercicio1(listaDeDados), Constantes.MENSAGEM_DE_SUCESSO_DO_EXERCICIO_1, Constantes.MENSAGEM_DE_ERRO_DO_EXERCICIO_1)
    apresentarResultadoDaExecucao(executarExercicio2(listaDeDados), Constantes.MENSAGEM_DE_SUCESSO_DO_EXERCICIO_2, Constantes.MENSAGEM_DE_ERRO_DO_EXERCICIO_2)
    apresentarResultadoDaExecucao(executarExercicio3(listaDeDados), Constantes.MENSAGEM_DE_SUCESSO_DO_EXERCICIO_3, Constantes.MENSAGEM_DE_ERRO_DO_EXERCICIO_3)
    apresentarResultadoDaExecucao(executarExercicio4(listaDeDados), Constantes.MENSAGEM_DE_SUCESSO_DO_EXERCICIO_4, Constantes.MENSAGEM_DE_ERRO_DO_EXERCICIO_4)
    apresentarResultadoDaExecucao(executarExperimentosDaParte1(listaDeDados), Constantes.MENSAGEM_DE_SUCESSO_DOS_EXPERIMENTOS, Constantes.MENSAGEM_DE_ERRO_DOS_EXPERIMENTOS)


if(__name__ == "__main__"):
    main()