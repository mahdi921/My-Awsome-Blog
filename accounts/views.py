from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            userinput = request.POST['username']
            try:
                username = User.objects.get(email=userinput).username
            except User.DoesNotExist:
                username = request.POST['username']
                if not User.objects.filter(username=username).exists():
                    messages.add_message(request, messages.ERROR,
                                         'Username or email does not exist, try again')
                    return redirect('/accounts/login')
            password = request.POST['password']
            data = {'username': username, 'password': password}
            form = AuthenticationForm(request=request, data=data)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.add_message(request, messages.SUCCESS,
                                         'Login successful, redirecting to home page...')
                    return redirect(reverse('website:index'))
            else:
                messages.add_message(request, messages.ERROR,
                                     'invalid credentials, try again')
        else:
            form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})
    else:
        messages.add_message(request, messages.ERROR,
                             "You are already logged in, redirecting to home page...")
        return redirect(reverse('website:index'))

def register_view(request):
    return render(request, 'accounts/register.html')

@login_required
def logut_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS,
                         "You have been logged out, redirecting to home page...")
    return redirect(reverse('website:index'))
