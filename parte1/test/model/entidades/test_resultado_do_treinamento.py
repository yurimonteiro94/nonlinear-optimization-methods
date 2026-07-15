import unittest

from model.entidades.modelo_logistico import ModeloLogistico
from model.entidades.resultado_do_treinamento import ResultadoDoTreinamento


class TestResultadoDoTreinamento(unittest.TestCase):

    def testConstrucao(self):
        resultado = ResultadoDoTreinamento()

        self.assertIsNone(resultado.getModeloLogistico())
        self.assertEqual(resultado.getListaDaFuncaoObjetivo(), [])
        self.assertEqual(resultado.getListaDaNormaDoGradiente(), [])
        self.assertEqual(resultado.getListaDaAcuracia(), [])
        self.assertEqual(resultado.getQuantidadeDeIteracoes(), 0)
        self.assertEqual(resultado.getTempoComputacional(), 0.0)
        self.assertEqual(resultado.getAcuracia(), 0.0)
        self.assertEqual(resultado.getMotivoDaParada(), "")

    def testSetters(self):
        resultado = ResultadoDoTreinamento()
        modeloLogistico = ModeloLogistico([1.0, 2.0], 3.0)

        resultado.setModeloLogistico(modeloLogistico)
        resultado.setListaDaFuncaoObjetivo([1.0, 2.0, 3.0])
        resultado.setListaDaNormaDoGradiente([5.0, 4.0, 3.0])
        resultado.setListaDaAcuracia([0.5, 0.75, 1.0])
        resultado.setQuantidadeDeIteracoes(100)
        resultado.setTempoComputacional(1.234)
        resultado.setAcuracia(0.98)
        resultado.setMotivoDaParada("Teste")

        self.assertEqual(resultado.getModeloLogistico(), modeloLogistico)
        self.assertEqual(resultado.getListaDaFuncaoObjetivo(), [1.0, 2.0, 3.0])
        self.assertEqual(resultado.getListaDaNormaDoGradiente(), [5.0, 4.0, 3.0])
        self.assertEqual(resultado.getListaDaAcuracia(), [0.5, 0.75, 1.0])
        self.assertEqual(resultado.getQuantidadeDeIteracoes(), 100)
        self.assertEqual(resultado.getTempoComputacional(), 1.234)
        self.assertEqual(resultado.getAcuracia(), 0.98)
        self.assertEqual(resultado.getMotivoDaParada(), "Teste")


if(__name__ == "__main__"):
    unittest.main()