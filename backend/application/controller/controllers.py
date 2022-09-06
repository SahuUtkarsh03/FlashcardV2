from flask import jsonify,  request , make_response , send_file
from flask import current_app as app
import datetime 
import jwt
from functools import wraps
import csv

from werkzeug.security import check_password_hash
from application.data.model import Card, Deck
from application.utils.helper import getUser
from application.data.database import db
from application.jobs.tasks import sendCSV as scsv


# a custom wrapper to check if there is a JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=["HS256"])
            # current_user = User.query.filter_by(public_id=data['public_id']).first()
            current_user = getUser(data['username'])
        except:
            return jsonify({'message' : 'Token is invalid! : {}'.format(token)}), 401

        return f(current_user, *args, **kwargs)

    return decorated

@app.route('/login',methods=['POST'])
def login():
    auth = request.authorization
    # print(auth)
    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    user = getUser(auth.username)
    # print(user)
    if not user:
        return make_response('Could not verify, Wrong username', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if check_password_hash(user.hashed_password, auth.password):
        # print(user)
        token = jwt.encode({'username' : user.user_name,
                            'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                            app.config['SECRET_KEY'],
                            algorithm="HS256")

        return make_response(token,200)

    return make_response('Could not verify, Wrong Password', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

@app.route("/senddeck/<deckid>",methods=['GET'])
@token_required
def sendCSV(current_user,deckid):
    job=scsv.delay(deckid)
    fields=['id','deck_id','question','answer','card_score','last_reviewed']
    res=job.wait()
    with open("Deck.csv",'w') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames = fields)
        writer.writeheader() 
        writer.writerows(res)
    return send_file("Deck.csv",as_attachment=True)

@app.route("/reviewcard/<cardid>",methods=['POST'])
@token_required
def reviewCard(current_user,cardid):
    if request.is_json:
        r = request.json
        score=r['score']
        card=Card.query.filter_by(id=int(cardid)).first()
        card.card_score=int(score)
        card.last_reviewed= datetime.datetime.utcnow().strftime('%d-%m-%Y %H:%M')
        deckid=card.deck_id
        deck=Deck.query.filter_by(deck_id=deckid).first()
        cards=deck.cards
        deckscore=0
        for card in cards: 
            deckscore+=card.card_score
        deck.deck_score=deckscore
        deck.last_reviewed= datetime.datetime.utcnow().strftime('%d-%m-%Y %H:%M')
        db.session.commit()
        return {"Msg":"Reviewed Successfully"},200
    else : return {"errMsg": "Not Json"}, 400

    pass

'''
@app.route("/createDeck", methods=['POST'])
@token_required
def createDeck(current_user):
    if request.is_json:
        r = request.json
        deck_name=r['deckname']
        deck=Deck.query.filter_by(deck_name = deck_name , owner_userid = int(current_user.user_id)).first()
        if deck is None:
            deck = Deck(deck_name = deck_name ,
            owner_userid = int(current_user.user_id),
            last_reviewed=datetime.datetime.utcnow().strftime('%d-%m-%Y %H:%M') ,
            deck_score=0)
            db.session.add(deck)
            db.session.commit()
            return {"Msg":"Deck Added Successfully"},201
        else : 
            return {"errMsg" : "Deck Exists"},409

    else: return {"errMsg": "Not Json"}, 400
'''

@app.route("/getdecks",methods=['GET'])
@token_required
def getDecks(current_user):
    res={}
    print(current_user.decks)
    for deck in current_user.decks: 
        print(deck)
        res[deck.deck_id]=deck.decktoJson()
    return jsonify(res),200

@app.route("/getcards/<deckid>",methods=['GET'])
@token_required
def getCards(current_user,deckid):
    res={}
    cards = Card.query.filter_by(deck_id= deckid).all()
    for card in cards: res[card.id]=card.toJson()
    return jsonify(res),200

@app.route("/", methods=['GET'])
def home():
    return "<h1>App is working</h1>"

