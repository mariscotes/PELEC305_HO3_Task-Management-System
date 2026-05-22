from django.urls import path
from . import views

urlpatterns = [
    path('api/tasks/', views.TaskListCreate.as_view(), name='task-list-create'),
]