from flask_wtf import FlaskForm
from wtforms import HiddenField
from wtforms.validators import DataRequired

class BookSelectionForm(FlaskForm):
    book_isbn = HiddenField('ISBN',validators=[DataRequired()],id='book_isbn')