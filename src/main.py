from flask import Flask, jsonify, request
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from repositories import feira_repository as repo

app = Flask(__name__)

#------------------------GET---------------------------------#

@app.route('/feiras', methods=['GET'])
def get_feiras():
    return jsonify(repo.get_all())


@app.route('/feiras/id/<int:id>', methods=['GET'])
def get_feiras_id(id):
    feiras = repo.search_for_id(id)
    return jsonify(feiras) if feiras else (jsonify({"erro": "no feiras found"}), 404)

@app.route('/feiras/registro/<string:registro>', methods=['GET'])
def get_feiras_registro(registro):
    feiras = repo.search_for_registro(registro)
    return jsonify(feiras) if feiras else (jsonify({"erro": "no feiras found"}), 404)


@app.route('/feiras/distrito/<string:distrito>', methods=['GET'])
def get_feiras_distrito(distrito):
    feiras = repo.search_for_distrito(distrito)
    return jsonify(feiras) if feiras else (jsonify({"erro": "no feiras found"}), 404)
        

@app.route('/feiras/regiao/<string:regiao5>', methods=['GET'])
def get_feiras_regiao(regiao5):
    feiras = repo.search_for_regiao5(regiao5)
    return jsonify(feiras) if feiras else (jsonify({"erro": "no feiras found"}), 404)


@app.route('/feiras/nome_feira/<string:nome_feira>', methods=['GET'])
def get_feiras_nome(nome_feira):
    feiras = repo.search_for_name(nome_feira)
    return jsonify(feiras) if feiras else (jsonify({"erro": "no feiras found"}), 404)


@app.route('/feiras/bairro/<string:bairro>', methods=['GET'])
def get_feiras_bairro(bairro):
    feiras = repo.search_for_bairro(bairro)
    return jsonify(feiras) if feiras else (jsonify({"erro": "no feiras found"}), 404)


#------------------------PUT---------------------------------#

@app.route('/feiras/registro/<string:registro>', methods=['PUT'])     
def edit_feira_id(registro):
    edited_feira = request.get_json()
    
    if 'REGISTRO' in edited_feira and str(edited_feira['REGISTRO']).lower() != registro.lower():
        return jsonify({"erro": "cant modify registro"}), 400
    
    success = repo.update_feira(registro, edited_feira)
    if success:
        feira_atualizada = repo.search_for_registro(registro)
        return jsonify(feira_atualizada), 200
        
    return jsonify({"erro": "feira not founded"}), 404
                
#------------------------POST---------------------------------#

@app.route('/feiras', methods=['POST'])
def include_new_feira():
    new_feira = request.get_json()

    if 'registro' not in new_feira and 'REGISTRO' not in new_feira:
            return jsonify({"erro": "REGISTRO field is required"}), 400

    id_generated = repo.register_feira(new_feira)
    saved_feira = repo.search_for_id(id_generated)
    return jsonify(saved_feira), 201

#------------------------DELETE---------------------------------#

@app.route('/feiras/registro/<string:registro>', methods=['DELETE'])
def delete_feiras(registro):
    success = repo.delete_feira(registro)
    if success:
        return jsonify({"message": f"feira {registro} deleted successfully"}), 200
            
    return jsonify({"erro": "feira not founded"}), 404


if __name__ == "__main__":
    app.run(port=5000, host='localhost', debug=True)



