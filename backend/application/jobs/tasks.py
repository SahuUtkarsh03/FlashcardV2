from application.jobs.workers import celery
from application.data.model import Card,User
from celery.schedules import crontab
from application.utils.mail import sendEmail


@celery.task
def sendMailToAll():
    users=User.query.all()
    print(users)
    for user in users:
        print([deck.last_reviewed for deck in user.decks])
        sendEmail(
            user.email,
            "Hello {}".format(user.firstname),
            '''
            I hope that you would be doing great.
            Don't forget to revise your Flash Cards.

            Have a great Day.

            Regards,
            Utkarsh Sahu
            '''
        )
        

@celery.task
def sendCSV(deckid):
    '''
    an async function to return the list of JSON of cards...
    '''
    cards = Card.query.filter_by(deck_id= deckid).all()
    return [card.toJson() for card in cards]
    
@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):

    sender.add_periodic_task(
        crontab(minute=59,hour=23),
        sendMailToAll.s(),
        name="Mail testing"
        )