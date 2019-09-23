from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def start():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app


app = start()
db = SQLAlchemy(app)


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    games_played = db.Column(db.Integer, nullable=True)
    games_won = db.Column(db.Integer, nullable=True)
    games_lost = db.Column(db.Integer, nullable=True)
    avg_goals_per_game = db.Column(db.Float, nullable=True)
    win_rate = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.name


class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    match_date = db.Column(db.DateTime, nullable=False)
    player1 = db.Column(db.String(32), nullable=False)
    player2 = db.Column(db.String(32), nullable=False)
    player3 = db.Column(db.String(32), nullable=False)
    player4 = db.Column(db.String(32), nullable=False)
    final_score = db.Column(db.String(32), nullable=False)


class MatchEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
    match = db.relationship('Match', backref=db.backref('match_events', lazy=True))
    event_type = db.Column(db.String(32), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    player = db.relationship('Player', backref=db.backref('events', lazy=True))
    pos = db.Column(db.String(32))
