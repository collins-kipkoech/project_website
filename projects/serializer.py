from rest_framework import serializers
from .models import ProjectsApi

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsApi
        fields = ('title', 'description')