from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/apiestilorei'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando o SQLAlchemy
db = SQLAlchemy(app)


# Modelo de Cliente
# Classe gera uma tabela (Code frist)
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(15), nullable=False)

    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


# Criar o banco de dados (executar uma vez)
# Criar as tabelas diretamente ao iniciar o aplicativo
with app.app_context():
    db.create_all()

#rota para integrar python com javascript via json
@app.route('/api/cliente', methods=['GET'])
def pegar_cliente():
    return jsonify({'cliente':'Rafael','telefone':'(61)996371619'})

# Criar uma rota para retornar dados do banco de dados
@app.route('/getclientes', methods=['GET'])
def busca_clientes():
    clientes = Cliente.query.all()
    # Retorna os clientes em formato JSON
    return jsonify([{'nome': cliente.nome,
                    'telefone': cliente.telefone}
                    for cliente in clientes])

if __name__ == '__main__':
    app.run(debug=True)