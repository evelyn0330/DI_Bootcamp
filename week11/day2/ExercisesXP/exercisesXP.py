# Exercise 1
# import flask
#
# dir(flask)
# -----------------------------------------------------------------------------
# Exercise 2
import flask

app = flask.Flask(__name__)

@app.route("/")
def homepage():
    return flask.render_template('CV.html')


if __name__ == "__main__":
  app.run(debug=True, port=8080)