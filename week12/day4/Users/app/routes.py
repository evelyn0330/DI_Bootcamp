import flask
from Users.app import app
from Users.app.forms import Form


@app.route("/")
def index():
    return flask.render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = Form()
    if form.validate_on_submit():
        firstname = form.firstname.data
        city = form.city.data

        print("Here is what I got from the form:")
        print("First Name: ", firstname)
        print("City Name: ", city)

        return flask.render_template('thanks.html')
    return flask.render_template('login.html', form=form)


