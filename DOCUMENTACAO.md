# Documentação Técnica

## Introdução

Este documento descreve a organização interna do projeto, a responsabilidade de cada módulo e as principais decisões adotadas durante o desenvolvimento.

O objetivo não é explicar a teoria dos algoritmos implementados, mas sim documentar a estrutura do software, facilitando sua compreensão, manutenção e evolução.

---

# Arquitetura

O projeto foi organizado em módulos independentes, procurando separar as diferentes responsabilidades da aplicação.

A estrutura adotada é inspirada no padrão Model-View-Controller (MVC). Embora o projeto seja relativamente pequeno, essa organização facilita a reutilização de código, reduz o acoplamento entre componentes e torna a manutenção mais simples.

Cada módulo possui uma responsabilidade específica, evitando que uma mesma classe acumule funções distintas.

---

# Organização dos diretórios

## controller

Os controladores coordenam a execução das funcionalidades do sistema.

Seu papel é receber as solicitações da aplicação, utilizar os serviços necessários e encaminhar os resultados para a camada de visualização.

Nenhuma regra de negócio é implementada nesta camada.

---

## model

Contém as entidades utilizadas durante a execução dos algoritmos.

Também inclui os componentes responsáveis pela leitura e carregamento dos conjuntos de dados utilizados nos experimentos.

As entidades representam apenas dados e não implementam algoritmos.

---

## services

Esta é a principal camada do projeto.

Nela encontram-se as implementações dos algoritmos estudados na disciplina, além das funções auxiliares utilizadas durante os experimentos.

Cada algoritmo foi implementado em uma classe independente, permitindo reutilização e comparação entre diferentes métodos.

---

## view

Responsável exclusivamente pela apresentação dos resultados.

Nesta camada são gerados gráficos, tabelas, arquivos CSV e textos utilizados para resumir os experimentos.

Essa separação permite modificar a forma de apresentação sem alterar a implementação dos algoritmos.

---

## test

Reúne todos os testes automatizados desenvolvidos para o projeto.

Os testes verificam tanto o funcionamento individual das classes quanto a integração entre os diferentes módulos.

---

# Fluxo de execução

A execução do programa começa nos arquivos principais (`main.py` e `main_parte_2.py`).

Os controladores inicializam os experimentos e acionam os serviços necessários.

Os serviços executam os algoritmos utilizando as entidades definidas na camada de modelo.

Ao término da execução, os resultados são enviados para a camada de visualização, responsável pela geração de gráficos, tabelas e resumos.

---

# Organização dos algoritmos

Cada algoritmo foi implementado de forma independente.

Essa decisão permite comparar diferentes métodos sem modificar a estrutura do restante da aplicação.

Sempre que possível, os algoritmos compartilham estruturas de dados e classes auxiliares já existentes, evitando duplicação de código.

---

# Testes automatizados

O projeto utiliza o módulo `unittest` da biblioteca padrão do Python.

Os testes foram organizados seguindo a mesma estrutura do projeto, permitindo localizar facilmente os testes correspondentes a cada componente.

Sempre que novas funcionalidades foram adicionadas, seus respectivos testes também foram implementados.

---

# Convenções adotadas

Durante o desenvolvimento foram adotadas algumas convenções para manter uniformidade em todo o projeto.

Entre elas destacam-se:

- separação entre lógica de negócio e apresentação dos resultados;

- utilização de classes com responsabilidade única;

- reutilização de componentes sempre que possível;

- implementação de testes automatizados para os principais módulos;

- padronização da organização dos diretórios;

- utilização de nomes descritivos para classes, métodos e variáveis.

Além disso, optou-se por manter o código-fonte sem comentários desnecessários.

Em vez de comentários distribuídos ao longo da implementação, a documentação foi concentrada neste documento e no README do projeto. Essa abordagem evita redundâncias e facilita a manutenção da documentação ao longo da evolução do software.

---

# Considerações finais

O projeto foi desenvolvido buscando equilibrar simplicidade, organização e facilidade de manutenção.

A arquitetura modular permitiu implementar diferentes algoritmos utilizando uma estrutura comum, favorecendo tanto a reutilização de código quanto a realização dos experimentos propostos na disciplina.

A documentação apresentada neste arquivo complementa o README do repositório, enquanto os aspectos matemáticos e experimentais são discutidos no relatório da disciplina.