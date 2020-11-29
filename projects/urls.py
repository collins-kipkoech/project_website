from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home-view'),
    path('details/<int:id>/',views.project_details,name='details'),
    path('post/',views.post_project,name='post_project'),
]