from django.urls import path,re_path
from . import views

app_name = "myapp"
urlpatterns = [
    path('',views.home,name='home'), # This is the home page
    path("getuser/",views.queryview,name = "queryview"),
    path("showform/",views.showform,name = "showform"),
    path("getform/",views.getform,name = "getform"),
    # path("superheros/<str:hero>",views.superheros,name="superheros"),
    # path("superheros/<str:hero>/<str:hero_color>",views.superheros,name="superheros"),
    re_path(r'^superheros/(?P<hero>[^/]+)(?:/(?P<hero_cd color>[^/]+))?/?$', views.superheros, name="superheros"),
]
