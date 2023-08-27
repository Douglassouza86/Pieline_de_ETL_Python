# Projeto de ETL para Cálculo de Métricas de Desempenho em Vendas

## Descrição do Projeto

Este projeto consiste na criação de um pipeline de ETL (Extração, Transformação e Carregamento) para calcular métricas de desempenho a partir de dados de vendas. Utilizando a linguagem de programação Python e a biblioteca Pandas, o projeto visa extrair informações de um arquivo CSV contendo dados de vendas, realizar transformações específicas e, em seguida, carregar os resultados transformados em um novo arquivo CSV.

## Etapas do Projeto

### Extração de Dados

O projeto começa com a extração de dados a partir de um arquivo CSV chamado `dados_vendas.csv`. Este arquivo contém informações sobre produtos vendidos, incluindo o ID do produto, nome do produto, quantidade vendida e receita gerada pelas vendas.

### Transformação de Dados

Durante a fase de transformação, o código lê os dados do arquivo CSV, calcula métricas de desempenho e adiciona essas métricas como colunas adicionais aos dados. As métricas calculadas incluem o preço unitário e a margem de lucro.

### Carregamento de Dados Transformados

Após a transformação dos dados, o código salva os resultados em um novo arquivo CSV chamado `metricas_desempenho.csv`. Este arquivo contém as métricas de desempenho calculadas, incluindo preço unitário e margem de lucro, que podem ser usadas para análises posteriores.

## Benefícios do Projeto

- **Demonstração de Habilidades**: O projeto demonstra a capacidade de criar um pipeline de ETL completo, desde a extração até o carregamento, usando a biblioteca Pandas em Python.
- **Aplicação Prática**: Através do cálculo das métricas de desempenho, o projeto ilustra como transformar dados brutos em informações úteis para tomada de decisões de negócios.

## Execução do Projeto

Para executar o projeto, siga os seguintes passos:

1. Certifique-se de ter o arquivo `dados_vendas.csv` no mesmo diretório do arquivo `ETL_CSV.py`.
2. Execute o arquivo `ETL_CSV.py` usando o Python para iniciar o pipeline de ETL.
3. Após a execução, o arquivo `metricas_desempenho.csv` conterá os resultados das métricas de desempenho calculadas.

O projeto não apenas demonstra conhecimentos técnicos, mas também fornece uma base sólida para explorar outras aplicações de ETL em diferentes domínios, como análise de mídias sociais, previsão de demanda e muito mais.
