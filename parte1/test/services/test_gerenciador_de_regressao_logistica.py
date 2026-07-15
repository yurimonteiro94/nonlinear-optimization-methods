import math
import unittest
from model.entidades.modelo_logistico import ModeloLogistico

from services.gerenciador_de_regressao_logistica import GerenciadorDeRegressaoLogistica


class TestGerenciadorDeRegressaoLogistica(unittest.TestCase):

    def testRetornoDaSigmoideParaZero(self):
        resultado = GerenciadorDeRegressaoLogistica.retornarSigmoide(0.0)

        self.assertAlmostEqual(resultado, 0.5)

    def testRetornoDaSigmoideParaValorPositivo(self):
        resultado = GerenciadorDeRegressaoLogistica.retornarSigmoide(2.0)
        esperado = 1.0 / (1.0 + math.exp(-2.0))

        self.assertAlmostEqual(resultado, esperado)

    def testRetornoDaSigmoideParaValorNegativo(self):
        resultado = GerenciadorDeRegressaoLogistica.retornarSigmoide(-2.0)
        esperado = 1.0 / (1.0 + math.exp(2.0))

        self.assertAlmostEqual(resultado, esperado)
        
    def testRetornoDaProbabilidade(self):
        modeloLogistico = ModeloLogistico([1.0, 2.0], 0.5)
        listaDeCaracteristicas = [3.0, 4.0]

        resultado = GerenciadorDeRegressaoLogistica.retornarProbabilidade(modeloLogistico, listaDeCaracteristicas)

        esperado = 1.0 / (1.0 + math.exp(-(0.5 + 1.0 * 3.0 + 2.0 * 4.0)))

        self.assertAlmostEqual(resultado, esperado)

    def testRetornoDaProbabilidadeParaModeloNulo(self):
        resultado = GerenciadorDeRegressaoLogistica.retornarProbabilidade(None, [1.0, 2.0])

        self.assertIsNone(resultado)

    def testRetornoDaProbabilidadeParaListaNula(self):
        modeloLogistico = ModeloLogistico([1.0, 2.0], 0.0)

        resultado = GerenciadorDeRegressaoLogistica.retornarProbabilidade(modeloLogistico, None)

        self.assertIsNone(resultado)

    def testRetornoDaProbabilidadeParaQuantidadeInvalidaDeCaracteristicas(self):
        modeloLogistico = ModeloLogistico([1.0, 2.0], 0.0)

        resultado = GerenciadorDeRegressaoLogistica.retornarProbabilidade(modeloLogistico, [1.0])

        self.assertIsNone(resultado)

    def testRetornoDaFuncaoObjetivo(self):
        modeloLogistico = ModeloLogistico([0.5, -0.2], 0.1)

        listaDeEntradasNormalizadas = [
            [1.0, 2.0],
            [0.5, -1.0]
        ]

        listaDeSaidasEsperadas = [
            1,
            0
        ]

        resultado = GerenciadorDeRegressaoLogistica.retornarFuncaoObjetivo(modeloLogistico, listaDeEntradasNormalizadas, listaDeSaidasEsperadas)

        self.assertIsNotNone(resultado)
        self.assertGreaterEqual(resultado, 0.0)

    def testRetornoDaFuncaoObjetivoParaModeloNulo(self):
        resultado = GerenciadorDeRegressaoLogistica.retornarFuncaoObjetivo(None, [[1.0]], [1])

        self.assertIsNone(resultado)

    def testRetornoDaFuncaoObjetivoParaListaDeEntradasNula(self):
        modeloLogistico = ModeloLogistico([1.0], 0.0)

        resultado = GerenciadorDeRegressaoLogistica.retornarFuncaoObjetivo(modeloLogistico, None, [1])

        self.assertIsNone(resultado)

    def testRetornoDaFuncaoObjetivoParaListaDeSaidasNula(self):
        modeloLogistico = ModeloLogistico([1.0], 0.0)

        resultado = GerenciadorDeRegressaoLogistica.retornarFuncaoObjetivo(modeloLogistico, [[1.0]], None)

        self.assertIsNone(resultado)

    def testRetornoDaFuncaoObjetivoParaQuantidadeDiferenteDeEntradasESaidas(self):
        modeloLogistico = ModeloLogistico([1.0], 0.0)

        resultado = GerenciadorDeRegressaoLogistica.retornarFuncaoObjetivo(modeloLogistico, [[1.0]], [1, 0])

        self.assertIsNone(resultado)

    def testRetornoDoGradienteDosPesos(self):
        modeloLogistico = ModeloLogistico([0.0, 0.0], 0.0)

        listaDeEntradasNormalizadas = [
            [1.0, 2.0],
            [3.0, 4.0]
        ]

        listaDeSaidasEsperadas = [
            0,
            1
        ]

        gradiente = GerenciadorDeRegressaoLogistica.retornarGradienteDosPesos(modeloLogistico, listaDeEntradasNormalizadas, listaDeSaidasEsperadas)

        self.assertIsNotNone(gradiente)
        self.assertEqual(len(gradiente), 2)

    def testRetornoDoGradienteDoVies(self):
        modeloLogistico = ModeloLogistico([0.0, 0.0], 0.0)

        listaDeEntradasNormalizadas = [
            [1.0, 2.0],
            [3.0, 4.0]
        ]

        listaDeSaidasEsperadas = [
            0,
            1
        ]

        gradiente = GerenciadorDeRegressaoLogistica.retornarGradienteDoVies(modeloLogistico, listaDeEntradasNormalizadas, listaDeSaidasEsperadas)

        self.assertIsNotNone(gradiente)

if(__name__ == "__main__"):
    unittest.main()