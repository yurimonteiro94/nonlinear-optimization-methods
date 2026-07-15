import os
import tempfile
import unittest

from model.entidades.configuracao_do_treinamento import ConfiguracaoDoTreinamento
from model.entidades.resultado_do_treinamento import ResultadoDoTreinamento
from view.view_exercicio_1 import ViewExercicio1


class TestViewExercicio1(unittest.TestCase):

    def testSalvamentoDoGrafico(self):
        with tempfile.TemporaryDirectory() as pastaTemporaria:
            caminhoDoArquivo = pastaTemporaria + os.sep + "grafico.png"

            resultado = ViewExercicio1.salvarGrafico([1.0, 0.8, 0.5], "Título", "X", "Y", caminhoDoArquivo)

            self.assertTrue(resultado)
            self.assertTrue(os.path.exists(caminhoDoArquivo))

    def testRetornoDoTextoDoResumo(self):
        resultadoDoTreinamento = ResultadoDoTreinamento()
        resultadoDoTreinamento.setListaDaFuncaoObjetivo([1.0, 0.5])
        resultadoDoTreinamento.setListaDaNormaDoGradiente([0.8, 0.2])
        resultadoDoTreinamento.setQuantidadeDeIteracoes(2)
        resultadoDoTreinamento.setTempoComputacional(0.1)
        resultadoDoTreinamento.setAcuracia(0.9)
        resultadoDoTreinamento.setMotivoDaParada("Teste")

        configuracao = ConfiguracaoDoTreinamento(0.1, 1.0e-6, 1000, 32, 0.9, True)

        texto = ViewExercicio1.retornarTextoDoResumo(resultadoDoTreinamento, 0.85, configuracao)

        self.assertIsNotNone(texto)
        self.assertIn("Steepest Descent", texto)
        self.assertIn("Acurácia de treinamento", texto)
        self.assertIn("Acurácia de teste", texto)

    def testRetornoParaListaDeValoresVazia(self):
        with tempfile.TemporaryDirectory() as pastaTemporaria:
            caminhoDoArquivo = pastaTemporaria + os.sep + "grafico.png"

            resultado = ViewExercicio1.salvarGrafico([], "Título", "X", "Y", caminhoDoArquivo)

            self.assertFalse(resultado)


if(__name__ == "__main__"):
    unittest.main()