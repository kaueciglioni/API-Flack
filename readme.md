# API de Gerenciamento de Livros

Esta é uma API simples construída com Flask para gerenciar uma coleção de livros. Ela permite a visualização, adição, edição e remoção de livros.

## Rotas Disponíveis

- `GET /livros`: Retorna todos os livros disponíveis na coleção.
- `GET /livros/<int:id>`: Retorna os detalhes de um livro específico com base no ID fornecido.
- `PUT /livros/<int:id>`: Atualiza os detalhes de um livro existente com base no ID fornecido.
- `POST /livros`: Adiciona um novo livro à coleção.
- `DELETE /livros/<int:id>`: Remove um livro da coleção com base no ID fornecido.

## Estrutura dos Dados

Cada livro é representado por um objeto JSON com os seguintes campos:

- `id`: O identificador único do livro.
- `título`: O título do livro.
- `autor`: O autor do livro.

## Como Executar

1. Certifique-se de ter o Python e o Flask instalados em seu ambiente.
2. Clone este repositório ou baixe o arquivo `app.py`.
3. Abra um terminal na pasta onde o arquivo `app.py` está localizado.
4. Execute o comando `python app.py` para iniciar o servidor Flask.
5. A API estará disponível em `http://localhost:5000/`.

## Exemplos de Uso

- Para visualizar todos os livros: `GET http://localhost:5000/livros`.
- Para visualizar os detalhes de um livro específico com ID 1: `GET http://localhost:5000/livros/1`.
- Para adicionar um novo livro: `POST http://localhost:5000/livros` com corpo JSON contendo os detalhes do novo livro.
- Para atualizar os detalhes de um livro existente com ID 1: `PUT http://localhost:5000/livros/1` com corpo JSON contendo os novos detalhes do livro.
- Para remover um livro com ID 1: `DELETE http://localhost:5000/livros/1`.

Certifique-se de substituir `localhost` e `5000` pelos valores apropriados se você estiver executando a API em um ambiente diferente.
