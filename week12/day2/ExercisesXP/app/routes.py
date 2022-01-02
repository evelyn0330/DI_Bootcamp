import flask
from ExercisesXP.app import app
from ExercisesXP.app.forms import Form


@app.route('/', methods=['GET'])
def index():
    return flask.render_template('index.html')


@app.route('/add-city', methods=['GET', 'POST'])
def add_city():
    form = Form()
    if form.validate_on_submit():
        cityname = form.cityname.data
        citycountry = form.citycountry.data
        numofinhabitants = form.numofinhabitants.data
        cityarea = form.cityarea.data

        print("Here's what I got from the form:")
        print("City's name: ", cityname)
        print("City's country: ", citycountry)
        print("Number of inhabitants: ", numofinhabitants)
        print("City's area: ", cityarea)

        return flask.redirect('/')
    return flask.render_template('add-city.html', form=form)

