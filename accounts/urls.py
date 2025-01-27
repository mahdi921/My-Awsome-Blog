from django.urls import path
from accounts.views import login_view, register_view#, logut_view,

app_name = 'accounts'

urlpatterns = [
    path('login',login_view, name='login'),
    # path('logout', logut_view, name='logout'),
    path('register', register_view, name='register'),
]