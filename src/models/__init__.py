from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

from .user.user_model import User
from .people.people_model import People
from .planets.planets_model import Planets
from .favorite.favorite_planet_model import Favorite