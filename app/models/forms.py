from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class Delet_form(FlaskForm):
    senha = PasswordField('Senha', validators=[DataRequired()], render_kw={"placeholder": "Password"})
