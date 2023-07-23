from flask import Flask, jsonify, request
from models import storage

app = Flask(__name__)

storage.reload()

@app.route('/states_list', strict_slashes=False, methods=['GET'])
def get_items():
    # Fetch data from the storage engine using storage.all(...)
    all_items = storage.all()
    items = [item.to_dict() for item in all_items.values()]
    return jsonify(items)

@app.teardown_appcontext
def teardown_appcontext(exception):
    #Close current SQLAlchemmy session after each request
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
