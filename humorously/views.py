import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from random import randint
from django.views.generic.base import RedirectView
#from django.contrib.auth.decorators import login_required
from .models import Jokester, Joke, Review, Category, Set, Act, Club

class RedirectView(RedirectView):
    permanent = False
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user is not None and self.request.user.is_superuser:
            return reverse('/admin')
        else:
            return '/accounts/login'
#@login_required todo / make views require authentication
#@login_required
class IndexView(generic.TemplateView):
    template_name = "index.html"
    context_object_name = "random_jokester"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random_jokester'] = Jokester.objects.order_by("?").first()
        context['random_joke'] = Joke.objects.order_by("?").first()
        context['random_club'] = Club.objects.order_by("?").first()
        context['popular_jokester'] = Jokester.objects.all().first()
        return context

#@login_required todo / make views require authentication
class JokesterView(generic.ListView):
    template_name = "jokesters.html"
    context_object_name = "latest_jokester_list"
    def get_queryset(self):
        print(Jokester.objects.filter(created__lte=timezone.now()).order_by('-created')[:10])
        return Jokester.objects.filter(created__lte=timezone.now()).order_by('-created')[:10]

class JokeListView(generic.ListView):
    print('JokeListView()')
    template_name = "jokes.html"
    conext_object_name = "latest_joke_list"
    def get_queryset(self):
        print(Joke.objects.order_by('-created')[:10])
        return Joke.objects.order_by('-created')[:10]
