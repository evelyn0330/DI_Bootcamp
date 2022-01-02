import flask_wtf
import wtforms


class Form(flask_wtf.FlaskForm):
    firstname = wtforms.StringField("First Name", [wtforms.validators.DataRequired()])
    city = wtforms.StringField("City name", [wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("Submit")




