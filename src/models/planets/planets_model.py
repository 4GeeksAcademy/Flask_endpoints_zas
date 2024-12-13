from .. import db

class Planets (db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Boolean(), unique=False, nullable=False)
    population = db.Column(db.String(80), unique=False, nullable=False)
    favorite_planets = db.relationship("favorite_planet", backref= "Planets", lazy=True)

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.uid,
            "name": self.name
            
        }