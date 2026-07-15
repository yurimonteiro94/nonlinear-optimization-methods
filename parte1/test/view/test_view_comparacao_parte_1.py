import os
import tempfile
import unittest

from model.entidades.resultado_do_treinamento import ResultadoDoTreinamento
from services.constantes import Constantes
from view.view_comparacao_parte_1 import ViewComparacaoParte1


class TestViewComparacaoParte1(unittest.TestCase):

    def retornarLinhaDoResultado(self):
        resultado = ResultadoDoTreinamento()
        resultado.setListaDaFuncaoObjetivo([1.0, 0.5])
        resultado.setListaDaAcuracia([0.5, 0.9])
        resultado.setQuantidadeDeIteracoes(2)
        resultado.setTempoComputacional(0.1)
        resultado.setAcuracia(0.9)

        return ["Teste", 0.1, 32, 0.9, 2, 0.1, 0.5, 0.9, 0.85, resultado]

    def testRetornoDoTextoDaLinhaCsv(self):
        texto = ViewComparacaoParte1.retornarTextoDaLinhaCsv(self.retornarLinhaDoResultado())

        self.assertIsNotNone(texto)
        self.assertIn("Teste", texto)
        self.assertIn("0.85", texto)

    def testSalvamentoDaTabela(self):
        with tempfile.TemporaryDirectory() as pastaTemporaria:
            caminhoDoArquivo = pastaTemporaria + os.sep + "tabela.csv"

            resultado = ViewComparacaoParte1.salvarTabela([self.retornarLinhaDoResultado()], caminhoDoArquivo)

            self.assertTrue(resultado)
            self.assertTrue(os.path.exists(caminhoDoArquivo))

    def testRetornoDoResumo(self):
        texto = ViewComparacaoParte1.retornarTextoDoResumo([self.retornarLinhaDoResultado()])

        self.assertIsNotNone(texto)
        self.assertIn("Resumo da Parte 1", texto)
        self.assertIn("Método com maior acurácia", texto)

    def testRetornoParaListaNula(self):
        texto = ViewComparacaoParte1.retornarTextoDoResumo(None)

        self.assertIsNone(texto)


if(__name__ == "__main__"):
    unittest.main()