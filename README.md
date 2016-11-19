# Tango With Django

A python web app built using `Python 3.5.2` and `Django 1.10.2` that works through the book _[Tango with Django](http://www.tangowithdjango.com/book17/chapters/setup.html)_. The project currently includes two models, user authentication, a PostgreSQL database, and a customized admin interface.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Install postgreSQL for [Mac](https://launchschool.com/blog/how-to-install-postgresql-on-a-mac) or [Windows](https://www.tutorialspoint.com/postgresql/postgresql_environment.htm).

Download and install [python release 3.5.2](https://www.python.org/downloads/release/python-352/) and python's package manager [pip](https://packaging.python.org/installing/#install-pip-setuptools-and-wheel).

Note: If you have Python 2 >=2.7.9 or Python 3 >=3.4 installed from python.org, you will already have pip and setuptools, but will need to upgrade to the latest version:

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

   # launch the postgres shell
   psql

   # create the database
   davenestoff=# CREATE DATABASE tango_with_django;

   # exit the postgres shell
   davenestoff=# \q
   
   # migrate to complete db setup
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

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
