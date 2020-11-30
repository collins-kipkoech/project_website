from django.shortcuts import render,get_object_or_404,redirect
from .models import Projects
from .forms import PostProjectsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cloudinary.forms import cl_init_js_callbacks


# Create your views here.
def index(request):
    projects = Projects.objects.all()
    query = request.GET.get('q')
    if query:
        projects = projects.filter(title__icontains=query)

    context = {
        'projects': projects,
    }
    return render(request,'projects/index.html',context)

def project_details(request,id):
    project = get_object_or_404(Projects,id=id)
    context = {
        'project':project,
    }
    return render(request,'projects/details.html',context)

@login_required
def post_project(request):
    if request.method == 'POST':
        print(request.POST)
        form = PostProjectsForm(request.POST,request.FILES)
        if form.is_valid():
            addProject = form.save(commit=False)
            addProject.save()
            
            messages.success(request,'Your project has been posted successfully')
            return redirect('home-view')

    else:
        form = PostProjectsForm()
    context = {'form':form,}
    return render(request,'projects/post_projects.html',context)