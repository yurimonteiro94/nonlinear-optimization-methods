from controller.controller_otimizacao_quadratica import ControllerOtimizacaoQuadratica
from model.entidades.funcao_quadratica import FuncaoQuadratica
from services.constantes_parte_2 import ConstantesParte2
from view.view_exercicio_5 import ViewExercicio5
from view.view_parte_2 import ViewParte2


def retornarFuncaoQuadraticaDoExercicio4():
    matrizA = [
        [2.0, -1.8],
        [-1.8, 2.0]
    ]

    vetorB = [
        3.4,
        -4.2
    ]

    constanteC = 4.6

    return FuncaoQuadratica(matrizA, vetorB, constanteC)


def retornarPontoInicialDoExercicio4():
    return [3.0, -5.0]


def retornarFuncaoQuadraticaDoExercicio5():
    matrizA = [
        [2.0, -1.8, 0.0, 0.0],
        [-1.8, 4.0, -1.8, 0.0],
        [0.0, -1.8, 4.0, -1.8],
        [0.0, 0.0, -1.8, 2.0]
    ]

    vetorB = [
        3.4,
        -8.4,
        6.8,
        -4.2
    ]

    constanteC = 13.8

    return FuncaoQuadratica(matrizA, vetorB, constanteC)


def retornarPontoInicialDoExercicio5():
    return [3.0, -5.0, 3.0, -5.0]


def executarExercicio4():
    funcaoQuadratica = retornarFuncaoQuadraticaDoExercicio4()
    pontoInicial = retornarPontoInicialDoExercicio4()

    resultadoDoSteepestDescent = ControllerOtimizacaoQuadratica.executarSteepestDescent(funcaoQuadratica,pontoInicial,ConstantesParte2.TOLERANCIA_PADRAO,ConstantesParte2.NUMERO_MAXIMO_DE_ITERACOES_PADRAO)

    if(resultadoDoSteepestDescent is None):
        return False

    resultadoDoNewton = ControllerOtimizacaoQuadratica.executarNewton(funcaoQuadratica,pontoInicial,ConstantesParte2.TOLERANCIA_PADRAO,ConstantesParte2.NUMERO_MAXIMO_DE_ITERACOES_PADRAO)

    if(resultadoDoNewton is None):
        return False

    resultadosDoSteepestDescentForamSalvos = ViewParte2.salvarResultadosDoSteepestDescent(funcaoQuadratica,resultadoDoSteepestDescent)
    resultadosDoNewtonForamSalvos = ViewParte2.salvarResultadosDoNewton(funcaoQuadratica,resultadoDoNewton)
    comparacaoFoiSalva = ViewParte2.salvarComparacao(resultadoDoSteepestDescent,resultadoDoNewton)

    return resultadosDoSteepestDescentForamSalvos and resultadosDoNewtonForamSalvos and comparacaoFoiSalva


def executarExercicio5():
    funcaoQuadratica = retornarFuncaoQuadraticaDoExercicio5()
    pontoInicial = retornarPontoInicialDoExercicio5()

    resultadoDoSteepestDescent = ControllerOtimizacaoQuadratica.executarSteepestDescent(funcaoQuadratica,pontoInicial,ConstantesParte2.TOLERANCIA_PADRAO,ConstantesParte2.NUMERO_MAXIMO_DE_ITERACOES_PADRAO)

    if(resultadoDoSteepestDescent is None):
        return False

    resultadoDoNewton = ControllerOtimizacaoQuadratica.executarNewton(funcaoQuadratica,pontoInicial,ConstantesParte2.TOLERANCIA_PADRAO,ConstantesParte2.NUMERO_MAXIMO_DE_ITERACOES_PADRAO)

    if(resultadoDoNewton is None):
        return False

    resultadosDoSteepestDescentForamSalvos = ViewExercicio5.salvarResultadosDoSteepestDescent(funcaoQuadratica,resultadoDoSteepestDescent)
    resultadosDoNewtonForamSalvos = ViewExercicio5.salvarResultadosDoNewton(funcaoQuadratica,resultadoDoNewton)
    comparacaoFoiSalva = ViewExercicio5.salvarComparacao(resultadoDoSteepestDescent,resultadoDoNewton)

    return resultadosDoSteepestDescentForamSalvos and resultadosDoNewtonForamSalvos and comparacaoFoiSalva


def executarParte2():
    if(not executarExercicio4()):
        return False
    elif(not executarExercicio5()):
        return False

    return True


def main():
    if(executarParte2()):
        print(ConstantesParte2.MENSAGEM_DE_SUCESSO_DA_PARTE_2)
    else:
        print(ConstantesParte2.MENSAGEM_DE_ERRO_DA_PARTE_2)


if(__name__ == "__main__"):
    main()