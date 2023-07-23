from flask import Flask, jsonify, request, render_template
from models.engine.db_storage import DBStorage
from models import State


app = Flask(__name__)
#initialize the storage instance
storage = DBStorage()

storage.reload()

@app.route('/states_list', methods=['GET'], strict_slashes=False)
def states_list():
    # Fetch all State objects from the storage and sort them by name
    states = sorted(storage.all(State).values(), key=lambda state: state.name)

    # Render the HTML template with the list of states
    return render_template('states_list.html', states=states)


@app.teardown_appcontext
def teardown_appcontext(exception):
    #Close current SQLAlchemmy session after each request
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
