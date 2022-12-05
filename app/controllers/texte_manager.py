def limitar_texto(text: str, n_max_letras: 80):
    if len(text) > n_max_letras:
        text = text[:n_max_letras] +'...'
    return text
