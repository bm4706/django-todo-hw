from django.http import HttpResponse
from django.shortcuts import redirect, render
from user.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


@csrf_exempt
def signup(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        User.objects.create_user(username=username, password=password)
        
        return redirect("/todo/")
    elif request.method == "GET":
        return render(request, "user/signup.html")
    else:
        return HttpResponse("타당하지않은", status=405)


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password) # 아이디가 없으면 none값을 리턴
        if user is not None:
            auth_login(request, user)
            # return redirect("/user/loginok/")
            return redirect("/todo/")
        else:
            return HttpResponse("타당하지않은", status=401)
    elif request.method == "GET":
        return render(request, "user/login.html")
    else:
        return HttpResponse("타당하지않은", status=405)    

def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return redirect("/todo/")
    else:
        return HttpResponse("타당하지않은", status=401)


    
# def loginok(request):
#     auth_logout(request)
#     # m ="로그인 성공!"
#     return HttpResponse(request.user)
#     # return HttpResponse(m) # 로그인 성공이라는걸 만들어보고싶어서 넣은 기능