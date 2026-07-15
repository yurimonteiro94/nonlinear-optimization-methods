# PRO6006Lista3

Este repositório contém a implementação dos algoritmos desenvolvidos na disciplina **PRO6006 – Programação Não Linear**.

O projeto foi implementado em Python e organizado de forma modular, separando as responsabilidades entre controle da aplicação, regras de negócio, entidades, visualização dos resultados e testes automatizados.

Além da implementação dos algoritmos, o projeto gera gráficos, tabelas e resultados utilizados durante os experimentos realizados na disciplina.

## Organização do projeto

O código está dividido em módulos independentes.

- **controller**: coordena a execução dos experimentos e faz a comunicação entre as demais camadas do sistema.

- **model**: contém as entidades utilizadas pela aplicação e os componentes responsáveis pelo acesso aos dados.

- **services**: reúne a implementação dos algoritmos, cálculos numéricos e demais regras de negócio.

- **view**: responsável pela geração de gráficos, tabelas e apresentação dos resultados.

- **test**: contém a suíte de testes automatizados.

- **dados**: armazena os conjuntos de dados utilizados pelos experimentos.

- **graficos**: guarda as figuras produzidas durante a execução dos algoritmos.

- **resultados**: armazena arquivos de saída gerados automaticamente.

## Dependências

As bibliotecas necessárias encontram-se no arquivo `requirements.txt`.

Para instalá-las, execute:

```bash
pip install -r requirements.txt
```

## Execução

A Parte 1 pode ser executada por meio do arquivo

```bash
python main.py
```

A Parte 2 pode ser executada por meio de

```bash
python main_parte_2.py
```

## Testes

Todos os testes automatizados podem ser executados com o comando

```bash
python -m unittest discover -s test -t . -p "test_*.py"
```

## Objetivos

O projeto foi desenvolvido com os seguintes objetivos:

- implementar os algoritmos estudados na disciplina;
- comparar o comportamento dos diferentes métodos de otimização;
- gerar automaticamente gráficos e resultados experimentais;
- validar a implementação por meio de testes automatizados.

## Documentação

Uma descrição mais detalhada da arquitetura, da organização do código e das principais decisões de desenvolvimento encontra-se no arquivo `DOCUMENTACAO.md`.