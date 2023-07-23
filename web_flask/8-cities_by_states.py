from flask import Flask, render_template
from models import storage, State, City

app = Flask(__name__)

@app.route('/cities_by_states', methods=['GET'], strict_slashes=False)
def cities_by_states():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    return render_template('cities_by_states.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
