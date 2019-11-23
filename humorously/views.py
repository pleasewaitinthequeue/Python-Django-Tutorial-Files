from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Under construction.</h1>")
    #template_name = 'humorously/index.html'
