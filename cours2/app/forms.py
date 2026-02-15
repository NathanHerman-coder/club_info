from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class ProductForm(FlaskForm):
    name = StringField("Nom", validators=[DataRequired(), Length(max=128)])
    price = DecimalField("Prix", places=2, validators=[DataRequired(), NumberRange(min=0)])
    stock = IntegerField("Stock", default=0, validators=[NumberRange(min=0)])
    description = TextAreaField("Description")
    submit = SubmitField("Enregistrer")


class CheckoutForm(FlaskForm):
    fullname = StringField("Nom complet", validators=[DataRequired(), Length(max=128)])
    email = StringField("Email", validators=[DataRequired(), Length(max=128)])
    address = TextAreaField("Adresse", validators=[DataRequired(), Length(max=512)])
    submit = SubmitField("Commander")
