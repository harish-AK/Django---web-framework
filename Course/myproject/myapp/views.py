from django.shortcuts import render
from django.http import HttpResponse
from menuapp.models import Menu,MenuCategory
# Create your views here.

def home(request):
    path = request.path
    method = request.method
    response = HttpResponse()
    response.headers['AGE'] = 20
    content = f'''
    <h1>Welcome to my Django app!</h1>
    <br><p>Path: {path}</p>
    <br><p>Method: {method}</p>
    <br><h2>Headers: {response.headers}</h2>
    '''
    return HttpResponse(content, content_type='text/html',charset='utf-8')

def queryview(request):
    name = request.GET['name']
    id = request.GET['id']
    return HttpResponse(f"Name :{name} and ID :{id}")

def showform(request):
    return render(request,"myapp/inputform.html")

def getform(request):
    name = request.POST['name']
    id = request.POST['id']
    return HttpResponse(f"Name :{name} and ID :{id}")

def superheros(request,hero,hero_color=None):
    items = {
        "Batman":"Goated",
        "Superman":"Mid",
        "Flash":"Bad"
    }
    color = {
        "Batman":"Black",
        "Superman":"Blue",
        "Flash":"red"
    }
    rating = items[hero]
    if hero_color is not None:
        return HttpResponse(f"<h1>{hero}</h1> <h2>{items[hero]}</h2><h3>{color[hero]}</h3>")
    else:
        return HttpResponse(f"<h1>{hero}</h1> <h3>{items[hero]}</h3>")

def hello_html(request,name):
    context =  {"name":name}
    return render(request,'myapp/hello.html',context)


def dictview(request):
    menu_items = Menu.objects.all()
    context = {"menu_items":menu_items}
    return render(request,"myapp/menu_items.html",context)
