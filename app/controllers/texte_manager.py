def limitar_texto(text: str, n_max_letras: 80):
    if len(text) > n_max_letras:
        text = text[:n_max_letras] +'...'
    return text


def verificar_arg_secundarios_dict(body: dict, arg: str, padrao):
    if arg not in body:
        body[arg] = padrao
    elif body[arg] == '': 
        body[arg] = padrao
    return body
