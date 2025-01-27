from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from accounts.forms import RegisterForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordResetView

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
                    return redirect(reverse('accounts:login'))
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
    if not request.user.is_authenticated:
        if request.method == "POST":
            data = {
                'username': request.POST.get('username'),
                'first_name': request.POST.get('first_name'),
                'last_name': request.POST.get('last_name'),
                'email': request.POST.get('email'),
                'password1': request.POST.get('password1'),
                'password2': request.POST.get('password2')
            }
            if User.objects.filter(username=data['username']).exists() or User.objects.filter(email=data['email']).exists():
                messages.add_message(request, messages.ERROR,
                                     "Username or email already exists")
                return redirect(reverse('accounts:register'))
            form = RegisterForm(data=data)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS,
                                     "Registration successful, redirecting to login page...")
                return redirect('/accounts/login')
            else:
                messages.add_message(request, messages.ERROR,
                                     "Check your input and try again")
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/register.html', context)
    else:
        messages.add_message(request, messages.INFO,
                             "Please log out first before registering, redirecting to home page...  ")
        return redirect(reverse('website:index'))


def logut_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.add_message(request, messages.SUCCESS,
                             "You have been logged out, redirecting to home page...")
        return redirect(reverse('website:index'))
    else:
        messages.add_message(request, messages.INFO,
                             "You are already logged out, redirecting to home page... ")
        return redirect(reverse('website:index'))

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_message = "We have emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you dont receive an email, " \
                      "please make sure you have entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('accounts:login')
