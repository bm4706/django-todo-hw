"""
URL configuration for firstproject project.

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
from django.http import HttpResponse
from django.urls import path

from . import views
# def pingpong(request):
#     # print(request.header)
#     return HttpResponse('pong')

# def index(request):
#     # print(request.GET.get('q')) #
#     # print(request.GET.get('a'))
#     name = request.GET.get('name')
#     return HttpResponse(f'<h1>index</h1> <p>안녕하세요 {name}님</p>')






urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('loginok/', views.loginok),
]
