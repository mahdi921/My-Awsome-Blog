from django.urls import path
from accounts.views import login_view, logut_view, register_view, ResetPasswordView #, profile_view, profile_edit_view,
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
app_name = 'accounts'

urlpatterns = [
    path('login',login_view, name='login'),
    path('logout', logut_view, name='logout'),
    path('register', register_view, name='register'),
    path('password-reset', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html',
                                                     success_url=reverse_lazy('accounts:password_reset_complete')),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]