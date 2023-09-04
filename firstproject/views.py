from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

def pingpong(request):
    # print(request.header)
    # return HttpResponse('pong')
    
    # templates폴더에 html만들어주고 setting.py에도 설정 'DIRS': [BASE_DIR/'firstproject'/'templates'] 바꿔주면 새로운걸로 써야함
    return render(request, 'pong.html')


def index(request):
    # print(request.GET.get('q')) #
    # print(request.GET.get('a'))
    name = request.GET.get('name')
    # return HttpResponse(f'<h1>index</h1> <p>안녕하세요 {name}님</p>')
    return render(request, 'index.html')

def getdata(request):
    print(request.POST.get('todo'))
    print(request.POST.get('todo2'))
    print(request.POST.get('todo3'))
    
    return HttpResponse('ok')