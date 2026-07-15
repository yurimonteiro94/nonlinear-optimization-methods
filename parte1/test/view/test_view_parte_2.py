import os
import tempfile
import unittest

from model.entidades.funcao_quadratica import FuncaoQuadratica
from model.entidades.resultado_otimizacao import ResultadoOtimizacao
from services.constantes_parte_2 import ConstantesParte2
from view.view_parte_2 import ViewParte2


class TestViewParte2(unittest.TestCase):

    def retornarResultado(self):
        resultado = ResultadoOtimizacao()
        resultado.setPontoFinal([1.0, 2.0])
        resultado.setListaDePontos([[0.0, 0.0], [1.0, 2.0]])
        resultado.setListaDaFuncaoObjetivo([0.0, -9.0])
        resultado.setListaDaNormaDoGradiente([8.0, 0.0])
        resultado.setQuantidadeDeIteracoes(1)
        resultado.setTempoComputacional(0.01)
        resultado.setMotivoDaParada(ConstantesParte2.MOTIVO_DA_PARADA_POR_NORMA_DO_GRADIENTE)

        return resultado

    def testRetornoDoTextoDoResumo(self):
        funcaoQuadratica = FuncaoQuadratica([[2.0, 0.0], [0.0, 4.0]], [-2.0, -8.0], 0.0)

        texto = ViewParte2.retornarTextoDoResumo("Teste", funcaoQuadratica, self.retornarResultado())

        self.assertIsNotNone(texto)
        self.assertIn("Ponto final", texto)
        self.assertIn("Número de condição", texto)

    def testSalvamentoDoGraficoDeValores(self):
        with tempfile.TemporaryDirectory() as pastaTemporaria:
            caminhoDoArquivo = pastaTemporaria + os.sep + "grafico.png"

            resultado = ViewParte2.salvarGraficoDeValores([10.0, 5.0, 1.0], "Teste", "Valor", caminhoDoArquivo)

            self.assertTrue(resultado)
            self.assertTrue(os.path.exists(caminhoDoArquivo))

    def testSalvamentoDoTexto(self):
        with tempfile.TemporaryDirectory() as pastaTemporaria:
            caminhoDoArquivo = pastaTemporaria + os.sep + "resultado.txt"

            resultado = ViewParte2.salvarTexto("Teste", caminhoDoArquivo)

            self.assertTrue(resultado)
            self.assertTrue(os.path.exists(caminhoDoArquivo))

    def testRetornoParaListaDeValoresVazia(self):
        resultado = ViewParte2.salvarGraficoDeValores([], "Teste", "Valor", "grafico.png")

        self.assertFalse(resultado)


if(__name__ == "__main__"):
    unittest.main()