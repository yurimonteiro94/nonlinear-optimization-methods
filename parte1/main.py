from controller.controller_amostra import ControllerAmostra
from model.entidades.configuracao_do_treinamento import ConfiguracaoDoTreinamento
from model.entidades.modelo_logistico import ModeloLogistico
from services.constantes import Constantes
from services.gerenciador_de_regressao_logistica import GerenciadorDeRegressaoLogistica
from services.gerenciador_steepest_descent import GerenciadorSteepestDescent
from view.view_exercicio_1 import ViewExercicio1


def retornarListaDePesosIniciais(quantidadeDePesos):
    if(quantidadeDePesos <= Constantes.QUANTIDADE_NULA):
        return None

    listaDePesosIniciais = []
    indiceDoPeso = Constantes.INDICE_INICIAL

    while(indiceDoPeso < quantidadeDePesos):
        listaDePesosIniciais.append(Constantes.VALOR_INICIAL_DOS_PARAMETROS)
        indiceDoPeso = indiceDoPeso + Constantes.INCREMENTO_UNITARIO

    return listaDePesosIniciais


def executarExercicio1():
    listaDeTreinamentoFoiCarregada = ControllerAmostra.carregarListaDeAmostrasDeTreinamento()
    listaDeTesteFoiCarregada = ControllerAmostra.carregarListaDeAmostrasDeTeste()

    if(not listaDeTreinamentoFoiCarregada):
        return False

    elif(not listaDeTesteFoiCarregada):
        return False

    listaDeAmostrasDeTreinamento = ControllerAmostra.retornarListaDeAmostrasDeTreinamento()
    listaDeAmostrasDeTeste = ControllerAmostra.retornarListaDeAmostrasDeTeste()

    listaDeMedias = ControllerAmostra.retornarListaDeMedias(listaDeAmostrasDeTreinamento)
    listaDeDesviosPadrao = ControllerAmostra.retornarListaDeDesviosPadrao(listaDeAmostrasDeTreinamento, listaDeMedias)

    if(listaDeMedias is None):
        return False

    elif(listaDeDesviosPadrao is None):
        return False

    listaDeEntradasDeTreinamento = ControllerAmostra.retornarListaDeEntradasNormalizadas(listaDeAmostrasDeTreinamento, listaDeMedias, listaDeDesviosPadrao)
    listaDeEntradasDeTeste = ControllerAmostra.retornarListaDeEntradasNormalizadas(listaDeAmostrasDeTeste, listaDeMedias, listaDeDesviosPadrao)

    listaDeSaidasDeTreinamento = ControllerAmostra.retornarListaDeSaidasEsperadas(listaDeAmostrasDeTreinamento)
    listaDeSaidasDeTeste = ControllerAmostra.retornarListaDeSaidasEsperadas(listaDeAmostrasDeTeste)

    if(listaDeEntradasDeTreinamento is None):
        return False

    elif(listaDeEntradasDeTeste is None):
        return False

    elif(listaDeSaidasDeTreinamento is None):
        return False

    elif(listaDeSaidasDeTeste is None):
        return False

    quantidadeDePesos = len(listaDeEntradasDeTreinamento[Constantes.INDICE_INICIAL])
    listaDePesosIniciais = retornarListaDePesosIniciais(quantidadeDePesos)

    if(listaDePesosIniciais is None):
        return False

    modeloLogistico = ModeloLogistico(listaDePesosIniciais, Constantes.VALOR_INICIAL_DOS_PARAMETROS)

    configuracaoDoTreinamento = ConfiguracaoDoTreinamento(Constantes.LEARNING_RATE_PADRAO, Constantes.TOLERANCIA_PADRAO, Constantes.NUMERO_MAXIMO_DE_ITERACOES_PADRAO, Constantes.TAMANHO_DO_MINI_BATCH_PADRAO, Constantes.BETA_PADRAO, Constantes.EMBARALHAR_AMOSTRAS_POR_PADRAO)

    resultadoDoTreinamento = GerenciadorSteepestDescent.executar(modeloLogistico, listaDeEntradasDeTreinamento, listaDeSaidasDeTreinamento, configuracaoDoTreinamento)

    if(resultadoDoTreinamento is None):
        return False

    acuraciaDeTeste = GerenciadorDeRegressaoLogistica.retornarAcuracia(resultadoDoTreinamento.getModeloLogistico(), listaDeEntradasDeTeste, listaDeSaidasDeTeste)

    if(acuraciaDeTeste is None):
        return False

    graficosForamSalvos = ViewExercicio1.salvarGraficos(resultadoDoTreinamento)
    resumoFoiSalvo = ViewExercicio1.salvarResumo(resultadoDoTreinamento, acuraciaDeTeste, configuracaoDoTreinamento)
    resumoFoiApresentado = ViewExercicio1.apresentarResumo(resultadoDoTreinamento, acuraciaDeTeste, configuracaoDoTreinamento)

    if(not graficosForamSalvos):
        return False

    elif(not resumoFoiSalvo):
        return False

    elif(not resumoFoiApresentado):
        return False

    return True


def main():
    exercicioFoiExecutado = executarExercicio1()

    if(exercicioFoiExecutado):
        ViewExercicio1.apresentarMensagem(Constantes.MENSAGEM_DE_SUCESSO_DO_EXERCICIO_1)
    else:
        ViewExercicio1.apresentarMensagem(Constantes.MENSAGEM_DE_ERRO_DO_EXERCICIO_1)


if(__name__ == "__main__"):
    main()