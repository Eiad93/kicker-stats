from set_db import app
from flask_marshmallow import Marshmallow
from set_db import Match, MatchEvent, Player


# init marshmallow
marshmallow = Marshmallow(app)


class PlayerSchema(marshmallow.ModelSchema):
    class Meta:
        model = Player


class MatchSchema(marshmallow.ModelSchema):
    class Meta:
        model = Match


class MatchEventSchema(marshmallow.ModelSchema):
    class Meta:
        model = MatchEvent


