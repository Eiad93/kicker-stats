from flask import request
from set_db import db
from set_db import Player, Match, MatchEvent
from set_db import app
from objects_schema import PlayerSchema, MatchEventSchema, MatchSchema

db.create_all()
player_schema = PlayerSchema(many=True)
match_schema = MatchSchema()
match_event_schema = MatchEventSchema()


@app.route('/')
def home():

    return 'Here comes the welcome and the start a new match button'


@app.route('/get_players', methods=['GET'])
def get_players():
    players = Player.query.all()
    result = player_schema.dumps(players)
    return result


@app.route('/new_player', methods=['POST'])
def new_player():
    data = request.json
    player = player_schema.load(data)
    db.session.add(player)
    db.session.commit()
    return 'ok'


@app.route('/add_match', methods=['POST'])
def add_match():
    data = request.json
    match = match_schema.load(data)
    db.session.add(match)
    db.session.commit()
    return 'ok'

# ToDo update match methods to add the final score
# ToDo remove the validation for adding the match


@app.route('/add_event', methods=['POST'])
def add_event():
    data = request.json
    match_event = match_event_schema.load(data)
    db.session.add(match_event)
    db.session.commit()
    return 'ok'
