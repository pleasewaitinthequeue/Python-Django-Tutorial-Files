from django import forms
from .models import Joke, Category

class JokeForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), to_field_name="name")

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
