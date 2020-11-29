from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterUserForm,ProfileUpdateForm
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

@login_required
def profile_view(request):
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'Your account has been updated successfully')
            return redirect('profile')

    else:
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'profile_form':profile_form,
    }
    return render(request,'users/profile.html',context)

