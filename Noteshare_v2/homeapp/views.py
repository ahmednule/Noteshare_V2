from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    render(request, 'homeapp/home.html')

def about(request):
    render(request, 'homeapp/about.html')

def contact(request):
    render(request, 'homeapp/base.html')