from flask import Flask, jsonify, request

app = Flask(__name__)

feiras = [
    {
        'id': 1,
        'DISTRITO': 'VILA FORMOSA',
        'REGIAO5': 'Leste',
        'NOME_FEIRA': 'VILA FORMOSA',
        'REGISTRO': '4041-0',
        'BAIRRO': 'VL FORMOSA'
    },
    {
        'id': 2,
        'DISTRITO': 'VILA PRUDENTE',
        'REGIAO5': 'Leste',
        'NOME_FEIRA': 'PRACA SANTA HELENA',
        'REGISTRO': '4045-2',
        'BAIRRO': 'VL ZELINA'
    }
]

#------------------------GET---------------------------------#

@app.route('/feiras', methods=['GET'])
def get_feiras():
    return jsonify(feiras)

@app.route('/feiras/id/<int:id>', methods=['GET'])
def get_feiras_id(id):
    for feira in feiras:
        if feira.get('id') == id:
            return jsonify(feira)
        
@app.route('/feiras/distrito/<string:distrito>', methods=['GET'])
def get_feiras_distrito(distrito):
    feiras_encontradas = []
    
    for feira in feiras:
        if feira.get('DISTRITO').lower() == distrito.lower():
            feiras_encontradas.append(feira)
            
    if feiras_encontradas:
        return jsonify(feiras_encontradas)
        
@app.route('/feiras/regiao/<string:regiao5>', methods=['GET'])
def get_feiras_regiao(regiao5):
    feiras_encontradas = []
    
    for feira in feiras:
        if feira.get('REGIAO5').lower() == regiao5.lower():
            feiras_encontradas.append(feira)
            
    if feiras_encontradas:
        return jsonify(feiras_encontradas)
    
@app.route('/feiras/nome_feira/<string:nome_feira>', methods=['GET'])
def get_feiras_nome(nome_feira):
    feiras_encontradas = []
    
    for feira in feiras:
        if feira.get('NOME_FEIRA').lower() == nome_feira.lower():
            feiras_encontradas.append(feira)
            
    if feiras_encontradas:
        return jsonify(feiras_encontradas)

@app.route('/feiras/bairro/<string:bairro>', methods=['GET'])
def get_feiras_bairro(bairro):
    feiras_encontradas = []
    
    for feira in feiras:
        if feira.get('BAIRRO').lower() == bairro.lower():
            feiras_encontradas.append(feira)
            
    if feiras_encontradas:
        return jsonify(feiras_encontradas)
    
#------------------------PUT---------------------------------#

@app.route('/feiras/registro/<string:registro>', methods=['PUT'])     
def edit_feira_id(registro):
    edited_feira = request.get_json()
    
    if 'REGISTRO' in edited_feira and str(edited_feira['REGISTRO']).lower() != registro.lower():
        return jsonify({"erro": "cant modify registro"}), 400
    
    for indice, feira in enumerate(feiras):
        if feira.get('REGISTRO','').lower() == registro.lower():
            feiras[indice].update(edited_feira)
            return jsonify(feiras[indice])
        
    return jsonify({"erro": "feira not founded"}), 404
                
#------------------------POST---------------------------------#

@app.route('/feiras', methods=['POST'])
def include_new_feira():
    new_feira = request.get_json()
    feiras.append(new_feira)

    return jsonify(feiras)

#------------------------DELETE---------------------------------#

@app.route('/feiras/registro/<string:registro>', methods=['DELETE'])
def delete_feiras(registro):
    global feiras 
    feiras = [
        feira for feira in feiras 
        if feira.get('REGISTRO', '').lower() != registro.lower()
    ]

    return jsonify(feiras)

app.run(port=5000, host='localhost', debug=True)

