import logging

from django.core.mail import send_mail
from django.conf import settings
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
from .forms import JokeForm, ProfileForm, ReviewForm, ClubForm

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
        return context

def edit_profile(request, pk):
    profile = get_object_or_404(Jokester, pk=pk)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile.save()
            send_mail(
                'Welcome to Humorous.ly',
                'Thank you for joining Humorous.ly, it means the world to us.  ',
                settings.EMAIL_HOST_USER,
                [ profile.user.email ],
            )
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
        return Jokester.objects.filter(created__lte=timezone.now()).order_by('-created')[:10]

class JokesterDetail(LoginRequiredMixin, generic.DetailView):
    model = Jokester
    template_name = "jokester.html"
    def get_queryset(self):
        return Jokester.objects.all()

class JokeListView(LoginRequiredMixin, generic.ListView):
    template_name = "jokes.html"
    context_object_name = "latest_joke_list"
    def get_queryset(self):
        return Joke.objects.order_by('?')[:10]

class JokeDetail(LoginRequiredMixin, generic.DetailView):
    model = Joke
    template_name = "joke.html"
    def get_queryset(self):
        return Joke.objects.all()

def joke_summary(request, pk):
    print(request)
    joke = get_object_or_404(Joke, pk=pk)
    reviews = Review.objects.filter(joke_id=pk)
    return render(request, 'joke_summary.html', { 'joke': joke, 'reviews': reviews})

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

def add_new_review(request, pk):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.joke_id = pk
            review.save()
            return redirect('/humorously/joke/%s/summary' % (review.joke_id), pk=review.joke_id)
    else:
        form = ReviewForm()
        return render(request, 'review_edit.html', {'form': form })

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

class ClubsView(LoginRequiredMixin, generic.ListView):
    model = Club
    template_name = 'clubs.html'
    context_object_name = 'latest_club_list'
    def get_queryset(self):
        return Club.objects.order_by('?')[:10]

class ClubDetailView(LoginRequiredMixin, generic.DetailView):
    model = Club
    template_name = 'club.html'
    def get_queryset(self):
        return Club.objects.all()

def add_new_club(request):
    if request.method == "POST":
        form = ClubForm(request.POST)
        if form.is_valid():
            club = form.save(commit=False)
            club.user = request.user
            club.save()
            return redirect('/humorously/club/%s/detail' % (club.id), pk=club.id)
    else:
        form = ClubForm()
        return render(request, 'club_edit.html', {'form': form })
