import unittest
from datetime import datetime

from model.entidades.amostra import Amostra
from services.constantes import Constantes
from services.gerenciador_de_amostras import GerenciadorDeAmostras


class TestGerenciadorDeAmostras(unittest.TestCase):

    TEXTO_DA_DATA = "2015-02-04 17:51:00"

    TEMPERATURA_DA_PRIMEIRA_AMOSTRA = 10.0
    UMIDADE_DA_PRIMEIRA_AMOSTRA = 20.0
    LUMINOSIDADE_DA_PRIMEIRA_AMOSTRA = 30.0
    CO2_DA_PRIMEIRA_AMOSTRA = 40.0
    RAZAO_DE_UMIDADE_DA_PRIMEIRA_AMOSTRA = 50.0

    TEMPERATURA_DA_SEGUNDA_AMOSTRA = 20.0
    UMIDADE_DA_SEGUNDA_AMOSTRA = 40.0
    LUMINOSIDADE_DA_SEGUNDA_AMOSTRA = 60.0
    CO2_DA_SEGUNDA_AMOSTRA = 80.0
    RAZAO_DE_UMIDADE_DA_SEGUNDA_AMOSTRA = 100.0

    MEDIA_DA_TEMPERATURA = 15.0
    MEDIA_DA_UMIDADE = 30.0
    MEDIA_DA_LUMINOSIDADE = 45.0
    MEDIA_DO_CO2 = 60.0
    MEDIA_DA_RAZAO_DE_UMIDADE = 75.0

    DESVIO_PADRAO_DA_TEMPERATURA = 5.0
    DESVIO_PADRAO_DA_UMIDADE = 10.0
    DESVIO_PADRAO_DA_LUMINOSIDADE = 15.0
    DESVIO_PADRAO_DO_CO2 = 20.0
    DESVIO_PADRAO_DA_RAZAO_DE_UMIDADE = 25.0

    VALOR_NORMALIZADO_DA_PRIMEIRA_AMOSTRA = -1.0
    VALOR_NORMALIZADO_DA_SEGUNDA_AMOSTRA = 1.0

    @classmethod
    def setUpClass(cls):
        data = datetime.strptime(TestGerenciadorDeAmostras.TEXTO_DA_DATA, Constantes.FORMATO_DA_DATA)
        primeiroIdentificador = Constantes.PRIMEIRO_IDENTIFICADOR
        segundoIdentificador = primeiroIdentificador + Constantes.INCREMENTO_UNITARIO

        cls.primeiraAmostra = Amostra(primeiroIdentificador, data, TestGerenciadorDeAmostras.TEMPERATURA_DA_PRIMEIRA_AMOSTRA, TestGerenciadorDeAmostras.UMIDADE_DA_PRIMEIRA_AMOSTRA, TestGerenciadorDeAmostras.LUMINOSIDADE_DA_PRIMEIRA_AMOSTRA, TestGerenciadorDeAmostras.CO2_DA_PRIMEIRA_AMOSTRA, TestGerenciadorDeAmostras.RAZAO_DE_UMIDADE_DA_PRIMEIRA_AMOSTRA, Constantes.OCUPACAO_VAZIA)
        cls.segundaAmostra = Amostra(segundoIdentificador, data, TestGerenciadorDeAmostras.TEMPERATURA_DA_SEGUNDA_AMOSTRA, TestGerenciadorDeAmostras.UMIDADE_DA_SEGUNDA_AMOSTRA, TestGerenciadorDeAmostras.LUMINOSIDADE_DA_SEGUNDA_AMOSTRA, TestGerenciadorDeAmostras.CO2_DA_SEGUNDA_AMOSTRA, TestGerenciadorDeAmostras.RAZAO_DE_UMIDADE_DA_SEGUNDA_AMOSTRA, Constantes.OCUPACAO_PRESENTE)
        cls.listaDeAmostras = []
        cls.listaDeAmostras.append(cls.primeiraAmostra)
        cls.listaDeAmostras.append(cls.segundaAmostra)

    def testRetornoDaListaDeCaracteristicas(self):
        listaDeCaracteristicas = GerenciadorDeAmostras.retornarListaDeCaracteristicas(TestGerenciadorDeAmostras.primeiraAmostra)
        listaDeCaracteristicasEsperadas = [TestGerenciadorDeAmostras.TEMPERATURA_DA_PRIMEIRA_AMOSTRA, TestGerenciadorDeAmostras.UMIDADE_DA_PRIMEIRA_AMOSTRA, TestGerenciadorDeAmostras.LUMINOSIDADE_DA_PRIMEIRA_AMOSTRA, TestGerenciadorDeAmostras.CO2_DA_PRIMEIRA_AMOSTRA, TestGerenciadorDeAmostras.RAZAO_DE_UMIDADE_DA_PRIMEIRA_AMOSTRA]

        self.assertEqual(listaDeCaracteristicas, listaDeCaracteristicasEsperadas)

    def testRetornoDaListaDeMedias(self):
        listaDeMedias = GerenciadorDeAmostras.retornarListaDeMedias(TestGerenciadorDeAmostras.listaDeAmostras)
        listaDeMediasEsperadas = [TestGerenciadorDeAmostras.MEDIA_DA_TEMPERATURA, TestGerenciadorDeAmostras.MEDIA_DA_UMIDADE, TestGerenciadorDeAmostras.MEDIA_DA_LUMINOSIDADE, TestGerenciadorDeAmostras.MEDIA_DO_CO2, TestGerenciadorDeAmostras.MEDIA_DA_RAZAO_DE_UMIDADE]

        self.assertEqual(listaDeMedias, listaDeMediasEsperadas)

    def testRetornoDaListaDeDesviosPadrao(self):
        listaDeMedias = GerenciadorDeAmostras.retornarListaDeMedias(TestGerenciadorDeAmostras.listaDeAmostras)
        listaDeDesviosPadrao = GerenciadorDeAmostras.retornarListaDeDesviosPadrao(TestGerenciadorDeAmostras.listaDeAmostras, listaDeMedias)
        listaDeDesviosPadraoEsperados = [TestGerenciadorDeAmostras.DESVIO_PADRAO_DA_TEMPERATURA, TestGerenciadorDeAmostras.DESVIO_PADRAO_DA_UMIDADE, TestGerenciadorDeAmostras.DESVIO_PADRAO_DA_LUMINOSIDADE, TestGerenciadorDeAmostras.DESVIO_PADRAO_DO_CO2, TestGerenciadorDeAmostras.DESVIO_PADRAO_DA_RAZAO_DE_UMIDADE]

        self.assertEqual(listaDeDesviosPadrao, listaDeDesviosPadraoEsperados)

    def testRetornoDaListaDeEntradasNormalizadas(self):
        listaDeMedias = GerenciadorDeAmostras.retornarListaDeMedias(TestGerenciadorDeAmostras.listaDeAmostras)
        listaDeDesviosPadrao = GerenciadorDeAmostras.retornarListaDeDesviosPadrao(TestGerenciadorDeAmostras.listaDeAmostras, listaDeMedias)
        listaDeEntradasNormalizadas = GerenciadorDeAmostras.retornarListaDeEntradasNormalizadas(TestGerenciadorDeAmostras.listaDeAmostras, listaDeMedias, listaDeDesviosPadrao)
        listaDePrimeirasCaracteristicasNormalizadasEsperadas = [TestGerenciadorDeAmostras.VALOR_NORMALIZADO_DA_PRIMEIRA_AMOSTRA, TestGerenciadorDeAmostras.VALOR_NORMALIZADO_DA_PRIMEIRA_AMOSTRA, TestGerenciadorDeAmostras.VALOR_NORMALIZADO_DA_PRIMEIRA_AMOSTRA, TestGerenciadorDeAmostras.VALOR_NORMALIZADO_DA_PRIMEIRA_AMOSTRA, TestGerenciadorDeAmostras.VALOR_NORMALIZADO_DA_PRIMEIRA_AMOSTRA]
        listaDeSegundasCaracteristicasNormalizadasEsperadas = [TestGerenciadorDeAmostras.VALOR_NORMALIZADO_DA_SEGUNDA_AMOSTRA, TestGerenciadorDeAmostras.VALOR_NORMALIZADO_DA_SEGUNDA_AMOSTRA, TestGerenciadorDeAmostras.VALOR_NORMALIZADO_DA_SEGUNDA_AMOSTRA, TestGerenciadorDeAmostras.VALOR_NORMALIZADO_DA_SEGUNDA_AMOSTRA, TestGerenciadorDeAmostras.VALOR_NORMALIZADO_DA_SEGUNDA_AMOSTRA]
        listaDeEntradasNormalizadasEsperadas = []
        listaDeEntradasNormalizadasEsperadas.append(listaDePrimeirasCaracteristicasNormalizadasEsperadas)
        listaDeEntradasNormalizadasEsperadas.append(listaDeSegundasCaracteristicasNormalizadasEsperadas)

        self.assertEqual(listaDeEntradasNormalizadas, listaDeEntradasNormalizadasEsperadas)

    def testRetornoDaListaDeSaidasEsperadas(self):
        listaDeSaidasEsperadas = GerenciadorDeAmostras.retornarListaDeSaidasEsperadas(TestGerenciadorDeAmostras.listaDeAmostras)
        listaDeSaidasEsperadasCorretas = [Constantes.OCUPACAO_VAZIA, Constantes.OCUPACAO_PRESENTE]

        self.assertEqual(listaDeSaidasEsperadas, listaDeSaidasEsperadasCorretas)

    def testRetornoParaListaDeAmostrasVazia(self):
        listaDeAmostrasVazia = []
        listaDeMedias = GerenciadorDeAmostras.retornarListaDeMedias(listaDeAmostrasVazia)

        self.assertIsNone(listaDeMedias)


if(__name__ == "__main__"):
    unittest.main()