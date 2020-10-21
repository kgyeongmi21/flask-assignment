from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField


class WriteForm(FlaskForm):
    title = StringField()
    author = StringField()
    content = TextAreaField()
    submit = SubmitField('게시')
