from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


class CommentForm(FlaskForm):
    body = StringField('Comment:', validators=[InputRequired()])
