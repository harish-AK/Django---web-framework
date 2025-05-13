from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home_redirect(request):
    return redirect('/contacts/')  # Redirects root to contacts

urlpatterns = [
    path('', home_redirect),  # Redirects root URL to /contacts/
    path('admin/', admin.site.urls),
    path('contacts/', include('details.urls')),  
]
