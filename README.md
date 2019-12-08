# Python Django Tutorial Files (Main)

## Index
1. [Project Root (that's where we are!)](./README.md)
2. [/Project/Project](./mysite/project.md)
3. [/Project/App](./polls/app.md)

## Project Master Checklist
The master checklist is divided into Functional Requirements - things that are required to make the website usable, and Technical Requirements - things that are required to score points on our final project.  It is implied that our goal is to build a website that uses Djangos MVT model to connect the Pythonic front end, to the Relational Oracle Database Back End.  Below you will find the checklists for each.
### Functional Requirements (Minimum Viable Product)
- [ ] Homepage - Random Objects from the Database on it
  - [ ] Procedure / Function to get Random:  Joke, User, Category, Set
- [ ] Search Page (package?)
  - [ ] Procedure / Function to search in different ways using user keywords using dependencies
- [ ] User Account Page
  - [ ] Keep User Authentication nearby due to authentication **
  - [ ] Extend Default User Object Model?
- [ ] Joke View Page
  - [ ] Show Joke / User that created Joke / Stole / Joke Stealing***
  - [ ] Create Function / Procedure / Package for Joke Statistics / Reviews / Review Statistics
- [ ] Create Joke Page
- [ ] Create Review Page
- [ ] About Us Page - Static Page

### Technical Requirements (What we need to do for an A+)
- [ ] Sql Queries - select, update, insert - demonstrate connection between Object Relational Map and the Backend **(10 points)**
- [ ] Program Design / Flow Charts / Create Basic PL/SQL Block **(10 points)**
  - [x] Entity Relationship Diagram (Angie)
  - [ ] Use Case Diagram / Class Diagram
- [ ] Altering Table Structures / Cursors **(10 points)**
  - [ ] Search Function can Return Cursor(s)
  - [ ] Search Results will be displayed to the User in the GUI
- [ ] Procedures / Functions (at least one of each) **(24 points)**
  - [ ] Ins / Outs / Returns - need to infer this based on class diagram
  - [ ] Stored Procedures / Functions - return all the reviews for a joke
- [ ] Packages **(12 points)**
  - [ ] Search Package? - can use overloading to allow for different types of search
  - [ ] Joke Statistics?  - can bundle multiple functions / procedures into a package that will return Joke Stats and Review Information
- [ ] Program Unit Dependencies **(12 points)**
  - [ ] Functions / Procedures
  - [ ] Views / Tables
- [ ] Database Triggers **(12 points)**
  - [ ] Might be convenient to aggregate joke statistics
  - [ ] Convenient to aggregate user statistics

## Project Installation Instructions

### Clone Project to Your Local Machine
Windows Instructions (Linux and Apple may be Similar)
1. Follow instructions above for Setting Up Anaconda / Python / Django Environment with Atom IDE.  If you prefer another IDE you may use it.
2. Install [Oracle XE 18c](https://download.oracle.com/otn/nt/oracle18c/180000/OracleXE184_Win64.zip) and configure your database to accept a connection like the one described in settings.py (create a connection for 'system' with password 'admin')
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'xe',
        'USER': 'system',
        'PASSWORD': 'admin',
        'HOST': '',
        'PORT': '1521',
    }
}
```
3. Install cx_Oracle Driver using python command:  ```python -m pip install cx_Oracle --upgrade```
4. If you do not have [Git Command Line interface](https://git-scm.com/downloads), you may need to install it.  To check type in ```git --version``` on your terminal or command prompt - if your system spits out a version number, you have already installed it.
1. You can now clone the project by switching to the directory in which you want to clone the project to using ```cd directoryname``` and then typing ```git clone https://github.iu.edu/jomalair/Python-Django-Tutorial-Files.git```.
2. If this is your first time setting up the django project you may have to run ```python manage.py makemigrations``` followed by ```python manage.py migrate --fake-initial``` which instructs the the interpreter to ignore later migration files.  Migration files instruct the system to make changes to your database.
3. Keep in mind that if you're connecting to the database the first time you will also need to use the ```python manage.py createsuperuser``` command to create any usernames and passwords which you might need to login - the framework does not include any data in the database, it simply sets up a blank one.  
2. If you have installed all the necessary dependencies, then once you are done, you should be able to type ```python manage.py runserver``` and see a screen similar to this:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 29, 2019 - 13:48:30
Django version 2.2.6, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Setup Anaconda / Django / Atom
Windows Instructions (Linux and Apple may be similar).
1. [Install Anaconda](https://www.anaconda.com/distribution/), which is a set of tools that comes with Python distributions.  Optionally, you can install Python, but keep in mind that the commands below for creating your first project explicitly use 'conda' rather than the equivalent python or django commands.  To make sure that you have correctly installed Anaconda go to the Command Prompt or Terminal and type:  `conda info --all` which should spit out a number of details about your configuration environment.
2. Install the [Atom Integrated Development Environment (IDE)](https://atom.io)
3.    Use the Atom package installer (**File >> Settings >> Install**) to add the following packages:
  + platformio-ide-terminal - this package provides a terminal window to use in Atom
  + language-markdown - this package helps Atom understand and write [Markdown Language](https://daringfireball.net/projects/markdown/syntax)
  + markdown-writer - this package helps Atom write files in the correct .md format
  + markdown-preview (this may already be installed) - this package allows you to preview markdown files in your Atom IDE
1. Install [The Django Framework](https://www.djangoproject.com) by using `pip install django` or alternatively `conda install django` (Anaconda comes with its own package manager).  [Pip](https://pypi.org/project/pip/) is the Default Package Manager for Python.  When complete, you should be able to check the versions of Python `python --version` and Django `python -m django version`.

### Create your First Project
Windows / Mac / Linux Instructions (should use same commands)
1. Using the Command Prompt or Terminal program, Create a new Project `django-admin startproject [mysite]` where **mysite** refers to the name of the project.  The command should create a new directory in which it will write all of your project files.
2. Navigate your Command Prompt or Terminal into your project directory `cd mysite` before setting up a virtual python environment.
3. Set up a virtual environment by calling:  `conda create --name mysite python=3.6` where mysite is the name of your project.
4. Activate your virtual environment by calling:  `conda activate mysite`
5. To begin Running our Default Application in the Virtual Environment, type:  `python manage.py runserver`, this command is equivalent to `npm start` in Node, and instructs the computer to run scripts that will start running a test server at an address local to your machine.
6. To view the server in your web browser, copy and paste the address (yours may differ from mine) into your web browser:  `http://127.0.0.1:8000`
7. Typing `Ctrl + C` into your Command Prompt / Terminal will kill the Server, which can be restarted by repeating the command `python manage.py runserver`
8. The runserver command builds a rapid testing environment which is not intended for production use.


### Follow Tutorial to build Polls App
[Django Tutorials to Build a Polls App](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)

Django is a **Model, View, Template (MVT)** framework.

[The Django 8 Hour Course](https://www.youtube.com/watch?v=JT80XhYJdBw&t) goes through the tutorial at a high level, but can be difficult to follow.  Make sure you have both resources open if you choose to work through the video.

### Migrating to Oracle XE
In order to migrate, you must upgrade to version 12+ of the XE database.  XE is Oracle's open source tool which can be downloaded free from its website. The version that was used can be downloaded [here](https://www.oracle.com/database/technologies/xe-downloads.html) for Windows.  Note that you will need to unzip these files prior to being able to install Oracle XE.  Oracle Requires acceptance of the license agreement, and you may have to create an Oracle Account in order to signin and begin the download.  You also need to install a driver so that python can talk directly to Oracle.  In the terminal type:
```
python -m pip install cx_Oracle --upgrade
```
Next, after Oracle XE has been installed, and we have the python driver we are ready to Migrate the application to the new database.  When we migrate, we are migrating our Object Relational Mapping only, not the specific records from our application.  Therefore, this should not be done with a fully developed application.  All knowledge of specific object records will be lost, but it's a snap to recreate them using Django Admin.

Navigate to [settings.py](./mysite/settings.py) in the your project directory.  According to the tutorial, our project is actually called 'mysite' and it has an app in it called 'polls'.  The connection information for your Oracle XE database will need to be specified.  Note below how the old connection information has been commented out.  Your connection information may be different - the connection information below reflects this database superuser password which is set during the installation process.
```
#Before Editing Settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

===========================================================

#After Editing Settings.py
DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'xe',
        'USER': 'system',
        'PASSWORD': 'admin',
        'HOST': '',
        'PORT': '1521',
    }
}
```
Now you are ready to ask python to migrate your application.
```
python manage.py migrate
```
If there is nothing wrong, you will get a long list of OKs like the example below:
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying polls.0001_initial... OK
  Applying sessions.0001_initial... OK
```

If you are like me, you may have forgotten your superuser account and password in Python.  To create another one, simply run:
```
python manage.py createsuperuser
```
You should be able to run your server now, and it should by default create all of the object definitions that were in your previous database.  You can confirm this by running:
```
python manage.py runserver
```
Django should successfully start itself up with a connection to the database.
```
Performing system checks...

System check identified no issues (0 silenced).
November 09, 2019 - 15:26:39
Django version 2.2.6, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
To confirm that the migration was successful, simply visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and login with the superuser credentials that you created.  You should be able to add new objects using the Administrative menu.  To confirm that the information is being written to the database, you can use a tool like [Oracle SQL Developer](https://www.oracle.com/database/technologies/appdev/sql-developer.html) to connect to your default database and verify that the tables were created and populated.

### Creating a new 'App'

An app lives behind your 'project' path.  Many python apps can live in the same project.  You create a new app by typing the following command into the command prompt:

```
python manage.py startapp appname
```

This will create a new directory with the following files:

```
/project/appname/
  __init__.py
  admin.py
  apps.py
  migrations/
    __init__.py
  models.py
  tests.py
  views.py
```
