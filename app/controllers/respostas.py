from flask import jsonify

def resposta_cod_add(cod, msg=str):
    response = {}
    response['codico'] = cod
    response['mensagem'] = msg

    jsonify(response)
    return response