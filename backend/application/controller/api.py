from flask_restful import Resource
from werkzeug.security import generate_password_hash
from datetime import datetime

from application.data.database import db
from application.data.model import User,Deck,Card
from application.utils.validation import ValidationError
from application.utils.parser import *


# RESTful API for USER
class UserApi(Resource):

    def get(self,username):
        from application.utils.helper import getUser
        user=getUser(username)
        
        if user:
            return {"userid": user.user_id,
                    "username": user.user_name,
                    "firstname":user.firstname,
                    "lastname":user.lastname,
                    "email": user.email },200
        else:
            raise ValidationError(404,"UVE1006","Such user does not exist")

    def put(self,username):
        user=User.query.filter_by(user_name=username).first()
        if user is None:
            raise ValidationError(404,"UVE1006","Such user does not exist")
        else:
            args=update_user_parser.parse_args()
            firstname,lastname,password=args.get("firstname",None),args.get("lastname",None),args.get("password",None)
            if (firstname is None) or (firstname=='') :
                raise ValidationError(404,"UVE1001","Firstname is  required")
            elif password is None or (password==''):
                raise ValidationError(404,"UVE1003","Password is required")
            elif len(password)<8 or len(password)>20:
                raise ValidationError(404,"UVE1005","Password must be between 8 to 20 characters")
            else:            
                password=generate_password_hash(password)
                user.firstname,user.lastname,user.hashed_password=firstname,lastname,password
                db.session.commit()
                return {"new_fname":firstname,
                        "new_lname":lastname},200

    def delete(self,username):
        user=User.query.filter_by(user_name=username).first()
        if user is None:
            raise ValidationError(404,"UVE1006","Such user does not exist")
        elif len(user.decks)>0:
            raise ValidationError(404,"UVE1007","User has decks,Delete them first!")
        else:
            db.session.delete(user)
            db.session.commit()
            return {"deleteduser_id":user.user_id,
                    "deleteduser_fname":user.firstname,
                    "deleteduser_lname":user.lastname,
                    "deleteduser_username":user.user_name},200

    def post(self):
        args=user_parser.parse_args()
        firstname,lastname,username,password,email=args.get("firstname",None),args.get("lastname",None),args.get("username",None),args.get("password",None),args.get("email",None)
        if firstname is None or (firstname=='') :
            raise ValidationError(404,"UVE1001","Firstname is  required")
        elif username is None or (username=='') :
            raise ValidationError(404,"UVE1002","Username is  required")
        elif password is None or (password==''): 
            raise ValidationError(404,"UVE1003","Password is required")
        elif email is None or ("@" not in email) :
            raise ValidationError(404,"UVE1008","Email is required")
        elif User.query.filter_by(user_name=username).first()  is not None:
            raise ValidationError(404,"UVE1004","Username already exists")
        elif User.query.filter_by(email=email).first() is not None:
            raise ValidationError(404,"UVE1009","Email already exists")
        elif len(password)<8 or len(password)>20:
            raise ValidationError(404,"UVE1005","Password must be between 8 to 20 characters")
        else:
            newuser=User(user_name = username, hashed_password = generate_password_hash(password),firstname = firstname, lastname = lastname,email=email )
            db.session.add(newuser)
            db.session.commit()
            return {"newuserid":newuser.user_id,
                    "newuser_fname":newuser.firstname,
                    "newuser_lname":newuser.lastname,
                    "newuser_username":newuser.user_name,
                    "message":"New User Added Successfully"},201

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
                    "deck_score":deck.deck_score},200

    def delete(self,deckid):
        deck=Deck.query.filter_by(deck_id=deckid).first()
        if deck is None:
            raise ValidationError(404,"DVE1006","Deck does not exist")
        elif len(deck.cards)>0:
            raise ValidationError(404,"DVE1007","Deck has cards , delete them first")
        else:
            db.session.delete(deck)
            db.session.commit()
            return {"deck_id":deck.deck_id,
                    "deck_name":deck.deck_name,
                    "owner_userid":deck.owner_userid,
                    "last_reviewed": deck.last_reviewed,
                    "deck_score":deck.deck_score},200

    def post(self):
        args=deck_parser.parse_args()
        deckid,deckname,ownerid=args.get("deck_id",None),args.get("deck_name",None),args.get("owner_userid",None)
        deck=Deck.query.filter_by(deck_id=deckid).first()
        ownerDoesNotExists=User.query.filter_by(user_id=ownerid).first() is None
        if deck is not None:
            raise ValidationError(404,"DVE1001","Deck id is duplicate")
        elif deckname is None:
            raise ValidationError(404,"DVE1003","Deckname is required")
        elif ownerid is None:
            raise ValidationError(404,"DVE1004","Ownerid is needed")
        elif ownerDoesNotExists:
            raise ValidationError(404,"DVE1005","Ownerid is not Valid")
        else:
            newDeck=Deck(deck_name=deckname,
                        owner_userid=ownerid,
                        last_reviewed= datetime.utcnow().strftime('%d-%m-%Y %H:%M'),
                        deck_score=0)
            db.session.add(newDeck)
            db.session.commit()
            return {"deck_id":newDeck.deck_id,
                    "deck_name":newDeck.deck_name,
                    "owner_userid":newDeck.owner_userid,
                    "last_reviewed": newDeck.last_reviewed,
                    "deck_score":newDeck.deck_score},200

# RESTful API for CARD
class CardApi(Resource):

    def get(self,cardid):
        card=Card.query.filter_by(id=cardid).first()
        if card is None:
            raise ValidationError(404,"CVE1001","Card does not exist")
        else :
            return {"cardid": card.id,
                    "question":card.question,
                    "answer":card.answer,
                    "cardscore":card.card_score,
                    "parent_deckid":card.deck_id,
                    "last reviewed":card.last_reviewed},200

    def put(self,cardid):
        card=Card.query.filter_by(id=cardid).first()
        if card is None:
            raise ValidationError(404,"CVE1001","Card does not exist")
        else:
            args=card_parser.parse_args()
            question,answer=args.get("question",None),args.get("answer",None)
            if question is None:
                raise ValidationError(404,"CVE1002","question is required")
            elif answer is None:
                raise ValidationError(404,"CVE1003","answer is required")
            elif question==card.question:
                raise ValidationError(404,"CVE1004","Question is same as previous")
            elif answer==card.answer:
                raise ValidationError(404,"CVE1005","Answer is same as previous")
            else:
                card.question,card.answer=question,answer
                db.session.commit()
                return {"cardid": card.id,
                    "updated question":card.question,
                    "updated answer":card.answer,
                    "cardscore":card.card_score,
                    "parent_deckid":card.deck_id,
                    "last reviewed":card.last_reviewed},200

    def delete(self,cardid):
        card=Card.query.filter_by(id=cardid).first()
        if card is None:
            raise ValidationError(404,"CVE1001","Card does not exist")
        else:
            deck=Deck.query.filter_by(deck_id=card.deck_id).first()
            deck.deck_score-=card.card_score
            deck.last_reviewed= datetime.utcnow().strftime('%d-%m-%Y %H:%M')
            db.session.delete(card)
            db.session.commit()
            return {"deleted cardid": card.id,
                    "question":card.question,
                    "answer":card.answer,
                    "deleted cardscore":card.card_score,
                    "parent_deckid":card.deck_id,
                    "last reviewed":card.last_reviewed},200

    def post(self):
        args=post_card_parser.parse_args()
        question,answer,deckid=args.get("question",None),args.get("answer",None),args.get("deckid",None)
        if question is None:
            raise ValidationError(404,"CVE1002","question is required")
        elif answer is None:
            raise ValidationError(404,"CVE1003","answer is required")
        elif deckid is None:
            raise ValidationError(404,"CVE1004","deckid is required")
        elif Deck.query.filter_by(deck_id=deckid).first() is None:
            raise ValidationError(404,"CVE1005","Deck does not exist")
        else:
            card=Card(question=question,
            answer=answer,
            card_score=0,
            last_reviewed= datetime.utcnow().strftime('%d-%m-%Y %H:%M'),
            deck_id=deckid)
            db.session.add(card)
            db.session.commit()
            return {"created cardid": card.id,
                    "question":card.question,
                    "answer":card.answer,
                    "cardscore":card.card_score,
                    "parent_deckid":card.deck_id,
                    "last reviewed":card.last_reviewed},200