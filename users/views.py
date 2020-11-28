from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

    else:
        form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request,'users/register.html',context)
