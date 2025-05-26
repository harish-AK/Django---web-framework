from .forms import DemoForm
from django.urls import path,re_path
from . import views

app_name = "menuapp"
urlpatterns = [
    path('sampleform',views.sample_data,name='demoform'),
]