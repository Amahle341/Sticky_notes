# Sticky_notes
Django sticky notes application for note taking


FEATURES

User authentication (login & logout)

Create new notes

Edit existing notes

Delete notes

View all your personal notes

Each user only sees their own notes

PROJECT STRUCTURE

The project is organized as follows:

manage.py

db.sqlite3

home/

views.py

urls.py

templates/home/

welcome.html

login.html

logout.html

notes/

models.py

views.py

urls.py

templates/notes/

list.html

form.html

detail.html

sticky_notes/

settings.py

urls.py

wsgi.py

static/ (for CSS, JS, and image files)

TECHNOLOGIES USED

Python 3.13

Django 5

SQLite3 (default database)

HTML5, CSS3, Bootstrap 5

INSTALLATION AND SETUP

Clone the repository from GitHub:
git clone https://github.com/<your-username>/sticky-notes-django.git
Then open the project folder using:
cd sticky-notes-django

Create and activate a virtual environment:
python -m venv .venv
.venv\Scripts\activate (on Windows)

Install dependencies:
pip install django

Run database migrations:
python manage.py migrate

Create a superuser (optional):
python manage.py createsuperuser

Start the development server:
python manage.py runserver

Open your app in a browser at:
http://127.0.0.1:8000/

AUTHENTICATION

Only logged-in users can create, edit, or delete notes.

If a user isn’t logged in, they will automatically be redirected to the login page.

MODEL OVERVIEW

The Notes model includes the following fields:

title: Short text for the note’s title

content: The main body text of the note

created: Automatically stores the date and time when a note is created

user: Links each note to a specific user who created it

USER INTERFACE OVERVIEW

Home Page: Displays all notes belonging to the logged-in user.

Create Note Page: Provides a form for adding a new note.

Edit Note Page: Allows users to update their existing notes.

Login/Logout Pages: Use Django’s built-in authentication system.

AUTHOR

Ayanda
Software Engineering Student
Passionate about building simple, meaningful apps with Django and Python.
