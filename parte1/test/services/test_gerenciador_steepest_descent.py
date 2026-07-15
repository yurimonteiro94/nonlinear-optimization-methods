import unittest

from model.entidades.configuracao_do_treinamento import ConfiguracaoDoTreinamento
from model.entidades.modelo_logistico import ModeloLogistico
from services.gerenciador_steepest_descent import GerenciadorSteepestDescent


class TestGerenciadorSteepestDescent(unittest.TestCase):

    def testExecucaoDoSteepestDescent(self):
        modeloLogistico = ModeloLogistico([0.0, 0.0], 0.0)
        listaDeEntradasNormalizadas = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]
        listaDeSaidasEsperadas = [0, 0, 0, 1]
        configuracao = ConfiguracaoDoTreinamento(0.1, 1.0e-8, 100, 2, 0.9, True)

        resultado = GerenciadorSteepestDescent.executar(modeloLogistico, listaDeEntradasNormalizadas, listaDeSaidasEsperadas, configuracao)

        self.assertIsNotNone(resultado)
        self.assertIsNotNone(resultado.getModeloLogistico())
        self.assertGreater(len(resultado.getListaDaFuncaoObjetivo()), 0)
        self.assertEqual(len(resultado.getListaDaFuncaoObjetivo()), len(resultado.getListaDaNormaDoGradiente()))
        self.assertEqual(len(resultado.getListaDaFuncaoObjetivo()), len(resultado.getListaDaAcuracia()))
        self.assertGreaterEqual(resultado.getAcuracia(), 0.0)
        self.assertLessEqual(resultado.getAcuracia(), 1.0)
        self.assertGreaterEqual(resultado.getTempoComputacional(), 0.0)

    def testReducaoDaFuncaoObjetivo(self):
        modeloLogistico = ModeloLogistico([0.0, 0.0], 0.0)
        listaDeEntradasNormalizadas = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]
        listaDeSaidasEsperadas = [0, 0, 0, 1]
        configuracao = ConfiguracaoDoTreinamento(0.1, 0.0, 100, 2, 0.9, True)

        resultado = GerenciadorSteepestDescent.executar(modeloLogistico, listaDeEntradasNormalizadas, listaDeSaidasEsperadas, configuracao)
        listaDaFuncaoObjetivo = resultado.getListaDaFuncaoObjetivo()

        self.assertLess(listaDaFuncaoObjetivo[-1], listaDaFuncaoObjetivo[0])

    def testRetornoParaModeloNulo(self):
        configuracao = ConfiguracaoDoTreinamento(0.1, 1.0e-6, 100, 2, 0.9, True)

        resultado = GerenciadorSteepestDescent.executar(None, [[0.0]], [0], configuracao)

        self.assertIsNone(resultado)

    def testRetornoParaConfiguracaoNula(self):
        modeloLogistico = ModeloLogistico([0.0], 0.0)

        resultado = GerenciadorSteepestDescent.executar(modeloLogistico, [[0.0]], [0], None)

        self.assertIsNone(resultado)

    def testRetornoParaLearningRateInvalido(self):
        modeloLogistico = ModeloLogistico([0.0], 0.0)
        configuracao = ConfiguracaoDoTreinamento(0.0, 1.0e-6, 100, 2, 0.9, True)

        resultado = GerenciadorSteepestDescent.executar(modeloLogistico, [[0.0]], [0], configuracao)

        self.assertIsNone(resultado)


if(__name__ == "__main__"):
    unittest.main()