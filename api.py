from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K. Rowling'
    },
    {
        'id': 2,
        'título': 'Diário de um Banana',
        'autor': 'Jeff Kinney'
    },
    {
        'id': 3,
        'título': 'Percy Jackson e o Ladrão de Raios',
        'autor': 'Rick Riordan'
    },
    {
        'id': 4,
        'título': 'Arsène Lupin, O Ladrão de Casaca',
        'autor': 'Maurice Leblanc'
    },
    {
        'id': 5,
        'título': 'A Culpa é das Estrelas',
        'autor': 'John Green'
    },
    {
        'id': 6,
        'título': 'As Crônicas de Nárnia: O Leão, a Feiticeira e o Guarda-Roupa',
        'autor': 'C.S. Lewis'
    }
]

@app.route('/livros', methods=['GET'])
def pegar_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
def pegar_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

@app.route('/livros', methods=['POST'])
def adicionar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['DELETE'])
def remover_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)