import unittest

from services.constantes import Constantes
from services.gerenciador_de_experimentos_parte_1 import GerenciadorDeExperimentosParte1


class TestGerenciadorDeExperimentosParte1(unittest.TestCase):

    def testRetornoDoModeloInicial(self):
        modelo = GerenciadorDeExperimentosParte1.retornarModeloInicial(3)

        self.assertIsNotNone(modelo)
        self.assertEqual(modelo.getListaDePesos(), [0.0, 0.0, 0.0])
        self.assertEqual(modelo.getVies(), 0.0)

    def testRetornoParaQuantidadeDePesosInvalida(self):
        modelo = GerenciadorDeExperimentosParte1.retornarModeloInicial(0)

        self.assertIsNone(modelo)

    def testExecucaoDeMetodo(self):
        entradasDeTreinamento = [[0.0], [1.0], [2.0], [3.0]]
        saidasDeTreinamento = [0, 0, 1, 1]
        entradasDeTeste = [[0.5], [2.5]]
        saidasDeTeste = [0, 1]

        resultado = GerenciadorDeExperimentosParte1.executarMetodo(Constantes.NOME_DO_METODO_STEEPEST_DESCENT, entradasDeTreinamento, saidasDeTreinamento, entradasDeTeste, saidasDeTeste, 0.1, 2, 0.9, 10)

        self.assertIsNotNone(resultado)
        self.assertEqual(resultado[Constantes.INDICE_DO_NOME_DO_METODO_NO_RESULTADO], Constantes.NOME_DO_METODO_STEEPEST_DESCENT)
        self.assertIsNotNone(resultado[Constantes.INDICE_DO_RESULTADO_DO_TREINAMENTO])

    def testRetornoParaMetodoInvalido(self):
        entradas = [[0.0], [1.0]]
        saidas = [0, 1]

        resultado = GerenciadorDeExperimentosParte1.executarMetodo("Inválido", entradas, saidas, entradas, saidas, 0.1, 2, 0.9, 10)

        self.assertIsNone(resultado)

    def testRetornoParaListaDeDadosNula(self):
        resultado = GerenciadorDeExperimentosParte1.executarComparacaoDosMetodos(None)

        self.assertIsNone(resultado)


if(__name__ == "__main__"):
    unittest.main()