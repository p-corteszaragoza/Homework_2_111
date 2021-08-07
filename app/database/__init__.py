from app.routes import db
import json 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    hobbies = db.Column(db.String, nullable=True)
    active = db.Column(db.Boolean, nullable=False, default=1)

    def __repr__(self):
        return "<User %r>" % self.first_name

    def to_json(self):
        return {
            "id": int(self.id),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "hobbies": self.hobbies,
            "active": self.active
        }
