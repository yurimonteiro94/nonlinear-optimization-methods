import unittest

from model.entidades.funcao_quadratica import FuncaoQuadratica
from services.gerenciador_steepest_descent_funcao_quadratica import GerenciadorSteepestDescentFuncaoQuadratica


class TestGerenciadorSteepestDescentFuncaoQuadratica(unittest.TestCase):

    def setUp(self):
        self.funcaoQuadratica = FuncaoQuadratica([[2.0, 0.0], [0.0, 4.0]], [-2.0, -8.0], 0.0)

    def testRetornoDoTamanhoDoPassoExato(self):
        tamanhoDoPasso = GerenciadorSteepestDescentFuncaoQuadratica.retornarTamanhoDoPassoExato(self.funcaoQuadratica, [0.0, 0.0])

        self.assertIsNotNone(tamanhoDoPasso)
        self.assertGreater(tamanhoDoPasso, 0.0)

    def testExecucaoDoSteepestDescent(self):
        resultado = GerenciadorSteepestDescentFuncaoQuadratica.executar(self.funcaoQuadratica, [0.0, 0.0], 1.0e-8, 1000)

        self.assertIsNotNone(resultado)
        self.assertAlmostEqual(resultado.getPontoFinal()[0], 1.0, places=6)
        self.assertAlmostEqual(resultado.getPontoFinal()[1], 2.0, places=6)
        self.assertLessEqual(resultado.getListaDaNormaDoGradiente()[-1], 1.0e-8)

    def testReducaoDaFuncaoObjetivo(self):
        resultado = GerenciadorSteepestDescentFuncaoQuadratica.executar(self.funcaoQuadratica, [0.0, 0.0], 1.0e-8, 1000)

        self.assertLess(resultado.getListaDaFuncaoObjetivo()[-1], resultado.getListaDaFuncaoObjetivo()[0])

    def testRetornoParaFuncaoNula(self):
        resultado = GerenciadorSteepestDescentFuncaoQuadratica.executar(None, [0.0], 1.0e-8, 100)

        self.assertIsNone(resultado)

    def testRetornoParaNumeroMaximoDeIteracoesInvalido(self):
        resultado = GerenciadorSteepestDescentFuncaoQuadratica.executar(self.funcaoQuadratica, [0.0, 0.0], 1.0e-8, 0)

        self.assertIsNone(resultado)


if(__name__ == "__main__"):
    unittest.main()