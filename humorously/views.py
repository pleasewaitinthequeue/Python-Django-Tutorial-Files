from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
#from django.contrib.auth.decorators import login_required
from .models import Jokester
# Create your views here.
#@login_required

def index(request):
    return HttpResponse("<h1>Under construction.</h1>")
    #template_name = 'humorously/index.html'
class JokesterView(generic.ListView):
    template_name = "jokesters.html"
    context_object_name = 'latest_jokester_list'
    """
        return the top 10 jokesters, with a created date == today
    """
    def get_queryset(self):
        return Jokester.objects.filter(
            created__lte=timezone.now()).order_by('-created')[:10]
