from django.shortcuts import render
from .forms import DemoForm


# Create your views here.
def sample_data(request):
    form = DemoForm()
    context = {'form':form}
    return render(request,'form.html',context)

