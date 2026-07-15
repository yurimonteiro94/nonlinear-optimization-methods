import unittest

from model.entidades.configuracao_do_treinamento import ConfiguracaoDoTreinamento
from model.entidades.modelo_logistico import ModeloLogistico
from services.gerenciador_nesterov import GerenciadorNesterov


class TestGerenciadorNesterov(unittest.TestCase):

    def testExecucaoDoNesterov(self):
        modelo = ModeloLogistico([0.0, 0.0], 0.0)
        entradas = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]
        saidas = [0, 0, 0, 1]
        configuracao = ConfiguracaoDoTreinamento(0.1, 0.0, 100, 2, 0.9, True)

        resultado = GerenciadorNesterov.executar(modelo, entradas, saidas, configuracao)

        self.assertIsNotNone(resultado)
        self.assertLess(resultado.getListaDaFuncaoObjetivo()[-1], resultado.getListaDaFuncaoObjetivo()[0])

    def testRetornoDoModeloAntecipado(self):
        modelo = ModeloLogistico([1.0, 2.0], 3.0)

        modeloAntecipado = GerenciadorNesterov.retornarModeloAntecipado(modelo, [0.5, -0.5], 1.0, 0.9)

        self.assertIsNotNone(modeloAntecipado)
        self.assertAlmostEqual(modeloAntecipado.getListaDePesos()[0], 1.45)
        self.assertAlmostEqual(modeloAntecipado.getListaDePesos()[1], 1.55)
        self.assertAlmostEqual(modeloAntecipado.getVies(), 3.9)

    def testRetornoParaBetaInvalido(self):
        modelo = ModeloLogistico([0.0], 0.0)
        configuracao = ConfiguracaoDoTreinamento(0.1, 0.0, 100, 2, 1.0, True)

        resultado = GerenciadorNesterov.executar(modelo, [[0.0]], [0], configuracao)

        self.assertIsNone(resultado)


if(__name__ == "__main__"):
    unittest.main()