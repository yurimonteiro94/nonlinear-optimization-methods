import unittest

from model.entidades.configuracao_do_treinamento import ConfiguracaoDoTreinamento
from model.entidades.modelo_logistico import ModeloLogistico
from services.gerenciador_momentum import GerenciadorMomentum


class TestGerenciadorMomentum(unittest.TestCase):

    def testExecucaoDoMomentum(self):
        modelo = ModeloLogistico([0.0, 0.0], 0.0)
        entradas = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]
        saidas = [0, 0, 0, 1]
        configuracao = ConfiguracaoDoTreinamento(0.1, 0.0, 100, 2, 0.9, True)

        resultado = GerenciadorMomentum.executar(modelo, entradas, saidas, configuracao)

        self.assertIsNotNone(resultado)
        self.assertLess(resultado.getListaDaFuncaoObjetivo()[-1], resultado.getListaDaFuncaoObjetivo()[0])

    def testRetornoParaModeloNulo(self):
        configuracao = ConfiguracaoDoTreinamento(0.1, 0.0, 100, 2, 0.9, True)

        resultado = GerenciadorMomentum.executar(None, [[0.0]], [0], configuracao)

        self.assertIsNone(resultado)

    def testRetornoParaBetaInvalido(self):
        modelo = ModeloLogistico([0.0], 0.0)
        configuracao = ConfiguracaoDoTreinamento(0.1, 0.0, 100, 2, 1.0, True)

        resultado = GerenciadorMomentum.executar(modelo, [[0.0]], [0], configuracao)

        self.assertIsNone(resultado)


if(__name__ == "__main__"):
    unittest.main()