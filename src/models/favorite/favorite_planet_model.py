from .. import db

class Favorite_planet (db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Boolean(), unique=False, nullable=False)
    planet_id = db.Column(db.Integer, ForeignKey = ("planet.id"))

    def __repr__(self):
        return '<Favorite_planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.uid,
            "name": self.name,
            "description": self.description

            
        }