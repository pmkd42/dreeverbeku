from flask_app import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mon1 = db.Column(db.String(10000))
    mon2 = db.Column(db.String(10000))
    mon3 = db.Column(db.String(10000))
    mon4 = db.Column(db.String(10000))
    mon5 = db.Column(db.String(10000))
    mon6 = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    teams = db.relationship('Team')
    tournaments = db.relationship('Tournament')

class MyModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stage = db.Column(db.String(50), default='Welcome')

class MyModel2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stage2 = db.Column(db.Integer)

class Tournament(db.Model):
    round = db.Column(db.Integer, primary_key=True)
    pairings = db.Column(db.JSON)

    def __init__(self, pairings):
        self.pairings = pairings
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Standings(db.Model):
    round = db.Column(db.Integer, primary_key=True)

    already_played = db.Column(db.JSON)
    scores = db.Column(db.JSON)
    def __init__(self, already_played, scores):
        self.already_played = already_played
        self.scores = scores

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
