import unittest

from model.entidades.funcao_quadratica import FuncaoQuadratica
from services.gerenciador_newton_funcao_quadratica import GerenciadorNewtonFuncaoQuadratica


class TestGerenciadorNewtonFuncaoQuadratica(unittest.TestCase):

    def setUp(self):
        self.funcaoQuadratica = FuncaoQuadratica([[2.0, 0.0], [0.0, 4.0]], [-2.0, -8.0], 0.0)

    def testRetornoDaDirecaoDeNewton(self):
        listaDaDirecao = GerenciadorNewtonFuncaoQuadratica.retornarDirecaoDeNewton(self.funcaoQuadratica, [0.0, 0.0])

        self.assertIsNotNone(listaDaDirecao)
        self.assertAlmostEqual(listaDaDirecao[0], 1.0)
        self.assertAlmostEqual(listaDaDirecao[1], 2.0)

    def testExecucaoDoMetodoDeNewton(self):
        resultado = GerenciadorNewtonFuncaoQuadratica.executar(self.funcaoQuadratica, [0.0, 0.0], 1.0e-8, 100)

        self.assertIsNotNone(resultado)
        self.assertAlmostEqual(resultado.getPontoFinal()[0], 1.0)
        self.assertAlmostEqual(resultado.getPontoFinal()[1], 2.0)
        self.assertEqual(resultado.getQuantidadeDeIteracoes(), 1)
        self.assertLessEqual(resultado.getListaDaNormaDoGradiente()[-1], 1.0e-8)

    def testReducaoDaFuncaoObjetivo(self):
        resultado = GerenciadorNewtonFuncaoQuadratica.executar(self.funcaoQuadratica, [0.0, 0.0], 1.0e-8, 100)

        self.assertLess(resultado.getListaDaFuncaoObjetivo()[-1], resultado.getListaDaFuncaoObjetivo()[0])

    def testRetornoParaFuncaoNula(self):
        resultado = GerenciadorNewtonFuncaoQuadratica.executar(None, [0.0], 1.0e-8, 100)

        self.assertIsNone(resultado)

    def testRetornoParaToleranciaInvalida(self):
        resultado = GerenciadorNewtonFuncaoQuadratica.executar(self.funcaoQuadratica, [0.0, 0.0], -1.0, 100)

        self.assertIsNone(resultado)


if(__name__ == "__main__"):
    unittest.main()