from application.data.database import db
from flask_login import UserMixin
from datetime import datetime
from flask import jsonify

#user model
class User(db.Model, UserMixin):

    __tablename__ = "user"
    user_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    firstname = db.Column(db.String,nullable=False)
    lastname =  db.Column(db.String,nullable=True)
    user_name = db.Column(db.String,nullable=False,unique=True)
    hashed_password = db.Column(db.String, nullable=False)
    email=db.Column(db.String, nullable=False,unique=True)
    # Creating One-to-Many Relationship
    decks=db.relationship("Deck",backref='owner')

    def get_id(self):
        return (self.user_id)
    
    def __repr__(self):
        return '<Name %r>' % self.user_name

#deck model
class Deck(db.Model):

    __tablename__ = "deck"
    deck_id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    deck_name = db.Column(db.String,nullable=False)
    owner_userid=db.Column(db.Integer,db.ForeignKey("user.user_id"))
    last_reviewed = db.Column(db.Integer)
    deck_score = db.Column(db.Integer, default=0 )
    # creating One-to-Many Relationship
    cards=db.relationship("Card",backref='Deck')

    def get_id(self):
        return (self.deck_id)

    def decktoJson(self):
            return {"deck_id":self.deck_id,
                        "deck_name":self.deck_name,
                        "owner_userid":self.owner_userid,
                        "last_reviewed": self.last_reviewed,
                        "deck_score":self.deck_score}

    def exportDeck(self):
        print(self.cards)

    def __repr__(self):
        return '<Name %r>' % self.deck_name

#card model
class Card(db.Model):
    
    __tablename__ = "card"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deck_id = db.Column(db.Integer,db.ForeignKey("deck.deck_id"))
    question = db.Column(db.String,nullable=False)
    answer = db.Column(db.String,nullable=False)
    card_score = db.Column(db.Integer, default=0)
    last_reviewed = db.Column(db.Integer)

    def toJson(self):
        return {
            "id":self.id,
            "deck_id" :  self.deck_id,
            "question" :  self.question,
            "answer" :  self.answer,
            "card_score" :  self.card_score,
            "last_reviewed" : self.last_reviewed
        }