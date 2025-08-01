"""
URL configuration for Todo_List project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from home import views


urlpatterns = [
    path('', views.home, name='home'),
    path('tasks', views.tasks, name='tasks'),
    path('task/<int:task_id>/done/', views.mark_done, name='mark_done'),
    path('task/<int:task_id>/delete/', views.delete_task, name='delete_task'),   # ✅ DELETE
    path('task/<int:task_id>/edit/', views.edit_task, name='edit_task'), 
]
