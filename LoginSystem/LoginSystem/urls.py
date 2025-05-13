from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('', include('api.urls')),    # Route the root URL (/) to the 'api.urls'
]
