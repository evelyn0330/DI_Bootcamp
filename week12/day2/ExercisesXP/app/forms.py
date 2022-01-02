import flask_wtf
import wtforms


class Form(flask_wtf.FlaskForm):
    cityname = wtforms.StringField("City's name", [wtforms.validators.DataRequired(), wtforms.validators.Length(max=15)])
    citycountry = wtforms.StringField("City's Country", [wtforms.validators.DataRequired()])
    numofinhabitants = wtforms.IntegerField("Number of Inhabitants", [wtforms.validators.DataRequired()])
    cityarea = wtforms.IntegerField("City's area in Km")
    submit = wtforms.SubmitField("Submit")

