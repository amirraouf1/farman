"""
Definition of urls for farman.
"""

from datetime import datetime
from django.urls import path, include  # Import 'include' for app URL inclusion
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views as app_views  # Add `as app_views` to prevent naming conflicts

urlpatterns = [
    path('', app_views.home, name='home'),  # Reference `home` view explicitly from `app_views`
    path('contact/', app_views.contact, name='contact'),  # Reference `contact` view explicitly from `app_views`
    path('about/', app_views.about, name='about'),  # Reference `about` view explicitly from `app_views`
    path(
        'login/',
        LoginView.as_view(
            template_name='app/login.html',
            authentication_form=forms.BootstrapAuthenticationForm,
            extra_context={
                'title': 'Log in',
                'year': datetime.now().year,
            }
        ),
        name='login'
    ),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),  # Only one 'admin/' path needed
    path('personel/', include('personel.urls')),  # Include URLs from the 'personel' app
]
