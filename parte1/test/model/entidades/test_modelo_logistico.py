import unittest

from model.entidades.modelo_logistico import ModeloLogistico


class TestModeloLogistico(unittest.TestCase):

    def testCriacaoDoModeloLogistico(self):
        listaDePesos = [0.0, 0.0, 0.0, 0.0, 0.0]
        vies = 0.0

        modeloLogistico = ModeloLogistico(listaDePesos, vies)

        self.assertEqual(modeloLogistico.getListaDePesos(), listaDePesos)
        self.assertEqual(modeloLogistico.getVies(), vies)

    def testAlteracaoDaListaDePesos(self):
        modeloLogistico = ModeloLogistico([0.0, 0.0, 0.0, 0.0, 0.0], 0.0)
        novaListaDePesos = [1.0, 2.0, 3.0, 4.0, 5.0]

        modeloLogistico.setListaDePesos(novaListaDePesos)

        self.assertEqual(modeloLogistico.getListaDePesos(), novaListaDePesos)

    def testAlteracaoDoVies(self):
        modeloLogistico = ModeloLogistico([0.0, 0.0, 0.0, 0.0, 0.0], 0.0)
        novoVies = 1.5

        modeloLogistico.setVies(novoVies)

        self.assertEqual(modeloLogistico.getVies(), novoVies)


if(__name__ == "__main__"):
    unittest.main()