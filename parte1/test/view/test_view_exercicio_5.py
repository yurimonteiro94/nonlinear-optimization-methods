import os
import tempfile
import unittest

from model.entidades.funcao_quadratica import FuncaoQuadratica
from model.entidades.resultado_otimizacao import ResultadoOtimizacao
from view.view_exercicio_5 import ViewExercicio5


class TestViewExercicio5(unittest.TestCase):

    def retornarResultadoDaOtimizacao(self):
        resultado = ResultadoOtimizacao()

        resultado.setPontoFinal([1.0, 3.0, 1.0, 3.0])
        resultado.setListaDePontos([
            [3.0, -5.0, 3.0, -5.0],
            [1.0, 3.0, 1.0, 3.0]
        ])
        resultado.setListaDaFuncaoObjetivo([100.0, 0.0])
        resultado.setListaDaNormaDoGradiente([10.0, 0.0])
        resultado.setQuantidadeDeIteracoes(1)
        resultado.setTempoComputacional(0.01)
        resultado.setMotivoDaParada("Teste")

        return resultado

    def testRetornoDoTextoDoResumo(self):
        funcaoQuadratica = FuncaoQuadratica(
            [
                [2.0, -1.8, 0.0, 0.0],
                [-1.8, 4.0, -1.8, 0.0],
                [0.0, -1.8, 4.0, -1.8],
                [0.0, 0.0, -1.8, 2.0]
            ],
            [3.4, -8.4, 6.8, -4.2],
            13.8
        )

        texto = ViewExercicio5.retornarTextoDoResumo(
            "Teste",
            funcaoQuadratica,
            self.retornarResultadoDaOtimizacao()
        )

        self.assertIsNotNone(texto)
        self.assertIn("Exercício 5", texto)
        self.assertIn("Número de condição", texto)

    def testSalvamentoDoGraficoDasCoordenadas(self):
        with tempfile.TemporaryDirectory() as pastaTemporaria:
            caminhoDoArquivo = pastaTemporaria + os.sep + "coordenadas.png"

            resultado = ViewExercicio5.salvarGraficoDasCoordenadas(
                self.retornarResultadoDaOtimizacao().getListaDePontos(),
                "Teste",
                caminhoDoArquivo
            )

            self.assertTrue(resultado)
            self.assertTrue(os.path.exists(caminhoDoArquivo))

    def testSalvamentoDoGraficoDeValores(self):
        with tempfile.TemporaryDirectory() as pastaTemporaria:
            caminhoDoArquivo = pastaTemporaria + os.sep + "valores.png"

            resultado = ViewExercicio5.salvarGraficoDeValores(
                [10.0, 5.0, 1.0],
                "Teste",
                "Valor",
                caminhoDoArquivo
            )

            self.assertTrue(resultado)
            self.assertTrue(os.path.exists(caminhoDoArquivo))

    def testRetornoParaListaDePontosVazia(self):
        resultado = ViewExercicio5.salvarGraficoDasCoordenadas(
            [],
            "Teste",
            "teste.png"
        )

        self.assertFalse(resultado)


if(__name__ == "__main__"):
    unittest.main()