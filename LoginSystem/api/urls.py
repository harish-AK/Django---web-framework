from django.urls import path
from .views import user_register, user_login, index, home, user_logout

urlpatterns = [
    path('', index, name="index"),              # Home page or landing page
    path('register/', user_register, name="register"),  # Registration page
    path('login/', user_login, name="login"),            # Login page
    path('home/', home, name='home'),                  # Redirected after login
    path('logout/', user_logout, name='logout'),         # Logout page
]
