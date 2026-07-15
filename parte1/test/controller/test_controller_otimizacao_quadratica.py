import unittest

from controller.controller_otimizacao_quadratica import ControllerOtimizacaoQuadratica
from model.entidades.funcao_quadratica import FuncaoQuadratica


class TestControllerOtimizacaoQuadratica(unittest.TestCase):

    def setUp(self):
        self.funcaoQuadratica = FuncaoQuadratica([[2.0, 0.0], [0.0, 4.0]], [-2.0, -8.0], 0.0)

    def testExecucaoDoSteepestDescent(self):
        resultado = ControllerOtimizacaoQuadratica.executarSteepestDescent(self.funcaoQuadratica, [0.0, 0.0], 1.0e-8, 1000)

        self.assertIsNotNone(resultado)

    def testExecucaoDoMetodoDeNewton(self):
        resultado = ControllerOtimizacaoQuadratica.executarNewton(self.funcaoQuadratica, [0.0, 0.0], 1.0e-8, 100)

        self.assertIsNotNone(resultado)

    def testRetornoDoPontoOtimo(self):
        pontoOtimo = ControllerOtimizacaoQuadratica.retornarPontoOtimo(self.funcaoQuadratica)

        self.assertAlmostEqual(pontoOtimo[0], 1.0)
        self.assertAlmostEqual(pontoOtimo[1], 2.0)

    def testRetornoDoNumeroDeCondicao(self):
        numeroDeCondicao = ControllerOtimizacaoQuadratica.retornarNumeroDeCondicao(self.funcaoQuadratica)

        self.assertAlmostEqual(numeroDeCondicao, 2.0)


if(__name__ == "__main__"):
    unittest.main()