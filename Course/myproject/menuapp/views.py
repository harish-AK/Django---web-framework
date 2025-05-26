from django.shortcuts import render

# Create your views here.
def sample_data(request):
    name = request.GET.get('name')
    