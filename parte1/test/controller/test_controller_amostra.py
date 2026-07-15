import unittest

from controller.controller_amostra import ControllerAmostra


class TestControllerAmostra(unittest.TestCase):

    def testCarregamentoDaListaDeAmostrasDeTreinamento(self):
        resultado = ControllerAmostra.carregarListaDeAmostrasDeTreinamento()
        self.assertTrue(resultado)

    def testCarregamentoDaListaDeAmostrasDeTeste(self):
        resultado = ControllerAmostra.carregarListaDeAmostrasDeTeste()

        self.assertTrue(resultado)

    def testRetornoDaListaDeAmostrasDeTreinamento(self):
        ControllerAmostra.carregarListaDeAmostrasDeTreinamento()

        listaDeAmostras = ControllerAmostra.retornarListaDeAmostrasDeTreinamento()

        self.assertIsNotNone(listaDeAmostras)
        self.assertGreater(len(listaDeAmostras), 0)

    def testRetornoDaListaDeAmostrasDeTeste(self):
        ControllerAmostra.carregarListaDeAmostrasDeTeste()

        listaDeAmostras = ControllerAmostra.retornarListaDeAmostrasDeTeste()

        self.assertIsNotNone(listaDeAmostras)
        self.assertGreater(len(listaDeAmostras), 0)

    def testRetornoDaListaDeMedias(self):
        ControllerAmostra.carregarListaDeAmostrasDeTreinamento()

        listaDeAmostras = ControllerAmostra.retornarListaDeAmostrasDeTreinamento()
        listaDeMedias = ControllerAmostra.retornarListaDeMedias(listaDeAmostras)

        self.assertIsNotNone(listaDeMedias)
        self.assertEqual(len(listaDeMedias), 5)

    def testRetornoDaListaDeDesviosPadrao(self):
        ControllerAmostra.carregarListaDeAmostrasDeTreinamento()

        listaDeAmostras = ControllerAmostra.retornarListaDeAmostrasDeTreinamento()
        listaDeMedias = ControllerAmostra.retornarListaDeMedias(listaDeAmostras)
        listaDeDesviosPadrao = ControllerAmostra.retornarListaDeDesviosPadrao(listaDeAmostras, listaDeMedias)

        self.assertIsNotNone(listaDeDesviosPadrao)
        self.assertEqual(len(listaDeDesviosPadrao), 5)

    def testRetornoDaListaDeEntradasNormalizadas(self):
        ControllerAmostra.carregarListaDeAmostrasDeTreinamento()

        listaDeAmostras = ControllerAmostra.retornarListaDeAmostrasDeTreinamento()
        listaDeMedias = ControllerAmostra.retornarListaDeMedias(listaDeAmostras)
        listaDeDesviosPadrao = ControllerAmostra.retornarListaDeDesviosPadrao(listaDeAmostras, listaDeMedias)
        listaDeEntradasNormalizadas = ControllerAmostra.retornarListaDeEntradasNormalizadas(listaDeAmostras, listaDeMedias, listaDeDesviosPadrao)

        self.assertIsNotNone(listaDeEntradasNormalizadas)
        self.assertEqual(len(listaDeEntradasNormalizadas), len(listaDeAmostras))

    def testRetornoDaListaDeSaidasEsperadas(self):
        ControllerAmostra.carregarListaDeAmostrasDeTreinamento()

        listaDeAmostras = ControllerAmostra.retornarListaDeAmostrasDeTreinamento()
        listaDeSaidasEsperadas = ControllerAmostra.retornarListaDeSaidasEsperadas(listaDeAmostras)

        self.assertIsNotNone(listaDeSaidasEsperadas)
        self.assertEqual(len(listaDeSaidasEsperadas), len(listaDeAmostras))


if(__name__ == "__main__"):
    unittest.main()