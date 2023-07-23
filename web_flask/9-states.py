from flask import Flask, render_template
from models import storage, State, City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states', methods=['GET'], strict_slashes=False)
def states():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    return render_template('states.html', data=sorted_states)


@app.route('/states/<id>', methods=['GET'], strict_slashes=False)
def state_cities(id):
    state = storage.get(State, id)
    if state is not None:
        cities = state.cities if state.cities else state.cities()
        sorted_cities = sorted(cities, key=lambda city: city.name)
        return render_template('states.html', data=sorted_cities, state_name=state.name, is_state=True)
    else:
        return render_template('states.html', state_name='Not found!', is_state=False)

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
