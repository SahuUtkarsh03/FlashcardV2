from flask_restful import Resource
from datetime import datetime

from application.data.database import db
from application.data.model import User,Deck
from application.utils.validation import ValidationError
from application.utils.parser import *
from application.controller.controllers import token_required
import json

# RESTful API for DECK
class DeckApi(Resource):
    
    def get(self,deckid):
        deck=Deck.query.filter_by(deck_id=deckid).first()
        if deck is None:
            raise ValidationError(404,"DVE1006","Deck does not exist")
        else:
            return {"deck_id":deck.deck_id,
                    "deck_name":deck.deck_name,
                    "owner_userid":deck.owner_userid,
                    "last_reviewed": deck.last_reviewed,
                    "deck_score":deck.deck_score},200
    
    def put(self,deckid):
        deck=Deck.query.filter_by(deck_id=deckid).first()
        if deck is None:
            raise ValidationError(404,"DVE1006","Deck does not exist")
        args=update_deck_parser.parse_args()
        deckname=args.get("deck_name",None)
        if deckname is None:
            raise ValidationError(404,"DVE1003","Deckname is required")
        else:
            deck.deck_name=deckname
            db.session.commit()
            return {"deck_id":deck.deck_id,
                    "updateddeck_name":deck.deck_name,
                    "owner_userid":deck.owner_userid,
                    "last_reviewed": deck.last_reviewed,
                    "deck_score":deck.deck_score},201

    @token_required
    def delete(current_user,self,deckid):
        deck=Deck.query.filter_by(deck_id=deckid).first()
        if deck is None:
            raise ValidationError(404,"DVE1006","Deck does not exist")
        elif len(deck.cards)>0:
            raise ValidationError(404,"DVE1007","Deck has cards , delete them first")
        else:
            db.session.delete(deck)
            db.session.commit()

            return json.dumps({"deck_id":deck.deck_id,
                    "deck_name":deck.deck_name,
                    "owner_userid":deck.owner_userid,
                    "last_reviewed": deck.last_reviewed,
                    "deck_score":deck.deck_score}),200

    @token_required
    def post(current_user,self):
        args=deck_parser.parse_args()
        deckname=args.get("deck_name",None)
        ownerid= int(current_user.user_id)
        ownerDoesNotExists=User.query.filter_by(user_id=ownerid).first() is None
        deck=None if ownerDoesNotExists else (
            Deck.query.filter_by(deck_name = deckname, 
            owner_userid = ownerid).first()
        )
        if deck is not None:
            raise ValidationError(400,"DVE1001","Deck id is duplicate")
        elif deckname is None:
            raise ValidationError(400,"DVE1003","Deckname is required")
        elif ownerid is None:
            raise ValidationError(400,"DVE1004","Ownerid is needed")
        elif ownerDoesNotExists:
            raise ValidationError(400,"DVE1005","Ownerid is not Valid")
        else:
            newDeck=Deck(deck_name=deckname,
                        owner_userid=ownerid,
                        last_reviewed= datetime.utcnow().strftime('%d-%m-%Y %H:%M'),
                        deck_score=0
                    )
            db.session.add(newDeck)
            db.session.commit()
            
            return json.dumps({"deck_id":newDeck.deck_id,
                    "deck_name":newDeck.deck_name,
                    "owner_userid":newDeck.owner_userid,
                    "last_reviewed": newDeck.last_reviewed,
                    "deck_score":newDeck.deck_score}),201
