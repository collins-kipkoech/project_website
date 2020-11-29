from django import forms

from .models import Projects

class PostProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['image','title','description']