import flask
from DailyChallenge.config import Config

app = flask.Flask(__name__)
app.config.from_object(Config)


from DailyChallenge.app import routes


