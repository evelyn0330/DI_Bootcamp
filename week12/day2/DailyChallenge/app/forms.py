import flask_wtf
import wtforms


class Form(flask_wtf.FlaskForm):
    firstname = wtforms.StringField('First Name', [wtforms.validators.DataRequired()])
    lastname = wtforms.StringField('Last Name', [wtforms.validators.DataRequired()])
    age = wtforms.IntegerField('Age', [wtforms.validators.DataRequired()])
    experience = wtforms.StringField('Experience', [wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("Submit")



