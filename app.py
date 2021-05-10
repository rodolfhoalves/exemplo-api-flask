from flask import Flask
from flask import jsonify
from flask.globals import request
import json

app = Flask(__name__)

lista_de_alunos = [
    {
        'id': 0,
        'nome': 'Tiago Fernandes',
        'idade': 26
    },

    {
        'id': 1,
        'nome': 'André Souza',
        'idade': 29
    }
]


@app.route("/")
def main():
    return jsonify({'status': 'sucesso', 'mensagem': 'api de cadastro de alunos'})


@app.route("/alunos", methods = ['GET', 'POST'])
def alunos():
    
    # Retorna todos os alunos
    if request.method == 'GET':
        return jsonify(lista_de_alunos)

    # Adiciona um novo aluno
    if request.method == 'POST':
        response_body = json.loads(request.data)
        response_body['id'] = len(lista_de_alunos)
        lista_de_alunos.append(response_body)

        return jsonify({'status': 'sucesso', 'mensagem': 'Aluno cadastrado'}) 


@app.route("/alunos/<int:id>", methods = ['GET', 'DELETE', 'PUT'])
def alunos_por_id(id):

    # Retorna os dados do aluno pelo seu ID
    if request.method == 'GET':
        try:
            return jsonify(lista_de_alunos[id])
        except IndexError:
            return jsonify({'status': 'erro', 'mensagem': 'Não existe um aluno cadastro com esse ID: {}' .format(id)})
        except Exception:
            return jsonify({'status': 'erro', 'mensagem': 'Erro desconhecido'})

    # Remove um aluno
    if request.method == 'DELETE':

        try:
            lista_de_alunos.pop(id)
            return jsonify({'status': 'sucesso', 'mensagem': 'Aluno com o ID: ({}) removido do registro de alunos' .format(id)})
        except IndexError:
            return jsonify({'status': 'erro', 'mensagem': 'Não existe o aluno com o id {}' .format(id)})
        except Exception:
            return jsonify({'status': 'erro', 'mensagem': 'Erro desconhecido'})

    # Atualiza os dados de um aluno
    if request.method == 'PUT':

        try:
            response_body = json.loads(request.data)
            lista_de_alunos[id]['idade'] = response_body['idade']
            lista_de_alunos[id]['nome'] = response_body['nome']

            return jsonify({'status': 'sucesso', 'mensagem': 'Dados do aluno atualizado'})
        except IndexError:
            return jsonify({'status': 'erro', 'mensagem': 'Não existe aluno com o ID {}' .format(id)})
        except Exception:
            return jsonify({'status': 'erro', 'mensagem': 'Erro desocnhecido'})



if __name__ == "__main__":
    app.run(debug = True)