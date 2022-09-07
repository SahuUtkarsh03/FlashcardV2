# FlashcardV2

 FlashCard is a web application used specifically for Language or memory training. Users can Register & Login to create multiple Decks and Multiple cards. They can review them and get scored on that basis.

## Prerequisites

NOTE: ```This won't work on Windows as we need Redis and it is not supported on Windows, instead you will need WSL or Docker, however a Linux Sytem would be best as all you would be able to use all .sh files that help in setup and running```

1) [Python3](https://www.python.org/downloads/) and [Pip3](https://pypi.org/project/pip/)
2) [NodeJS](https://nodejs.org/en/)
3) [Redis](https://redis.io/) & [RESP](https://resp.app/)
4) [MailHog](https://github.com/mailhog/MailHog)

## Project Structure

``` bash
.
├── backend
│   ├── application
│   │   ├── config.py
│   │   ├── controller
│   │   │   ├── api
│   │   │   │   ├── cardapi.py
│   │   │   │   ├── deckapi.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── userapi.py
│   │   │   ├── controllers.py
│   │   │   └── __init__.py
│   │   ├── data
│   │   │   ├── database.py
│   │   │   ├── __init__.py
│   │   │   └── model.py
│   │   ├── __init__.py
│   │   ├── jobs
│   │   │   ├── __init__.py
│   │   │   ├── tasks.py
│   │   │   └── workers.py
│   │   └── utils
│   │       ├── helper.py
│   │       ├── __init__.py
│   │       ├── mail.py
│   │       ├── parser.py
│   │       └── validation.py
│   ├── celerybeat-schedule
│   ├── db
│   │   └── test_db.sqlite3
│   ├── Deck.csv
│   ├── localbeat.sh
│   ├── localrun.sh
│   ├── localsetup.sh
│   ├── localworker.sh
│   ├── main.py
│   └── requirements.txt
├── frontend
│   ├── babel.config.js
│   ├── jsconfig.json
│   ├── package.json
│   ├── package-lock.json
│   ├── public
│   │   └── index.html
│   ├── README.md
│   ├── src
│   │   ├── App.vue
│   │   ├── components
│   │   │   ├── AddCard.vue
│   │   │   ├── AddDeck.vue
│   │   │   ├── CardBody.vue
│   │   │   ├── DashBoard.vue
│   │   │   ├── DeckCard.vue
│   │   │   ├── HomePage.vue
│   │   │   ├── NavBar.vue
│   │   │   ├── ReviewCard.vue
│   │   │   ├── UserLogin.vue
│   │   │   ├── UserRegister.vue
│   │   │   └── ViewCards.vue
│   │   ├── main.js
│   │   ├── router.js
│   │   └── store
│   │       ├── index.js
│   │       └── modules
│   │           ├── deck.js
│   │           └── user.js
│   └── vue.config.js
├── MAD2 project .pdf
├── README.md
```

## Setup

* Clone the repository:

    ```bash
    git clone https://github.com/utkarsh4tech/FlashcardV2.git
    ```

* Setting Up Backend:

  * ```bash
    cd  backend/
    ```

  * ```bash
    source  localsetup.sh
    ```

  * ```bash
    source localrun.sh
    ```

  * ```bash
    source localbeat.sh
    ```

  * ```bash
    source localworker.sh
    ```

* Setting up frontend:

  * ```bash
    cd  frontend/
    ```

  * ```javascript
    npm i
    ```

  * ```javascript
    npm run serve
    ```

* Setting Up MailHog:

  ```bash
  ~/go/bin/MailHog
  ```

## Tech Stack Used

* Frontend : ```Vue.Js```
* Backend : ```Flask```
* API : ```Flask Restful```
* Authentication : ```JWT token```
* Database : ```Sqlite3```
* ORM : ```Flask-SQL Alchemy```
* Cache : ```Redis```
* Message Broker : ```Redis```
* Task-Queue : ```Celery```

## Demo

Watch this [video](https://drive.google.com/file/d/1u0taRTB9z3Cotcw0vvuyt9RVdUcgfOAN/view?usp=sharing) to know more about the project.

## Features

* Secure Login Using JWT
* Deck Management using APIs
* Export a Deck as a CSV (Asynchronous Task)
* Review Deck
* Daily Scheduled Reminders

## To-Do's

* Add feature to import a CSV to create deck
* Add Jinja Template to Mails
* Send Monthly Progress Report
* Improve UI / Add Animations for Card Review
