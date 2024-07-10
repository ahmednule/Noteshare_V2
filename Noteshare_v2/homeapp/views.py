from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

# Create your views here.
def home(request):
    render(request, 'homeapp/home.html')

def about(request):
    render(request, 'homeapp/about.html')

def contact(request):
    render(request, 'homeapp/base.html')



def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Change to your home page or desired URL
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})



def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Change to your home page or desired URL
        else:
            error_message = "Invalid username or password"
            return render(request, 'homeapp/login.html', {'error_message': error_message})
