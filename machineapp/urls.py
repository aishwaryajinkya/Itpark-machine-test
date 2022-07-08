"""machineTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from . import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.index),
    path('POST/client',v.addClient.as_view()),
    path('GET/client',v.listClient.as_view()),
    path('PUT-PATCH/client/:<int:pk>',v.editClient.as_view()),
    path('DELETE/clients/:<int:pk>',v.deleteClient.as_view()),
    path('GET-POST/projects',v.createListProject.as_view()),
    path('editDeleteProject/:<int:pk>',v.editDeleteProject.as_view()),
    path('listProject/:<int:id>',v.getProject),
]
