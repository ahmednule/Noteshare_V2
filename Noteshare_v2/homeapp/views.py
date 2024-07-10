from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'homeapp/home.html')

def about(request):
    return render(request, 'homeapp/about.html')

def contact(request):
    return render(request, 'homeapp/base.html')