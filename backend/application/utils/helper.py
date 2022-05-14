from application.data.model import User,Card,Deck
from main import cache


def getUser(username):
    user=User.query.filter_by(user_name=username).first()
    return user

@cache.memoize(timeout=50)
def getDeck(deck_name, owner_userid):
    deck=Deck.query.filter_by(deck_name = deck_name , owner_userid = int(owner_userid)).first()
    return deck


def getCard(cardid):
    card = Card.query.filter_by(id=int(cardid)).first()
    return card