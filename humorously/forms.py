from django import forms
from .models import Joke, Category, Jokester, Review, Club

class ProfileForm(forms.ModelForm):
    class Meta:
        proxy = True
        model = Jokester
        fields = ('city_residence','state','zipcode','country')

class JokeForm(forms.ModelForm):
    class Meta:
        model = Joke
        fields = ('category','title','text')

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

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title','score','text')


"""
class Review(models.Model):
    user = models.ForeignKey(
        User,
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
    def __str__(self):
        return self.title
"""

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ('name','title','description','address1','address2','city','state','zipcode','country')

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
"""
