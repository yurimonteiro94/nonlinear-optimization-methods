import unittest

from model.entidades.configuracao_do_treinamento import ConfiguracaoDoTreinamento
from model.entidades.modelo_logistico import ModeloLogistico
from services.gerenciador_sgd import GerenciadorSGD


class TestGerenciadorSGD(unittest.TestCase):

    def testExecucaoDoSGD(self):
        modeloLogistico = ModeloLogistico([0.0, 0.0], 0.0)
        listaDeEntradas = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]
        listaDeSaidas = [0, 0, 0, 1]
        configuracao = ConfiguracaoDoTreinamento(0.1, 0.0, 100, 2, 0.9, True)

        resultado = GerenciadorSGD.executar(modeloLogistico, listaDeEntradas, listaDeSaidas, configuracao)

        self.assertIsNotNone(resultado)
        self.assertGreater(len(resultado.getListaDaFuncaoObjetivo()), 0)
        self.assertGreaterEqual(resultado.getAcuracia(), 0.0)
        self.assertLessEqual(resultado.getAcuracia(), 1.0)

    def testReducaoDaFuncaoObjetivo(self):
        modeloLogistico = ModeloLogistico([0.0, 0.0], 0.0)
        listaDeEntradas = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]
        listaDeSaidas = [0, 0, 0, 1]
        configuracao = ConfiguracaoDoTreinamento(0.1, 0.0, 100, 2, 0.9, True)

        resultado = GerenciadorSGD.executar(modeloLogistico, listaDeEntradas, listaDeSaidas, configuracao)
        listaDaFuncaoObjetivo = resultado.getListaDaFuncaoObjetivo()

        self.assertLess(listaDaFuncaoObjetivo[-1], listaDaFuncaoObjetivo[0])

    def testRetornoDaListaDeIndicesEmbaralhados(self):
        listaDeIndices = GerenciadorSGD.retornarListaDeIndicesEmbaralhados(5, 0)

        self.assertEqual(len(listaDeIndices), 5)
        self.assertEqual(sorted(listaDeIndices), [0, 1, 2, 3, 4])

    def testRetornoParaModeloNulo(self):
        configuracao = ConfiguracaoDoTreinamento(0.1, 0.0, 10, 2, 0.9, True)

        resultado = GerenciadorSGD.executar(None, [[0.0]], [0], configuracao)

        self.assertIsNone(resultado)

    def testRetornoParaTamanhoDoMiniBatchInvalido(self):
        modeloLogistico = ModeloLogistico([0.0], 0.0)
        configuracao = ConfiguracaoDoTreinamento(0.1, 0.0, 10, 0, 0.9, True)

        resultado = GerenciadorSGD.executar(modeloLogistico, [[0.0]], [0], configuracao)

        self.assertIsNone(resultado)

    def testAtualizacaoDoModelo(self):
        modeloLogistico = ModeloLogistico([0.0], 0.0)

        resultado = GerenciadorSGD.atualizarModelo(modeloLogistico, [[1.0]], [1], 0.1)

        self.assertTrue(resultado)
        self.assertNotEqual(modeloLogistico.getListaDePesos()[0], 0.0)


if(__name__ == "__main__"):
    unittest.main()