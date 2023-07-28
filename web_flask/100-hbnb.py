#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import storage, State, Amenity

app = Flask(__name__)

@app.route('/hbnb', methods=['GET'])
def hbnb():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    amenities = storage.all(Amenity).values()
    sorted_amenities = sorted(amenities, key=lambda amenity: amenity.name)

    return render_template('100-hbnb.html', states=sorted_states, amenities=sorted_amenities)

@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    