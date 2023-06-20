from . import db

class GroupInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    CWID = db.Column(db.Integer)
    size = db.Column(db.Integer)
    email = db.Column(db.String(100))
    group_assigned_room = db.Column(db.Integer)
    message = db.Column(db.String(1000))

class RoomInfo(db.Model):
    occupancy = db.Column(db.boolean, default=False)
    id = db.Column(db.Integer, primary_key=True)