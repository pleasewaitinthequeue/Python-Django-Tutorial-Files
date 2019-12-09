from django.urls import path

from . import views

app_name = 'humorously'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about', views.AboutView.as_view(), name='about'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('jokesters', views.JokesterView.as_view(), name='jokesters'),
    path('jokester/<int:pk>/', views.JokesterDetail.as_view(), name='jokesterdetail'),
    path('jokes', views.JokeListView.as_view(), name='jokes'),
    path('joke/<int:pk>/', views.JokeDetail.as_view(), name='jokedetail'),
]
