import os
import unittest
import main_parte_2
from model.entidades.funcao_quadratica import FuncaoQuadratica

class TestMainParte2(unittest.TestCase):

    def testArquivoPrincipalDaParte2NaoEstaVazio(self):
        caminhoDoArquivo = os.path.abspath(main_parte_2.__file__)
        self.assertGreater(os.path.getsize(caminhoDoArquivo),0)

    def testRetornoDaFuncaoQuadraticaDoExercicio4(self):
        funcaoQuadratica = (main_parte_2.retornarFuncaoQuadraticaDoExercicio4())
        self.assertIsInstance(funcaoQuadratica,FuncaoQuadratica)

    def testRetornoDaFuncaoQuadraticaDoExercicio5(self):
        funcaoQuadratica = (main_parte_2.retornarFuncaoQuadraticaDoExercicio5())
        self.assertIsInstance(funcaoQuadratica,FuncaoQuadratica)

    def testDimensaoDoPontoInicialDoExercicio4(self):
        pontoInicial = (main_parte_2.retornarPontoInicialDoExercicio4())
        self.assertEqual(len(pontoInicial),2)

    def testDimensaoDoPontoInicialDoExercicio5(self):
        pontoInicial = (main_parte_2.retornarPontoInicialDoExercicio5())
        self.assertEqual(len(pontoInicial),4)


if(__name__ == "__main__"):
    unittest.main()