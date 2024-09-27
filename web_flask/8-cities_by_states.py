#!/usr/bin/python3
"""
A simple Flask web application that displays a list of states and their cities.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """Method to remove the current SQLAlchemy session"""
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Route that displays a list of all State objects and their linked City objects"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=sorted_states)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
