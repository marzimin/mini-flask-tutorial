# Flask and basic web dev tutorial

Goal:
Build a simple to do list website/web app & gain a basic understanding of web development.

Practice on:

- Templates & Static Content (HTML + CSS)
- Setup & Using SQLite and SQLAlchemy (data storage for tasks)
- Create a basic CRUD app (Create, Read, Update, Delete)
- Build app in containerized environment (Docker)
- (BONUS) Make the site look nicer with further CSS and JavaScript
- (BONUS) Deploy to Heroku

Steps (for future me to remember):

On CLI (working directory):

- `python3 -m venv venv && . venv/bin/activate` to set up virtual environment
- `pip3 install flask flask-sqlalchemy` to install packages in your venv
- `mkdir app && cd app` to make and move to app directory
- `touch app.py` to create app.py file in /app
- In /app `mkdir static/css` for css files and `mkdir templates` for html files
- When done `pip freeze > requirements.txt` to create .txt file - place in root directory
- `touch Dockerfile` in root directory too

## Run in Dockerized container

- Have Docker Desktop installed on your machine.
- git clone the project to your desired working directory

On CLI (root working directory - not /app):

Image name of python-flask-tutorial (or any name of choice)

Build/Update image by:
`docker build -t python-flask-tutorial .`

To run (creates a new container each time and deletes it when done ctrl+C in CLI):
    `docker run --rm -p 8000:8000 python-flask-tutorial`

Your CLI should then show the [localhost link](http://0.0.0.0:8000).
