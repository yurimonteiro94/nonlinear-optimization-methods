from controller.controller_otimizacao_quadratica import ControllerOtimizacaoQuadratica
from model.entidades.funcao_quadratica import FuncaoQuadratica
from services.constantes_parte_2 import ConstantesParte2
from view.view_parte_2 import ViewParte2


def retornarFuncaoQuadratica():
    matrizA = [
        [100.0, 0.0],
        [0.0, 1.0]
    ]

    vetorB = [
        -100.0,
        -2.0
    ]

    constanteC = 0.0

    return FuncaoQuadratica(matrizA, vetorB, constanteC)


def executarParte2():
    funcaoQuadratica = retornarFuncaoQuadratica()
    pontoInicial = [-4.0, 8.0]

    resultadoDoSteepestDescent = ControllerOtimizacaoQuadratica.executarSteepestDescent(funcaoQuadratica, pontoInicial, ConstantesParte2.TOLERANCIA_PADRAO, ConstantesParte2.NUMERO_MAXIMO_DE_ITERACOES_PADRAO)

    if(resultadoDoSteepestDescent is None):
        return False

    resultadoDoNewton = ControllerOtimizacaoQuadratica.executarNewton(funcaoQuadratica, pontoInicial, ConstantesParte2.TOLERANCIA_PADRAO, ConstantesParte2.NUMERO_MAXIMO_DE_ITERACOES_PADRAO)

    if(resultadoDoNewton is None):
        return False

    resultadosDoSteepestDescentForamSalvos = ViewParte2.salvarResultadosDoSteepestDescent(funcaoQuadratica, resultadoDoSteepestDescent)
    resultadosDoNewtonForamSalvos = ViewParte2.salvarResultadosDoNewton(funcaoQuadratica, resultadoDoNewton)
    comparacaoFoiSalva = ViewParte2.salvarComparacao(resultadoDoSteepestDescent, resultadoDoNewton)

    return resultadosDoSteepestDescentForamSalvos and resultadosDoNewtonForamSalvos and comparacaoFoiSalva


def main():
    if(executarParte2()):
        print(ConstantesParte2.MENSAGEM_DE_SUCESSO_DA_PARTE_2)
    else:
        print(ConstantesParte2.MENSAGEM_DE_ERRO_DA_PARTE_2)


if(__name__ == "__main__"):
    main()