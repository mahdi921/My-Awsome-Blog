from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def login_view(request):
    return render(request, 'accounts/login.html')

def register_view(request):
    return render(request, 'accounts/register.html')

@login_required
def logut_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS,
                         "You have been logged out, redirecting to home page...")
    return redirect('/')
