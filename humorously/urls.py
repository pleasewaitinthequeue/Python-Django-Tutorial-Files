from django.urls import path

from . import views

app_name = 'humorously'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about', views.AboutView.as_view(), name='about'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/edit', views.edit_profile, name='profileedit'),
    path('jokesters', views.JokesterView.as_view(), name='jokesters'),
    path('jokester/<int:pk>/', views.JokesterDetail.as_view(), name='jokesterdetail'),
    path('jokes', views.JokeListView.as_view(), name='jokes'),
    path('joke/<int:pk>/detail', views.JokeDetail.as_view(), name='jokedetail'),
    path('joke/add', views.add_new_joke, name='jokeadd'),
    path('joke/<int:pk>/edit', views.edit_joke, name='jokeedit'),
    path('joke/<int:pk>/summary', views.joke_summary, name='jokesummary'),
    path('joke/<int:pk>/reviews/add', views.add_new_review, name='addnewreview'),
    path('clubs', views.ClubsView.as_view(), name='clubs'),
    path('club/<int:pk>/detail', views.ClubDetailView.as_view(), name='clubdetail'),
    path('club/add', views.add_new_club, name='addclub'),
    #path('', views.SearchView.as_view(), name='searchjokes'),
    path('search/', views.SearchJokesView.as_view(), name='searchresults'),
]
