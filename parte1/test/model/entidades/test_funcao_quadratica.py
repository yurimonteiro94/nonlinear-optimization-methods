import unittest

from model.entidades.funcao_quadratica import FuncaoQuadratica


class TestFuncaoQuadratica(unittest.TestCase):

    def testCriacaoDaFuncaoQuadratica(self):
        matrizA = [[2.0, 0.0], [0.0, 4.0]]
        vetorB = [-2.0, -8.0]
        constanteC = 3.0

        funcaoQuadratica = FuncaoQuadratica(matrizA, vetorB, constanteC)

        self.assertEqual(funcaoQuadratica.getMatrizA(), matrizA)
        self.assertEqual(funcaoQuadratica.getVetorB(), vetorB)
        self.assertEqual(funcaoQuadratica.getConstanteC(), constanteC)

    def testAlteracaoDaFuncaoQuadratica(self):
        funcaoQuadratica = FuncaoQuadratica([[1.0]], [0.0], 0.0)

        funcaoQuadratica.setMatrizA([[3.0]])
        funcaoQuadratica.setVetorB([2.0])
        funcaoQuadratica.setConstanteC(1.0)

        self.assertEqual(funcaoQuadratica.getMatrizA(), [[3.0]])
        self.assertEqual(funcaoQuadratica.getVetorB(), [2.0])
        self.assertEqual(funcaoQuadratica.getConstanteC(), 1.0)


if(__name__ == "__main__"):
    unittest.main()