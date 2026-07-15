import math

from services.constantes import Constantes


class GerenciadorDeAmostras:

    @staticmethod
    def retornarListaDeCaracteristicas(amostra):
        if(amostra is None):
            return None

        listaDeCaracteristicas = []

        listaDeCaracteristicas.append(amostra.getTemperatura())
        listaDeCaracteristicas.append(amostra.getUmidade())
        listaDeCaracteristicas.append(amostra.getLuminosidade())
        listaDeCaracteristicas.append(amostra.getCo2())
        listaDeCaracteristicas.append(amostra.getRazaoDeUmidade())

        return listaDeCaracteristicas

    @staticmethod
    def retornarListaDeMedias(listaDeAmostras):
        if(listaDeAmostras is None):
            return None

        elif(len(listaDeAmostras) == Constantes.QUANTIDADE_NULA):
            return None

        listaDeCaracteristicasDaPrimeiraAmostra = GerenciadorDeAmostras.retornarListaDeCaracteristicas(listaDeAmostras[Constantes.INDICE_INICIAL])

        if(listaDeCaracteristicasDaPrimeiraAmostra is None):
            return None

        quantidadeDeCaracteristicas = len(listaDeCaracteristicasDaPrimeiraAmostra)
        listaDeSomas = []
        indiceDaCaracteristica = Constantes.INDICE_INICIAL

        while(indiceDaCaracteristica < quantidadeDeCaracteristicas):
            listaDeSomas.append(Constantes.QUANTIDADE_NULA)
            indiceDaCaracteristica = indiceDaCaracteristica + Constantes.INCREMENTO_UNITARIO

        indiceDaAmostra = Constantes.INDICE_INICIAL
        quantidadeDeAmostras = len(listaDeAmostras)

        while(indiceDaAmostra < quantidadeDeAmostras):
            listaDeCaracteristicas = GerenciadorDeAmostras.retornarListaDeCaracteristicas(listaDeAmostras[indiceDaAmostra])

            if(listaDeCaracteristicas is None):
                return None

            elif(len(listaDeCaracteristicas) != quantidadeDeCaracteristicas):
                return None

            indiceDaCaracteristica = Constantes.INDICE_INICIAL

            while(indiceDaCaracteristica < quantidadeDeCaracteristicas):
                listaDeSomas[indiceDaCaracteristica] = listaDeSomas[indiceDaCaracteristica] + listaDeCaracteristicas[indiceDaCaracteristica]
                indiceDaCaracteristica = indiceDaCaracteristica + Constantes.INCREMENTO_UNITARIO

            indiceDaAmostra = indiceDaAmostra + Constantes.INCREMENTO_UNITARIO

        listaDeMedias = []
        indiceDaCaracteristica = Constantes.INDICE_INICIAL

        while(indiceDaCaracteristica < quantidadeDeCaracteristicas):
            media = listaDeSomas[indiceDaCaracteristica] / quantidadeDeAmostras
            listaDeMedias.append(media)
            indiceDaCaracteristica = indiceDaCaracteristica + Constantes.INCREMENTO_UNITARIO

        return listaDeMedias

    @staticmethod
    def retornarListaDeDesviosPadrao(listaDeAmostras, listaDeMedias):
        if(listaDeAmostras is None):
            return None

        elif(listaDeMedias is None):
            return None

        elif(len(listaDeAmostras) == Constantes.QUANTIDADE_NULA):
            return None

        elif(len(listaDeMedias) == Constantes.QUANTIDADE_NULA):
            return None

        quantidadeDeCaracteristicas = len(listaDeMedias)
        listaDeSomasDosQuadrados = []
        indiceDaCaracteristica = Constantes.INDICE_INICIAL

        while(indiceDaCaracteristica < quantidadeDeCaracteristicas):
            listaDeSomasDosQuadrados.append(Constantes.QUANTIDADE_NULA)
            indiceDaCaracteristica = indiceDaCaracteristica + Constantes.INCREMENTO_UNITARIO

        indiceDaAmostra = Constantes.INDICE_INICIAL
        quantidadeDeAmostras = len(listaDeAmostras)

        while(indiceDaAmostra < quantidadeDeAmostras):
            listaDeCaracteristicas = GerenciadorDeAmostras.retornarListaDeCaracteristicas(listaDeAmostras[indiceDaAmostra])

            if(listaDeCaracteristicas is None):
                return None

            elif(len(listaDeCaracteristicas) != quantidadeDeCaracteristicas):
                return None

            indiceDaCaracteristica = Constantes.INDICE_INICIAL

            while(indiceDaCaracteristica < quantidadeDeCaracteristicas):
                diferenca = listaDeCaracteristicas[indiceDaCaracteristica] - listaDeMedias[indiceDaCaracteristica]
                listaDeSomasDosQuadrados[indiceDaCaracteristica] = listaDeSomasDosQuadrados[indiceDaCaracteristica] + diferenca * diferenca
                indiceDaCaracteristica = indiceDaCaracteristica + Constantes.INCREMENTO_UNITARIO

            indiceDaAmostra = indiceDaAmostra + Constantes.INCREMENTO_UNITARIO

        listaDeDesviosPadrao = []
        indiceDaCaracteristica = Constantes.INDICE_INICIAL

        while(indiceDaCaracteristica < quantidadeDeCaracteristicas):
            variancia = listaDeSomasDosQuadrados[indiceDaCaracteristica] / quantidadeDeAmostras
            desvioPadrao = math.sqrt(variancia)
            listaDeDesviosPadrao.append(desvioPadrao)
            indiceDaCaracteristica = indiceDaCaracteristica + Constantes.INCREMENTO_UNITARIO

        return listaDeDesviosPadrao

    @staticmethod
    def retornarListaDeCaracteristicasNormalizadas(amostra, listaDeMedias, listaDeDesviosPadrao):
        if(amostra is None):
            return None

        elif(listaDeMedias is None):
            return None

        elif(listaDeDesviosPadrao is None):
            return None

        elif(len(listaDeMedias) != len(listaDeDesviosPadrao)):
            return None

        listaDeCaracteristicas = GerenciadorDeAmostras.retornarListaDeCaracteristicas(amostra)

        if(listaDeCaracteristicas is None):
            return None

        elif(len(listaDeCaracteristicas) != len(listaDeMedias)):
            return None

        listaDeCaracteristicasNormalizadas = []
        indiceDaCaracteristica = Constantes.INDICE_INICIAL
        quantidadeDeCaracteristicas = len(listaDeCaracteristicas)

        while(indiceDaCaracteristica < quantidadeDeCaracteristicas):
            media = listaDeMedias[indiceDaCaracteristica]
            desvioPadrao = listaDeDesviosPadrao[indiceDaCaracteristica]
            valorDaCaracteristica = listaDeCaracteristicas[indiceDaCaracteristica]

            if(desvioPadrao == Constantes.QUANTIDADE_NULA):
                valorNormalizado = Constantes.QUANTIDADE_NULA
            else:
                valorNormalizado = (valorDaCaracteristica - media) / desvioPadrao

            listaDeCaracteristicasNormalizadas.append(valorNormalizado)
            indiceDaCaracteristica = indiceDaCaracteristica + Constantes.INCREMENTO_UNITARIO

        return listaDeCaracteristicasNormalizadas

    @staticmethod
    def retornarListaDeEntradasNormalizadas(listaDeAmostras, listaDeMedias, listaDeDesviosPadrao):
        if(listaDeAmostras is None):
            return None

        elif(listaDeMedias is None):
            return None

        elif(listaDeDesviosPadrao is None):
            return None

        elif(len(listaDeAmostras) == Constantes.QUANTIDADE_NULA):
            return None

        listaDeEntradasNormalizadas = []
        indiceDaAmostra = Constantes.INDICE_INICIAL
        quantidadeDeAmostras = len(listaDeAmostras)

        while(indiceDaAmostra < quantidadeDeAmostras):
            listaDeCaracteristicasNormalizadas = GerenciadorDeAmostras.retornarListaDeCaracteristicasNormalizadas(listaDeAmostras[indiceDaAmostra], listaDeMedias, listaDeDesviosPadrao)

            if(listaDeCaracteristicasNormalizadas is None):
                return None

            listaDeEntradasNormalizadas.append(listaDeCaracteristicasNormalizadas)
            indiceDaAmostra = indiceDaAmostra + Constantes.INCREMENTO_UNITARIO

        return listaDeEntradasNormalizadas

    @staticmethod
    def retornarListaDeSaidasEsperadas(listaDeAmostras):
        if(listaDeAmostras is None):
            return None

        elif(len(listaDeAmostras) == Constantes.QUANTIDADE_NULA):
            return None

        listaDeSaidasEsperadas = []
        indiceDaAmostra = Constantes.INDICE_INICIAL
        quantidadeDeAmostras = len(listaDeAmostras)

        while(indiceDaAmostra < quantidadeDeAmostras):
            saidaEsperada = listaDeAmostras[indiceDaAmostra].getOcupacao()
            listaDeSaidasEsperadas.append(saidaEsperada)
            indiceDaAmostra = indiceDaAmostra + Constantes.INCREMENTO_UNITARIO

        return listaDeSaidasEsperadas