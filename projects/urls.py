from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home-view'),
    path('details/<int:id>/',views.project_details,name='details'),
    path('post/',views.post_project,name='post_project'),
    path('api/projects/', views.ProjectsList.as_view()),
    path('api/project/project-id/<int:pk>/',views.ProjectDescription.as_view()),
    path('rate/<int:pk>/',views.rate_project,name='rate'),
]