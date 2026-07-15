from services.gerenciador_funcao_quadratica import GerenciadorFuncaoQuadratica
from services.gerenciador_newton_funcao_quadratica import GerenciadorNewtonFuncaoQuadratica
from services.gerenciador_steepest_descent_funcao_quadratica import GerenciadorSteepestDescentFuncaoQuadratica


class ControllerOtimizacaoQuadratica:

    @staticmethod
    def executarSteepestDescent(funcaoQuadratica, pontoInicial, tolerancia, numeroMaximoDeIteracoes):
        return GerenciadorSteepestDescentFuncaoQuadratica.executar(funcaoQuadratica, pontoInicial, tolerancia, numeroMaximoDeIteracoes)

    @staticmethod
    def executarNewton(funcaoQuadratica, pontoInicial, tolerancia, numeroMaximoDeIteracoes):
        return GerenciadorNewtonFuncaoQuadratica.executar(funcaoQuadratica, pontoInicial, tolerancia, numeroMaximoDeIteracoes)

    @staticmethod
    def retornarValorDaFuncaoObjetivo(funcaoQuadratica, ponto):
        return GerenciadorFuncaoQuadratica.retornarValorDaFuncaoObjetivo(funcaoQuadratica, ponto)

    @staticmethod
    def retornarPontoOtimo(funcaoQuadratica):
        return GerenciadorFuncaoQuadratica.retornarPontoOtimo(funcaoQuadratica)

    @staticmethod
    def retornarNumeroDeCondicao(funcaoQuadratica):
        return GerenciadorFuncaoQuadratica.retornarNumeroDeCondicao(funcaoQuadratica)

    @staticmethod
    def matrizEhPositivaDefinida(matriz):
        return GerenciadorFuncaoQuadratica.matrizEhPositivaDefinida(matriz)