import datetime

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# models that are currently in 'the jokeable' lucidchart
# https://www.lucidchart.com/documents/edit/920b7f8e-419b-4316-b131-b79178fd8c96/


# Django has a built in User Object - here is a link to the documentation
# https://docs.djangoproject.com/en/2.2/topics/auth/default/
class Jokester(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )
    city_residence = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=25)
    country = models.CharField(max_length=150)
    created = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return self.user.last_name + ", " + self.user.first_name

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Jokester.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.jokester.save()

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

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1024)
    created = models.DateTimeField(
        auto_now_add=True #had problems with datetimes evaluating to a specific date and time on the migration side.  auto_now_add is a bit that django has included to tell the database we want a default timestamp
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"
"""
category.py
============================
a description of category.py
categoryid varchar(10) (PK)
categoryname varchar(40)
categorydescription varchar(255) (max length or something like that)
"""
class Joke(models.Model):
    user = models.ForeignKey(
        User,#even though we don't specify a class for the user, this should relate back to the django.auth.user model that is included with the framework by default
        on_delete=models.CASCADE,#this should delete any jokes a user creates if they are deleted
        related_name='+', #setting this to '+' tells the framework that we don't want to relate the user back to the joke on the other side, we just want the id on this side.
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='+',
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=1024)
    def __str__(self):
        return self.title

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
class Review(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='+',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='+',
    )
    joke = models.ForeignKey(
        Joke,
        on_delete=models.CASCADE,
        related_name='+',
    )
    score = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=1024)
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
class Set(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='+',
    )
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1024)
"""
set.py
==============================
setid Number(10) (PK)
userid number(10) (FK)
setname varchar(40)
setdescription varchar(255) (max length or something like that)
"""
class Act(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='+',
    )
    set = models.ForeignKey(
        Set,
        on_delete=models.CASCADE,
        related_name='+',
    )
"""
act.py
===============================
actid Number(10) (PK)
userid Number(10) (FK)
setid Number(10) (FK)
actname varchar(40)
actdescription varchar(255) (max length or something like that)
"""

class Club(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='+',
    )
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1024)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True, default='')
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=25)
    country = models.CharField(max_length=150)
    def __str__(self):
        return self.name
    def full_address(self):
        return self.address1 + ' | ' + self.address2 + ' | ' + self.city + ', ' + self.state + ' ' + self.zipcode + ' | ' + self.country
