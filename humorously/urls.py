from django.urls import path

from . import views

app_name = 'humorously'
urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('jokesters', views.JokesterView.as_view(), name='jokesters')
]
