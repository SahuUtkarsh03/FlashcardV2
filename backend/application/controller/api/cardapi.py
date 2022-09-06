from flask_restful import Resource
from datetime import datetime

from application.data.database import db
from application.data.model import Deck,Card
from application.utils.validation import ValidationError
from application.utils.parser import *



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