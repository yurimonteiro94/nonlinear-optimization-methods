import csv

from services.constantes import Constantes


class GerenciadorCsv:

    @staticmethod
    def retornarListaDeLinhas(caminhoDoArquivo):
        listaDeLinhas = []

        try:
            with open(caminhoDoArquivo, Constantes.MODO_DE_LEITURA, newline=Constantes.TEXTO_VAZIO, encoding=Constantes.CODIFICACAO_DOS_ARQUIVOS_DE_ENTRADA) as arquivo:
                leitorCsv = csv.reader(arquivo, delimiter=Constantes.DELIMITADOR_CSV)
                leituraFoiConcluida = False

                while(not leituraFoiConcluida):
                    listaDeValoresDaLinha = next(leitorCsv, None)

                    if(listaDeValoresDaLinha is None):
                        leituraFoiConcluida = True
                    else:
                        listaDeLinhas.append(listaDeValoresDaLinha)
        except:
            return None

        quantidadeDeLinhas = len(listaDeLinhas)

        if(quantidadeDeLinhas == Constantes.QUANTIDADE_NULA):
            return None

        return listaDeLinhas

    @staticmethod
    def salvarListaDeLinhas(caminhoDoArquivo, listaDeLinhas):
        with open(caminhoDoArquivo, Constantes.MODO_DE_ESCRITA, newline=Constantes.TEXTO_VAZIO, encoding=Constantes.CODIFICACAO_DOS_ARQUIVOS_DE_SAIDA) as arquivo:
            gravadorCsv = csv.writer(arquivo, delimiter=Constantes.DELIMITADOR_CSV)
            indiceDaLinha = Constantes.INDICE_INICIAL
            quantidadeDeLinhas = len(listaDeLinhas)

            while(indiceDaLinha < quantidadeDeLinhas):
                gravadorCsv.writerow(listaDeLinhas[indiceDaLinha])
                indiceDaLinha = indiceDaLinha + Constantes.INCREMENTO_UNITARIO