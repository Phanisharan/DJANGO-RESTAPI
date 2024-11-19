"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TaskListView.as_view(), name='task-list'),
    path('tasks/<uuid:id>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='create-task'),
    path('tasks/update/<uuid:id>/', views.TaskUpdateView.as_view(), name='update-task'),
    path('tasks/delete/<uuid:id>/', views.TaskDeleteView.as_view(), name='delete-task'),
    path('tasks/complete/<uuid:id>/', views.TaskCompleteView.as_view(), name='complete-task'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
