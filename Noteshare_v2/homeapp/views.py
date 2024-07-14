from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'homeapp/home.html')

def about(request):
    return render(request, 'homeapp/about.html')

def base(request):
    return render(request, 'homeapp/base.html')

def signup(request):
    return render(request, 'homeapp/signup.html')