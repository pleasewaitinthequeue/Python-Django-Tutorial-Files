from django.urls import path

from . import views

app_name = 'humorously'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('jokesters', views.JokesterView.as_view(), name='jokesters'),
    path('redirect', views.RedirectView.as_view(), name='redirect'),
]
