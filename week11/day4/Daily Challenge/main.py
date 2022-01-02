import flask

app = flask.Flask(__name__)


@app.route('/')
def main():
    return flask.render_template('home.html', color= 'white')


@app.route('/blue')
def blue():
    return flask.render_template('home.html', color= 'blue')


@app.route('/red')
def red():
    return flask.render_template('home.html', color= 'red')


@app.route('/green')
def green():
    return flask.render_template('home.html', color= 'green')


@app.route('/yellow')
def yellow():
    return flask.render_template('home.html', color= 'yellow')


if __name__ == '__main__':
    app.run(debug=True, port=4545)