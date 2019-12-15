from django.contrib import admin

# Register your models here.
from .models import Jokester, Joke, Review, Category, Set, Act, Club
# Each model that you'd like to be able to edit within the default administrative interface must be registered here
# Here is an example of what registration looked like for the polls app.

class JokesterAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['city_residence']}),
        (None, {'fields': ['state']}),
        (None, {'fields': ['zipcode']}),
        (None, {'fields': ['country']}),
        (None, {'fields': ['photo_url']}),
    ]
    list_display = ('__str__','created')
    list_filter = ['created']
    search_fields = ['__str__']

class JokeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user']}),
        (None, {'fields': ['category']}),
        (None, {'fields': ['title']}),
        (None, {'fields': ['text']}),
    ]
    list_display = ('__str__','created')
    list_filter = ['created']
    search_fields = ['__str__','title','text']

"""
class Jokester(models.Model):
    last_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    email_address = models.CharField(max_length=150)
    city_residence = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=25)
    country = models.CharField(max_length=150)
    created = models.DateTimeField(
        default=datetime.now()
    )
    def __str__(self):
        return last_name + ', ' + first_name
"""
class ClubAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['title']}),
        (None, {'fields': ['address1']}),
        (None, {'fields': ['address2']}),
        (None, {'fields': ['city']}),
        (None, {'fields': ['state']}),
        (None, {'fields': ['country']}),
        ('Timestamp', {'fields': ['created'], 'classes':['collapse']}),
    ]
    list_display = ('__str__','created','full_address')
    list_filter = ['created']
    search_fields = ['__str__','title','text']
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
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=25)
    country = models.CharField(max_length=150)
    def __str__(self):
        return self.name
"""
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('name', 'description')}),
    ]
    list_display = ('__str__','description','created')
    list_filter = ['created']
    search_fields = ['__str__','name','description']
"""
category.py
============================
a description of category.py
categoryid varchar(10) (PK)
categoryname varchar(40)
categorydescription varchar(255) (max length or something like that)
"""

admin.site.register(Jokester, JokesterAdmin)
admin.site.register(Joke, JokeAdmin)
admin.site.register(Review)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Set)
admin.site.register(Act)
admin.site.register(Club)
