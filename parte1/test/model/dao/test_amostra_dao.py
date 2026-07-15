import unittest

from model.dao.amostra_dao import AmostraDAO
from model.entidades.amostra import Amostra


class TestAmostraDAO(unittest.TestCase):

    QUANTIDADE_ESPERADA_DE_AMOSTRAS_DE_TREINAMENTO = 16448
    QUANTIDADE_ESPERADA_DE_AMOSTRAS_DE_TESTE = 4112
    INDICE_DA_PRIMEIRA_AMOSTRA = 0
    CAMINHO_DO_ARQUIVO_INEXISTENTE = "arquivo_inexistente.csv"

    @classmethod
    def setUpClass(cls):
        cls.treinamentoFoiCarregado = AmostraDAO.carregarListaDeAmostrasDeTreinamento()
        cls.testeFoiCarregado = AmostraDAO.carregarListaDeAmostrasDeTeste()

    def testCarregamentoDaListaDeAmostrasDeTreinamento(self):
        self.assertTrue(TestAmostraDAO.treinamentoFoiCarregado)

    def testCarregamentoDaListaDeAmostrasDeTeste(self):
        self.assertTrue(TestAmostraDAO.testeFoiCarregado)

    def testQuantidadeDeAmostrasDeTreinamento(self):
        listaDeAmostrasDeTreinamento = AmostraDAO.retornarListaDeAmostrasDeTreinamento()
        quantidadeDeAmostrasDeTreinamento = len(listaDeAmostrasDeTreinamento)

        self.assertEqual(quantidadeDeAmostrasDeTreinamento, TestAmostraDAO.QUANTIDADE_ESPERADA_DE_AMOSTRAS_DE_TREINAMENTO)

    def testQuantidadeDeAmostrasDeTeste(self):
        listaDeAmostrasDeTeste = AmostraDAO.retornarListaDeAmostrasDeTeste()
        quantidadeDeAmostrasDeTeste = len(listaDeAmostrasDeTeste)

        self.assertEqual(quantidadeDeAmostrasDeTeste, TestAmostraDAO.QUANTIDADE_ESPERADA_DE_AMOSTRAS_DE_TESTE)

    def testTipoDaPrimeiraAmostraDeTreinamento(self):
        listaDeAmostrasDeTreinamento = AmostraDAO.retornarListaDeAmostrasDeTreinamento()
        primeiraAmostraDeTreinamento = listaDeAmostrasDeTreinamento[TestAmostraDAO.INDICE_DA_PRIMEIRA_AMOSTRA]

        self.assertIsInstance(primeiraAmostraDeTreinamento, Amostra)

    def testTipoDaPrimeiraAmostraDeTeste(self):
        listaDeAmostrasDeTeste = AmostraDAO.retornarListaDeAmostrasDeTeste()
        primeiraAmostraDeTeste = listaDeAmostrasDeTeste[TestAmostraDAO.INDICE_DA_PRIMEIRA_AMOSTRA]

        self.assertIsInstance(primeiraAmostraDeTeste, Amostra)

    def testRetornoParaArquivoInexistente(self):
        listaDeAmostras = AmostraDAO.retornarListaDeAmostras(TestAmostraDAO.CAMINHO_DO_ARQUIVO_INEXISTENTE)

        self.assertIsNone(listaDeAmostras)


if(__name__ == "__main__"):
    unittest.main()