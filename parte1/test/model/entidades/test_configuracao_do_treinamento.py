import unittest

from model.entidades.configuracao_do_treinamento import ConfiguracaoDoTreinamento


class TestConfiguracaoDoTreinamento(unittest.TestCase):

    def testCriacaoDaConfiguracaoDoTreinamento(self):
        configuracao = ConfiguracaoDoTreinamento(0.01, 1.0e-6, 1000, 32, 0.9, True)

        self.assertEqual(configuracao.getLearningRate(), 0.01)
        self.assertEqual(configuracao.getTolerancia(), 1.0e-6)
        self.assertEqual(configuracao.getNumeroMaximoDeIteracoes(), 1000)
        self.assertEqual(configuracao.getTamanhoDoMiniBatch(), 32)
        self.assertEqual(configuracao.getBeta(), 0.9)
        self.assertTrue(configuracao.getEmbaralharAmostras())

    def testAlteracaoDaConfiguracaoDoTreinamento(self):
        configuracao = ConfiguracaoDoTreinamento(0.01, 1.0e-6, 1000, 32, 0.9, True)

        configuracao.setLearningRate(0.1)
        configuracao.setTolerancia(1.0e-4)
        configuracao.setNumeroMaximoDeIteracoes(500)
        configuracao.setTamanhoDoMiniBatch(64)
        configuracao.setBeta(0.5)
        configuracao.setEmbaralharAmostras(False)

        self.assertEqual(configuracao.getLearningRate(), 0.1)
        self.assertEqual(configuracao.getTolerancia(), 1.0e-4)
        self.assertEqual(configuracao.getNumeroMaximoDeIteracoes(), 500)
        self.assertEqual(configuracao.getTamanhoDoMiniBatch(), 64)
        self.assertEqual(configuracao.getBeta(), 0.5)
        self.assertFalse(configuracao.getEmbaralharAmostras())


if(__name__ == "__main__"):
    unittest.main()