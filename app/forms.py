from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    photo = FileField('Choose Photo to be uploaded', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])])