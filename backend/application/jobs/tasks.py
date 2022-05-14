from application.jobs.workers import celery
from application.data.model import Card,User
from celery.schedules import crontab
from datetime import timedelta , datetime
from application.utils.mail import sendEmail

@celery.task
def checkIfRevised():
    users=User.query.all()
    for user in users:
        for deck in user.decks:
            if (deck.last_reviewed - timedelta(days=1)) > datetime.utcnow().strftime('%d-%m-%Y %H:%M'):
                sendEmail(user.email,"FLASHCARD Reminder","Please Review Your FlashCards")


@celery.task
def sayHello(un):
    return "Hello{}".format(un)
    
@celery.task
def sendCSV(deckid):
    res=[]
    fields=['id','deck_id','question','answer','card_score','last_reviewed']
    cards = Card.query.filter_by(deck_id= deckid).all()
    for card in cards : res.append(card.toJson())
    return res,fields
    
@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=11,minute=59),
        checkIfRevised.s()
        )
    
    sender.add_periodic_task(
        crontab(minute=2),
        sayHello.s("Utkarsh")
        )