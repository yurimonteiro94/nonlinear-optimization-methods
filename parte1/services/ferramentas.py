import math
from datetime import datetime

from services.constantes import Constantes


class Ferramentas:

    @staticmethod
    def retornarListaDeValoresSemEspacos(listaDeValores):
        listaDeValoresSemEspacos = []
        indiceDoValor = Constantes.INDICE_INICIAL
        quantidadeDeValores = len(listaDeValores)

        while(indiceDoValor < quantidadeDeValores):
            valorSemEspacos = listaDeValores[indiceDoValor].strip()
            listaDeValoresSemEspacos.append(valorSemEspacos)
            indiceDoValor = indiceDoValor + Constantes.INCREMENTO_UNITARIO

        return listaDeValoresSemEspacos

    @staticmethod
    def linhaEhVazia(listaDeValoresDaLinha):
        indiceDoValor = Constantes.INDICE_INICIAL
        quantidadeDeValores = len(listaDeValoresDaLinha)

        while(indiceDoValor < quantidadeDeValores):
            valorDaLinha = listaDeValoresDaLinha[indiceDoValor].strip()

            if(valorDaLinha != Constantes.TEXTO_VAZIO):
                return False

            indiceDoValor = indiceDoValor + Constantes.INCREMENTO_UNITARIO

        return True

    @staticmethod
    def cabecalhoEhValido(listaDeCabecalhoRecebido, listaDeCabecalhoEsperado):
        listaDeCabecalhoSemEspacos = Ferramentas.retornarListaDeValoresSemEspacos(listaDeCabecalhoRecebido)

        quantidadeDeColunasRecebidas = len(listaDeCabecalhoSemEspacos)
        quantidadeDeColunasEsperadas = len(listaDeCabecalhoEsperado)

        if(quantidadeDeColunasRecebidas != quantidadeDeColunasEsperadas):
            return False

        indiceDaColuna = Constantes.INDICE_INICIAL

        while(indiceDaColuna < quantidadeDeColunasEsperadas):
            valorRecebido = listaDeCabecalhoSemEspacos[indiceDaColuna]
            valorEsperado = listaDeCabecalhoEsperado[indiceDaColuna]

            if(valorRecebido != valorEsperado):
                return False

            indiceDaColuna = indiceDaColuna + Constantes.INCREMENTO_UNITARIO

        return True

    @staticmethod
    def retornarData(textoDaData):
        try:
            data = datetime.strptime(textoDaData, Constantes.FORMATO_DA_DATA)
        except:
            return None

        return data

    @staticmethod
    def dataEhValida(textoDaData):
        data = Ferramentas.retornarData(textoDaData)

        if(data is None):
            return False

        return True

    @staticmethod
    def retornarNumeroReal(textoDoNumero):
        try:
            numeroReal = float(textoDoNumero)
        except:
            return None

        if(not math.isfinite(numeroReal)):
            return None

        return numeroReal

    @staticmethod
    def numeroRealEhValido(textoDoNumero):
        numeroReal = Ferramentas.retornarNumeroReal(textoDoNumero)

        if(numeroReal is None):
            return False

        return True

    @staticmethod
    def retornarNumeroInteiro(textoDoNumero):
        try:
            numeroInteiro = int(textoDoNumero)
        except:
            return None

        return numeroInteiro

    @staticmethod
    def identificadorEhValido(textoDoIdentificador):
        identificador = Ferramentas.retornarNumeroInteiro(textoDoIdentificador)

        if(identificador is None):
            return False

        elif(identificador < Constantes.PRIMEIRO_IDENTIFICADOR):
            return False

        return True

    @staticmethod
    def ocupacaoEhValida(textoDaOcupacao):
        ocupacao = Ferramentas.retornarNumeroInteiro(textoDaOcupacao)

        if(ocupacao is None):
            return False

        elif(ocupacao == Constantes.OCUPACAO_VAZIA):
            return True

        elif(ocupacao == Constantes.OCUPACAO_PRESENTE):
            return True

        return False

    @staticmethod
    def retornarListaDeUniao(listaDePrimeirosValores, listaDeSegundosValores):
        listaDeValoresUnidos = []

        indiceDoValor = Constantes.INDICE_INICIAL
        quantidadeDePrimeirosValores = len(listaDePrimeirosValores)

        while(indiceDoValor < quantidadeDePrimeirosValores):
            listaDeValoresUnidos.append(listaDePrimeirosValores[indiceDoValor])
            indiceDoValor = indiceDoValor + Constantes.INCREMENTO_UNITARIO

        indiceDoValor = Constantes.INDICE_INICIAL
        quantidadeDeSegundosValores = len(listaDeSegundosValores)

        while(indiceDoValor < quantidadeDeSegundosValores):
            listaDeValoresUnidos.append(listaDeSegundosValores[indiceDoValor])
            indiceDoValor = indiceDoValor + Constantes.INCREMENTO_UNITARIO

        return listaDeValoresUnidos

    @staticmethod
    def retornarListaDeSubconjunto(listaDeValores, indiceInicial, indiceFinal):
        listaDeSubconjunto = []
        indiceDoValor = indiceInicial

        while(indiceDoValor < indiceFinal):
            listaDeSubconjunto.append(listaDeValores[indiceDoValor])
            indiceDoValor = indiceDoValor + Constantes.INCREMENTO_UNITARIO

        return listaDeSubconjunto