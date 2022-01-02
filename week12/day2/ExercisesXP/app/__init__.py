import flask
from ExercisesXP.config import Config

app = flask.Flask(__name__)
app.config.from_object(Config)


from ExercisesXP.app import routes










