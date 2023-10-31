<!-- Título -->
<h1 align="center">Gerador de dados fictícios para PostgreSQL e MongoDB</h1>

<!-- Descrição -->
<p align="justify">
  Uma aplicação para o povoamento de bancos de dados com informações fictícias, criadas de forma automática por meio da biblioteca "Faker", utilizando a linguagem de programação Python.
</p>

<!-- Tabela de Conteúdo -->
## Tabela de Conteúdo

- [Sobre o Projeto](#sobre-o-projeto)
- [Objetivo](#objetivo)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instruções de Uso](#instruções-de-uso)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Contribuições](#contribuições)

<!-- Sobre o Projeto -->
## Sobre o Projeto

<p align="justify">
Este algoritmo foi desenvolvido como parte do Trabalho de Conclusão de Curso (TCC) do curso de Sistemas de Informação ministrado na UniFacisa. A aplicação em Python utiliza a biblioteca Faker para gerar dados fictícios, como CPF e nome de funcionários, e salários e descrições de cargos, que são então inseridos em bancos de dados PostgreSQL e MongoDB.
</p>

### Objetivo

<p align="justify">
O principal objetivo do projeto é comparar o desempenho e a eficiência dos Sistemas de Gerenciamento de Banco de Dados (SGBDs) PostgreSQL e MongoDB ao realizarem operações de junção. Para isso, foi preciso criar tabelas (no caso do PostgreSQL) e coleções (no caso do MongoDB) com tamanho de armazenamento parecido, a fim de proporcionar condições equivalentes para ambos os bancos de dados durante a fase de testes. Além disso, para tornar as diferenças de desempenho entre ambos ainda mais evidentes, era preciso que esses bancos de dados consumissem considerável espaço de memória. Assim, o autor optou por convencionar que cada tabela e cada coleção atingiria um total de 1GB de armazenamento, proporcionando condições equivalentes de análise para as duas tecnologias. Por fim, tendo em vista que popular esses bancos de dados manualmente seria bastante custoso em termos de tempo e esforço, foram desenvolvidos os scripts presentes neste repositório com o intuito de automatizar o processo de criação das tabelas e das coleções, bem como o de inserção dos dados, tanto no PostgreSQL quanto no MongoDB, até que cada tabela e coleção atinja um total de 1GB de armazenamento.
</p>

<!-- Tecnologias Utilizadas -->
## Tecnologias Utilizadas

- Python
- Bibliotecas:
  - Faker: (https://pypi.org/project/Faker/);
  - Psycopg2: (https://pypi.org/project/psycopg2/) (para conectar-se ao servidor do PostgreSQL)
  - PyMongo: (https://pypi.org/project/pymongo/) (para conectar-se ao servidor do MongoDB)

<!-- Instruções de Uso -->
## Instruções de Uso

1. Clone este repositório em sua máquina local:

   ```bash
   git clone https://github.com/igorf1del/gerador-de-dados-bd.git
2. Navegue até o diretório do projeto:
   ```bash
   'cd nome-do-repositorio'
   
<!-- Estrutura do Repositório -->
## Estrutura do Repositório
A estrutura do repositório está organizada da seguinte forma:

- gerador_dados_postgre.py: Script para geração das tabelas e inserção de dados no PostgreSQL.
- gerador_dados_mongo.py: Script para geração das coleções e inserção de dados no MongoDB.

<!-- Contribuições -->
## Contribuições
Contribuições são bem-vindas! Se deseja melhorar ou expandir este projeto, sinta-se à vontade para enviar um pull request.
