# FlashcardV2

## Project Structure
```bash
.
├── backend
│   ├── application
│   │   ├── config.py
│   │   ├── controller
│   │   │   ├── api.py
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
│   ├── localbeat.sh
│   ├── localrun.sh
│   ├── localsetup.sh
│   ├── localworker.sh
│   ├── main.py
│   └── requirements.txt
├── FlashcardApp v2 - Modern Application Development - 2.pdf
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
│   │   └── router.js
│   └── vue.config.js
├── MAD2 project .pdf
└── README.md
```