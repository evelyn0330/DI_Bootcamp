import flask
from DailyChallenge.app import app
from DailyChallenge.app.forms import Form


@app.route('/', methods=['GET'])
def index():
    return flask.render_template('index.html')


@app.route('/cv-form', methods=['GET', 'POST'])
def cv_form():
    form = Form()
    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        age = form.age.data
        experience = form.experience.data

        print("Here is what I got from the form:")
        print("First name: ", firstname)
        print("Last name: ", lastname)
        print("Age: ", age)
        print("Experience: ", experience)

        return flask.render_template('cv.html', firstname=firstname, lastname=lastname, age=age, experience=experience)
    return flask.render_template('cv-form.html', form=form)
