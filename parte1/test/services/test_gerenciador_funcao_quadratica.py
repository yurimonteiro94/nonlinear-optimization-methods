import math
import unittest

from model.entidades.funcao_quadratica import FuncaoQuadratica
from services.gerenciador_funcao_quadratica import GerenciadorFuncaoQuadratica


class TestGerenciadorFuncaoQuadratica(unittest.TestCase):

    def setUp(self):
        self.funcaoQuadratica = FuncaoQuadratica([[2.0, 0.0], [0.0, 4.0]], [-2.0, -8.0], 0.0)

    def testValidacaoDaFuncaoQuadratica(self):
        resultado = GerenciadorFuncaoQuadratica.funcaoQuadraticaEhValida(self.funcaoQuadratica)

        self.assertTrue(resultado)

    def testRetornoParaFuncaoQuadraticaInvalida(self):
        funcaoQuadratica = FuncaoQuadratica([[1.0, 0.0]], [1.0, 2.0], 0.0)

        resultado = GerenciadorFuncaoQuadratica.funcaoQuadraticaEhValida(funcaoQuadratica)

        self.assertFalse(resultado)

    def testValidacaoDeMatrizSimetrica(self):
        self.assertTrue(GerenciadorFuncaoQuadratica.matrizEhSimetrica([[2.0, 1.0], [1.0, 3.0]]))
        self.assertFalse(GerenciadorFuncaoQuadratica.matrizEhSimetrica([[2.0, 1.0], [0.0, 3.0]]))

    def testValidacaoDeMatrizPositivaDefinida(self):
        self.assertTrue(GerenciadorFuncaoQuadratica.matrizEhPositivaDefinida([[2.0, 0.0], [0.0, 4.0]]))
        self.assertFalse(GerenciadorFuncaoQuadratica.matrizEhPositivaDefinida([[1.0, 0.0], [0.0, -1.0]]))

    def testRetornoDoValorDaFuncaoObjetivo(self):
        valor = GerenciadorFuncaoQuadratica.retornarValorDaFuncaoObjetivo(self.funcaoQuadratica, [1.0, 2.0])

        self.assertAlmostEqual(valor, -9.0)

    def testRetornoDoGradiente(self):
        gradiente = GerenciadorFuncaoQuadratica.retornarGradiente(self.funcaoQuadratica, [0.0, 0.0])

        self.assertEqual(gradiente, [-2.0, -8.0])

    def testRetornoDaNormaDoGradiente(self):
        norma = GerenciadorFuncaoQuadratica.retornarNormaDoGradiente(self.funcaoQuadratica, [0.0, 0.0])

        self.assertAlmostEqual(norma, math.sqrt(68.0))

    def testRetornoDaHessiana(self):
        hessiana = GerenciadorFuncaoQuadratica.retornarHessiana(self.funcaoQuadratica)

        self.assertEqual(hessiana, [[2.0, 0.0], [0.0, 4.0]])

    def testRetornoDoNumeroDeCondicao(self):
        numeroDeCondicao = GerenciadorFuncaoQuadratica.retornarNumeroDeCondicao(self.funcaoQuadratica)

        self.assertAlmostEqual(numeroDeCondicao, 2.0)

    def testRetornoDoPontoOtimo(self):
        pontoOtimo = GerenciadorFuncaoQuadratica.retornarPontoOtimo(self.funcaoQuadratica)

        self.assertAlmostEqual(pontoOtimo[0], 1.0)
        self.assertAlmostEqual(pontoOtimo[1], 2.0)

    def testRetornoParaPontoInvalido(self):
        valor = GerenciadorFuncaoQuadratica.retornarValorDaFuncaoObjetivo(self.funcaoQuadratica, [1.0])

        self.assertIsNone(valor)


if(__name__ == "__main__"):
    unittest.main()