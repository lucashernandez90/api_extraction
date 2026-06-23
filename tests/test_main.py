import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_all_feiras_returns_200(client):

    response = client.get('/feiras')
    assert response.status_code == 200
    assert response.content_type == 'application/json'

def test_get_feiras_by_distrito_success(client):

    response = client.get('/feiras/distrito/vila formosa')
    assert response.status_code == 200
    assert response.content_type == 'application/json'

def test_get_feiras_by_distrito_invalid_returns_404(client):

    response = client.get('/feiras/distrito/distrito-fantasma')
    assert response.status_code == 404
    assert b"no feiras found" in response.data

def test_post_without_registro_returns_400(client):

    incompleted_data = {
        "NOME_FEIRA": "FEIRA SEM REGISTRO"
    }
    response = client.post('/feiras', json=incompleted_data)
    assert response.status_code == 400
    assert b"REGISTRO field is required" in response.data

def test_get_feira_by_invalid_id_returns_404(client):

    response = client.get('/feiras/id/999999')
    assert response.status_code == 404
    assert b"no feiras found" in response.data

def test_put_cannot_modify_registro(client):

    invalid_data = {
        "REGISTRO": "CODIGO-DIFERENTE-DO-DA-URL",
        "NOME_FEIRA": "NOME ALTERADO"
    }
    response = client.put('/feiras/registro/4041-0', json=invalid_data)
    assert response.status_code == 400
    assert b"cant modify registro" in response.data

def test_crud_flow_post_put_delete(client):

    nova_feira = {
        "REGISTRO": "9999-TESTE-PYTEST",
        "NOME_FEIRA": "FEIRA TESTE AUTOMACAO",
        "DISTRITO": "TESTE",
        "BAIRRO": "TESTE",
        "REGIAO5": "Leste"
    }
    response_post = client.post('/feiras', json=nova_feira)
    assert response_post.status_code == 201
    
    dados_atualizados = {
        "NOME_FEIRA": "NOME ATUALIZADO PELO PYTEST",
        "BAIRRO": "BAIRRO NOVO"
    }
    response_put = client.put('/feiras/registro/9999-TESTE-PYTEST', json=dados_atualizados)
    assert response_put.status_code == 200
    assert b"NOME ATUALIZADO PELO PYTEST" in response_put.data

    response_delete = client.get('/feiras/id/')
    response_delete = client.delete('/feiras/registro/9999-TESTE-PYTEST')
    assert response_delete.status_code == 200
    assert b"deleted successfully" in response_delete.data