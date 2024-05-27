#!/usr/bin/python3
""" Index """
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects"""

    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]

    number_objs = {}
    for i in range(len(classes)):
        number_objs[names[i]] = storage.count(classes[i])

    return jsonify(number_objs)