from flask import Blueprint

favorite_bp = Blueprint('favorite', __name__)


@favorite_bp.route("/planets", methods = ["POST"])
def add_favorite_planet(planet_id):
        return "añadido planeta favorito", 200

@favorite_bp.route("/people", methods = ["POST"])
def add_favorite_character(people_id):
        return "añadido personaje favorito", 200

@favorite_bp.route("/planets", methods = ["DELETE"])
def delete_favorite_planet(planet_id):
        return "añadido planeta favorito", 200

@favorite_bp.route("/people", methods = ["DELETE"])
def delete_favorite_character(people_id):
        return "añadido personaje favorito", 200
