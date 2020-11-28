from django.shortcuts import render
from .models import Projects

# Create your views here.
def index(request):
    context = {
        'projects': Projects.objects.all()
    }
    return render(request,'projects/index.html',context)