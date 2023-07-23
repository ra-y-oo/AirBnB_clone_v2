from flask import Flask, render_template
from models import storage, State, City

app = Flask(__name__)

@app.route('/hbnb-filters', strict_slashes=False)
def hbnb_filters():
    # Fetch and sort State, City, and Amenity objects by name
    states = sorted(list(storage.all('State').values()), key=lambda x: x.name)
    cities = sorted(list(storage.all('City').values()), key=lambda x: x.name)
    amenities = sorted(list(storage.all('Amenity').values()), key=lambda x: x.name)

    return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities)



@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
