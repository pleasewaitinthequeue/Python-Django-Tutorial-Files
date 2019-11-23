from django.db import models

# Create your models here.

# models that are currently in 'the jokeable' lucidchart
# https://www.lucidchart.com/documents/edit/920b7f8e-419b-4316-b131-b79178fd8c96/


# Django has a built in User Object - here is a link to the documentation
# https://docs.djangoproject.com/en/2.2/topics/auth/default/
"""
a description of user.py
=======================
userid Number(10) (PK)
lastname varchar(25)
firstname varchar(25)
emailaddress varchar(40)
cityresidence char(10) (maybe make the limit higher here)
state char(2) (maybe make the limit hold the whole state name?)
(suggested:  zipcode varchar(25) (internationalization and zip+4))
(suggested: country (varchar(50)))
(suggested:  photoURL - this can be selected from a static list of assets in the app)
"""

"""
category.py
============================
a description of category.py
categoryid varchar(10) (PK)
categoryname varchar(40)
categorydescription varchar(255) (max length or something like that)
"""

"""
joke.py
============================
jokeid number(10) (PK)
userid number(10) (FK)
categoryid varchar(10) (FK)
datecreated (date)
joketitle varchar(40)
joketext varchar(350)
"""

"""
review.py
=============================
reviewid Number(10) (PK)
userid Number(10) (FK)
jokeid Number(10) (FK)
score Number(1)
reviewtitle varchar(40)
reviewtext varchar(255) (max length or something like that)
"""

"""
set.py
==============================
setid Number(10) (PK)
userid number(10) (FK)
setname varchar(40)
setdescription varchar(255) (max length or something like that)
"""

"""
act.py
===============================
actid Number(10) (PK)
userid Number(10) (FK)
setid Number(10) (FK)
actname varchar(40)
actdescription varchar(255) (max length or something like that)
"""
