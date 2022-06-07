# Breakable Toy for a contacts application.

## Description.
This project is a directory web application where you can manage your contacts.

## How to run the project locally.
The framework used was [Django, version 4.0](https://docs.djangoproject.com/en/4.0/).

This app also makes use of the package [python-decouple](https://pypi.org/project/python-decouple/), therefore you 
need to create an .env text file inside the outer contacts folder defining the following variables:

- DB_ENGINE. The database backend you define in the settings.py file.
- DB_NAME. The name of the database you'll connect to.
- DB_USER. The user name of the database.
- DB_PORT. The port number of the database connection.
- HOST. The host where the database is located.
- TIME_ZONE. The timezone for the database. 
- DEBUG. True or False for debuging mode.

Example:

DB_ENGINE=django.db.backends.postgresql\
DB_NAME=contacts\
DB_USER=admin\
DB_PORT=5432\
HOST=127.0.0.1\
DEBUG=True\
TIME_ZONE=America/Hermosillo

**Note:** the database needs to be created before running the project.

The database password is read from an environment variable called DB_PWD. You can define it like this:

$ read -s DB_PWD\
$ \
$ export DB_PWD

That way the password won't be written anywhere!

**Note:** when you close the terminal you have to define it again.

**Note:** if you are using sqlite, you only need to define TIME_ZONE and DEBUG. Although, all the variables have 
fallback values in the settings.py file in case you don't define any of them.

This project was developed using [PostgreSQL](https://www.postgresql.org/docs/current/).

