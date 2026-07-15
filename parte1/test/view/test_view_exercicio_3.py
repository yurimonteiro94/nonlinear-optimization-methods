import unittest

from model.entidades.configuracao_do_treinamento import ConfiguracaoDoTreinamento
from model.entidades.resultado_do_treinamento import ResultadoDoTreinamento
from view.view_exercicio_3 import ViewExercicio3


class TestViewExercicio3(unittest.TestCase):

    def testRetornoDoTextoDoResumo(self):
        resultado = ResultadoDoTreinamento()
        resultado.setListaDaFuncaoObjetivo([1.0, 0.5])
        resultado.setQuantidadeDeIteracoes(2)
        resultado.setTempoComputacional(0.1)
        resultado.setAcuracia(0.9)
        resultado.setMotivoDaParada("Teste")

        configuracao = ConfiguracaoDoTreinamento(0.1, 1.0e-6, 100, 32, 0.9, True)

        texto = ViewExercicio3.retornarTextoDoResumo(resultado, 0.85, configuracao)

        self.assertIsNotNone(texto)
        self.assertIn("Momentum", texto)
        self.assertIn("Beta", texto)


if(__name__ == "__main__"):
    unittest.main()