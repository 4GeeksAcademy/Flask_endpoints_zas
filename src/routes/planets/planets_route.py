from flask import Blueprint

planets_bp = Blueprint('planets', __name__)


@planets_bp.route("/", methods = ["GET"])
def get_planets():
        return "retornando todos los planetas", 200

@planets_bp.route("/<int:planet_id>", methods = ["GET"]) 
def get_planet(planet_id):
        return "retornando planeta", 200