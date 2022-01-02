import flask
import datetime


app = flask.Flask(__name__)

current_time = datetime.datetime.now()
greeting = ''

if 13 > current_time.hour >= 8:
    greeting = 'Good Morning!'
elif 17 > current_time.hour >= 13:
    greeting = 'Good Afternoon!'
elif 21 > current_time.hour >= 17:
    greeting = 'Good Evening!'
elif 8 > current_time.hour >= 21:
    greeting = 'Good Night!'


@app.route('/')
def home():
    return flask.render_template('greetings.html', message=greeting)


if __name__ == "__main__":
    app.run(debug=True,port=4545)





