from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired

class Contact(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    pref = StringField('Cats or dogs?', validators=[DataRequired()])
    message = StringField('What would you like to share with the world?', validators=[DataRequired()])
    submit = SubmitField('Submit')
