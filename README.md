# Tango With Django

A python web app built using `Python 3.5.2` and `Django 1.10.2` that works through the book _[Tango with Django](http://www.tangowithdjango.com/book17/chapters/setup.html)_. The project currently includes two models, user authentication, a PostgreSQL database, and a customized admin interface.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Install postgreSQL for [Mac](https://launchschool.com/blog/how-to-install-postgresql-on-a-mac) or [Windows](https://www.tutorialspoint.com/postgresql/postgresql_environment.htm).

Download and install [python release 3.5.2](https://www.python.org/downloads/release/python-352/) and python's package manager [pip](https://packaging.python.org/installing/#install-pip-setuptools-and-wheel).

_Note: If you have Python 2 >=2.7.9 or Python 3 >=3.4 installed from python.org, you will already have pip and setuptools, but will need to upgrade to the latest version:_

#### On Linux or OS X:
`   pip install -U pip setuptools`

#### On Windows:
`   python -m pip install -U pip setuptools`

Once pip has been installed, download `virtualenv` for setting up a virtual environment where you can run python 3.5 (especially necessary on OSX where python 2.7 comes native).

```

   pip install virtualenv (15.0.3)
   virtualenv <dir>
   source <dir>/bin/activate
   pip install django psycopg2

```

### Installing

To get the development environment up and running, clone the repository and then migrate all existing model information:

```

   git clone https://github.com/dnestoff/Tango-With-Django.git

```
Create the database by opening up postreSQL's interactive environment:
```

   # launches postgres shell
   psql

   # creates database
   davenestoff=# CREATE DATABASE tango_with_django;

   # exits postgres shell
   davenestoff=# \q
   
   # migration to complete db setup
   python manage.py migrate
   
```

Once complete, run the models and migrations and seed the data. 

```

   python manage.py makemigrations
   python manage.py migrate

   # seeding the database with the population script
   python populate_rango.py

      Starting Rango population script...
      
```

Once the migrations have been made, launch the application from a browser at `http://localhost:8000/rango/`. In a second tab, launch the admin panel at `http://localhost:8000/rango/`. 

### Using the app

(To be completed) 

## Running the tests

(To be completed)

## Coming up

Upcoming features for this project include:

- Session set-up and tracking
- Django Registration Redux
- jQuery and AJAX additions

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to Leif Azzopardi and David Campbell, the authors of [Tango With Django](http://www.tangowithdjango.com/)
