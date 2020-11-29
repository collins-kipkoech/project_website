from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterUserForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your account has been created successfully')
            return redirect('login')


    else:
        form = RegisterUserForm()
        
    context = {
        'form':form
    }
    return render(request,'users/register.html',context)



