from app import db

class Save_keys(db.Model):
    __tablename__ = 'save_keys'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pcname = db.Column(db.String)
    criador = db.Column(db.String)
    texto = db.Column(db.Text)
    data = db.Column(db.Date)
    

    def __init__(self, pcname, texto, data, criador='Sem registro'):
        self.pcname = pcname
        self.texto = texto
        self.data = data
        self.criador = criador

    def __repr__(self):
        return '<Save Keys %r>' % self.pcname
