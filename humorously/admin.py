from django.contrib import admin

# Register your models here.
from .models import Jokester
# Each model that you'd like to be able to edit within the default administrative interface must be registered here
# Here is an example of what registration looked like for the polls app.

class JokesterAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['city_residence']}),
        (None, {'fields': ['state']}),
        (None, {'fields': ['zipcode']}),
        (None, {'fields': ['country']}),
        ('Timestamp', {'fields': ['created'], 'classes': ['collapse']}),
    ],
    list_display = ('__str__','created','email_address')
    list_filter = ['created']
    search_fields = ['__str__']
admin.site.register(Jokester)

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
"""

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
admin.site.register(Question, QuestionAdmin)

"""
