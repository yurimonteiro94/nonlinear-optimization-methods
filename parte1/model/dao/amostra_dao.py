from model.entidades.amostra import Amostra
from services.constantes import Constantes
from services.ferramentas import Ferramentas
from services.gerenciador_csv import GerenciadorCsv

class AmostraDAO:

    __listaDeAmostrasDeTreinamento = []
    __listaDeAmostrasDeTeste = []

    @staticmethod
    def retornarAmostra(listaDeValores):
        quantidadeDeValores = len(listaDeValores)

        if(quantidadeDeValores != Constantes.QUANTIDADE_DE_COLUNAS_DA_LINHA_PROCESSADA):
            return None

        listaDeValoresSemEspacos = Ferramentas.retornarListaDeValoresSemEspacos(listaDeValores)

        textoDoIdentificador = listaDeValoresSemEspacos[Constantes.INDICE_DO_IDENTIFICADOR_NA_LINHA_ORIGINAL]
        textoDaData = listaDeValoresSemEspacos[Constantes.INDICE_DA_DATA_NA_LINHA_ORIGINAL]
        textoDaTemperatura = listaDeValoresSemEspacos[Constantes.INDICE_DA_TEMPERATURA_NA_LINHA_ORIGINAL]
        textoDaUmidade = listaDeValoresSemEspacos[Constantes.INDICE_DA_UMIDADE_NA_LINHA_ORIGINAL]
        textoDaLuminosidade = listaDeValoresSemEspacos[Constantes.INDICE_DA_LUMINOSIDADE_NA_LINHA_ORIGINAL]
        textoDoCo2 = listaDeValoresSemEspacos[Constantes.INDICE_DO_CO2_NA_LINHA_ORIGINAL]
        textoDaRazaoDeUmidade = listaDeValoresSemEspacos[Constantes.INDICE_DA_RAZAO_DE_UMIDADE_NA_LINHA_ORIGINAL]
        textoDaOcupacao = listaDeValoresSemEspacos[Constantes.INDICE_DA_OCUPACAO_NA_LINHA_ORIGINAL]

        if(not Ferramentas.identificadorEhValido(textoDoIdentificador)):
            return None

        elif(not Ferramentas.dataEhValida(textoDaData)):
            return None

        elif(not Ferramentas.numeroRealEhValido(textoDaTemperatura)):
            return None

        elif(not Ferramentas.numeroRealEhValido(textoDaUmidade)):
            return None

        elif(not Ferramentas.numeroRealEhValido(textoDaLuminosidade)):
            return None

        elif(not Ferramentas.numeroRealEhValido(textoDoCo2)):
            return None

        elif(not Ferramentas.numeroRealEhValido(textoDaRazaoDeUmidade)):
            return None

        elif(not Ferramentas.ocupacaoEhValida(textoDaOcupacao)):
            return None

        identificador = Ferramentas.retornarNumeroInteiro(textoDoIdentificador)
        data = Ferramentas.retornarData(textoDaData)
        temperatura = Ferramentas.retornarNumeroReal(textoDaTemperatura)
        umidade = Ferramentas.retornarNumeroReal(textoDaUmidade)
        luminosidade = Ferramentas.retornarNumeroReal(textoDaLuminosidade)
        co2 = Ferramentas.retornarNumeroReal(textoDoCo2)
        razaoDeUmidade = Ferramentas.retornarNumeroReal(textoDaRazaoDeUmidade)
        ocupacao = Ferramentas.retornarNumeroInteiro(textoDaOcupacao)

        return Amostra(identificador, data, temperatura, umidade, luminosidade, co2, razaoDeUmidade, ocupacao)

    @staticmethod
    def retornarListaDeAmostras(caminhoDoArquivo):
        listaDeLinhas = GerenciadorCsv.retornarListaDeLinhas(caminhoDoArquivo)

        if(listaDeLinhas is None):
            return None

        quantidadeDeLinhas = len(listaDeLinhas)

        if(quantidadeDeLinhas < Constantes.QUANTIDADE_MINIMA_DE_LINHAS_DO_ARQUIVO):
            return None

        listaDeCabecalho = listaDeLinhas[Constantes.INDICE_DO_CABECALHO]
        cabecalhoOriginalEhValido = Ferramentas.cabecalhoEhValido(listaDeCabecalho, Constantes.listaDeCabecalhoOriginal)
        cabecalhoProcessadoEhValido = Ferramentas.cabecalhoEhValido(listaDeCabecalho, Constantes.listaDeCabecalhoProcessado)

        if((not cabecalhoOriginalEhValido) and (not cabecalhoProcessadoEhValido)):
            return None

        listaDeAmostras = []
        indiceDaLinha = Constantes.INDICE_DA_PRIMEIRA_LINHA_DE_DADOS

        while(indiceDaLinha < quantidadeDeLinhas):
            listaDeValoresDaLinha = listaDeLinhas[indiceDaLinha]

            if(not Ferramentas.linhaEhVazia(listaDeValoresDaLinha)):
                amostra = AmostraDAO.retornarAmostra(listaDeValoresDaLinha)

                if(amostra is None):
                    return None

                listaDeAmostras.append(amostra)

            indiceDaLinha = indiceDaLinha + Constantes.INCREMENTO_UNITARIO

        if(len(listaDeAmostras) == Constantes.QUANTIDADE_NULA):
            return None

        return listaDeAmostras

    @staticmethod
    def carregarListaDeAmostrasDeTreinamento():
        listaDeAmostrasDeTreinamento = AmostraDAO.retornarListaDeAmostras(Constantes.CAMINHO_DO_ARQUIVO_DE_TREINAMENTO_PROCESSADO)

        if(listaDeAmostrasDeTreinamento is None):
            AmostraDAO.__listaDeAmostrasDeTreinamento = []
            return False

        AmostraDAO.__listaDeAmostrasDeTreinamento = listaDeAmostrasDeTreinamento

        return True

    @staticmethod
    def carregarListaDeAmostrasDeTeste():
        listaDeAmostrasDeTeste = AmostraDAO.retornarListaDeAmostras(Constantes.CAMINHO_DO_ARQUIVO_DE_TESTE_PROCESSADO)

        if(listaDeAmostrasDeTeste is None):
            AmostraDAO.__listaDeAmostrasDeTeste = []
            return False

        AmostraDAO.__listaDeAmostrasDeTeste = listaDeAmostrasDeTeste

        return True

    @staticmethod
    def retornarListaDeAmostrasDeTreinamento():
        return AmostraDAO.__listaDeAmostrasDeTreinamento

    @staticmethod
    def retornarListaDeAmostrasDeTeste():
        return AmostraDAO.__listaDeAmostrasDeTeste