from flask_app import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mon1 = db.Column(db.String(10000))
    mon1_shadow = db.Column(db.Integer)
    mon1_safe= db.Column(db.Integer, default=0)
    mon2 = db.Column(db.String(10000))
    mon2_shadow = db.Column(db.Integer)
    mon2_safe= db.Column(db.Integer, default=0)
    mon3 = db.Column(db.String(10000))
    mon3_shadow = db.Column(db.Integer)
    mon3_safe= db.Column(db.Integer, default=0)
    mon4 = db.Column(db.String(10000))
    mon4_shadow = db.Column(db.Integer)
    mon4_safe= db.Column(db.Integer, default=0)
    mon5 = db.Column(db.String(10000))
    mon5_shadow = db.Column(db.Integer)
    mon5_safe= db.Column(db.Integer, default=0)
    mon6 = db.Column(db.String(10000))
    mon6_shadow = db.Column(db.Integer)
    mon6_safe= db.Column(db.Integer, default=0)
    mon7 = db.Column(db.String(10000))
    mon7_shadow = db.Column(db.Integer)
    mon7_safe= db.Column(db.Integer, default=0)
    mon8 = db.Column(db.String(10000))
    mon8_shadow = db.Column(db.Integer)
    mon8_safe= db.Column(db.Integer, default=0)
    round_bans = db.Column(db.String, nullable=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    teams = db.relationship('Team')
    tournaments = db.relationship('Tournament')
    submitted = db.Column(db.Integer, default=0)
    banned = db.Column(db.Integer, default=0)
    wins = db.Column(db.String, default='[]')
    round_wins = db.Column(db.Integer, default=0)
    total_wins = db.Column(db.Integer, default=0)
    already_matched = db.Column(db.String, default='[]')
    toughness = db.Column(db.Integer, default=0)

class MyModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stage = db.Column(db.String(50), default='Welcome')

class MyModel2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stage2 = db.Column(db.Integer)

class Max_rounds_t(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    max_rounds = db.Column(db.Integer, default=0)
    current_round = db.Column(db.Integer, default=0)

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

