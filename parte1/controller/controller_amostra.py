from model.dao.amostra_dao import AmostraDAO
from services.gerenciador_de_amostras import GerenciadorDeAmostras


class ControllerAmostra:

    @staticmethod
    def carregarListaDeAmostrasDeTreinamento():
        return AmostraDAO.carregarListaDeAmostrasDeTreinamento()

    @staticmethod
    def carregarListaDeAmostrasDeTeste():
        return AmostraDAO.carregarListaDeAmostrasDeTeste()

    @staticmethod
    def retornarListaDeAmostrasDeTreinamento():
        return AmostraDAO.retornarListaDeAmostrasDeTreinamento()

    @staticmethod
    def retornarListaDeAmostrasDeTeste():
        return AmostraDAO.retornarListaDeAmostrasDeTeste()

    @staticmethod
    def retornarListaDeCaracteristicas(amostra):
        return GerenciadorDeAmostras.retornarListaDeCaracteristicas(amostra)

    @staticmethod
    def retornarListaDeMedias(listaDeAmostras):
        return GerenciadorDeAmostras.retornarListaDeMedias(listaDeAmostras)

    @staticmethod
    def retornarListaDeDesviosPadrao(listaDeAmostras, listaDeMedias):
        return GerenciadorDeAmostras.retornarListaDeDesviosPadrao(listaDeAmostras,listaDeMedias)

    @staticmethod
    def retornarListaDeCaracteristicasNormalizadas(amostra,listaDeMedias,listaDeDesviosPadrao):
        return GerenciadorDeAmostras.retornarListaDeCaracteristicasNormalizadas(amostra,listaDeMedias,listaDeDesviosPadrao)

    @staticmethod
    def retornarListaDeEntradasNormalizadas(listaDeAmostras,listaDeMedias,listaDeDesviosPadrao):
        return GerenciadorDeAmostras.retornarListaDeEntradasNormalizadas(listaDeAmostras,listaDeMedias,listaDeDesviosPadrao)

    @staticmethod
    def retornarListaDeSaidasEsperadas(listaDeAmostras):
        return GerenciadorDeAmostras.retornarListaDeSaidasEsperadas(listaDeAmostras)