import logging

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from random import randint
from django.views.generic.base import RedirectView
#from django.contrib.auth.decorators import login_required
from .models import Jokester, Joke, Review, Category, Set, Act, Club
from .forms import JokeForm, ProfileForm

class IndexView(LoginRequiredMixin, generic.TemplateView):
    login_url = '/accounts/login'
    redirect_field_name = 'redirect_to'
    template_name = "index.html"
    context_object_name = "random_jokester"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random_jokester'] = Jokester.objects.order_by("?").first()
        print(Jokester.objects.order_by("?").query)
        context['random_joke'] = Joke.objects.order_by("?").first()
        context['random_club'] = Club.objects.order_by("?").first()
        context['popular_jokester'] = Jokester.objects.all().first()
        print(Jokester.objects.order_by("?").query)
        print(Joke.objects.order_by("?").query)
        print(Club.objects.order_by("?").query)
        print(Jokester.objects.all().query)
        return context

class AboutView(LoginRequiredMixin, generic.TemplateView):
    template_name = "about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = "profile.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user;
        print(self.request.user)
        return context

def edit_profile(request, pk):
    profile = get_object_or_404(Jokester, pk=pk)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile.save()
            return redirect('/humorously/profile', pk=profile.id)
    else:
        form = ProfileForm(instance=profile)
    print(render(request, 'profile_edit.html', {'form': form }))
    return render(request, 'profile_edit.html', {'form': form })

#@login_required todo / make views require authentication
class JokesterView(LoginRequiredMixin, generic.ListView):
    template_name = "jokesters.html"
    context_object_name = "latest_jokester_list"
    def get_queryset(self):
        print(Jokester.objects.filter(created__lte=timezone.now()).order_by('-created')[:10].query)
        return Jokester.objects.filter(created__lte=timezone.now()).order_by('-created')[:10]

class JokesterDetail(LoginRequiredMixin, generic.DetailView):
    model = Jokester
    template_name = "jokester.html"
    def get_queryset(self):
        print(Jokester.objects.all().query)
        return Jokester.objects.all()

class JokeListView(LoginRequiredMixin, generic.ListView):
    template_name = "jokes.html"
    context_object_name = "latest_joke_list"
    def get_queryset(self):
        print(Joke.objects.order_by('?')[:10].query)
        return Joke.objects.order_by('?')[:10]

class JokeDetail(LoginRequiredMixin, generic.DetailView):
    model = Joke
    template_name = "joke.html"
    def get_queryset(self):
        print(Joke.objects.all().query)
        return Joke.objects.all()

def add_new_joke(request):
    if request.method == "POST":
        form = JokeForm(request.POST)
        if form.is_valid():
            joke = form.save(commit=False)
            joke.user = request.user
            joke.save()
            return redirect('/humorously/joke/%s/detail' % (joke.id), pk=joke.id)
    else:
        form = JokeForm()
        return render(request, 'joke_edit.html', {'form': form})

def edit_joke(request, pk):
    joke = get_object_or_404(Joke, pk=pk)
    if request.method == "POST":
        form = JokeForm(request.POST, instance=joke)
        if form.is_valid():
            joke = form.save(commit=False)
            joke.user = request.user
            joke.save()
            return redirect('/humorously/joke/%s/detail' % (joke.id), pk=joke.id)
    else:
        form = JokeForm(instance=joke)
    return render(request, 'joke_edit.html', {'form': form})
