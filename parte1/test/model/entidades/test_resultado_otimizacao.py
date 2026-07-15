import unittest

from model.entidades.resultado_otimizacao import ResultadoOtimizacao


class TestResultadoOtimizacao(unittest.TestCase):

    def testConstrucaoDoResultadoDaOtimizacao(self):
        resultado = ResultadoOtimizacao()

        self.assertIsNone(resultado.getPontoFinal())
        self.assertEqual(resultado.getListaDePontos(), [])
        self.assertEqual(resultado.getListaDaFuncaoObjetivo(), [])
        self.assertEqual(resultado.getListaDaNormaDoGradiente(), [])
        self.assertEqual(resultado.getQuantidadeDeIteracoes(), 0)
        self.assertEqual(resultado.getTempoComputacional(), 0.0)
        self.assertEqual(resultado.getMotivoDaParada(), "")

    def testAlteracaoDoResultadoDaOtimizacao(self):
        resultado = ResultadoOtimizacao()

        resultado.setPontoFinal([1.0, 2.0])
        resultado.setListaDePontos([[0.0, 0.0], [1.0, 2.0]])
        resultado.setListaDaFuncaoObjetivo([10.0, 0.0])
        resultado.setListaDaNormaDoGradiente([5.0, 0.0])
        resultado.setQuantidadeDeIteracoes(1)
        resultado.setTempoComputacional(0.01)
        resultado.setMotivoDaParada("Teste")

        self.assertEqual(resultado.getPontoFinal(), [1.0, 2.0])
        self.assertEqual(resultado.getListaDePontos(), [[0.0, 0.0], [1.0, 2.0]])
        self.assertEqual(resultado.getListaDaFuncaoObjetivo(), [10.0, 0.0])
        self.assertEqual(resultado.getListaDaNormaDoGradiente(), [5.0, 0.0])
        self.assertEqual(resultado.getQuantidadeDeIteracoes(), 1)
        self.assertEqual(resultado.getTempoComputacional(), 0.01)
        self.assertEqual(resultado.getMotivoDaParada(), "Teste")


if(__name__ == "__main__"):
    unittest.main()