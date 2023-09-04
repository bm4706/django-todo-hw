from django.http import HttpResponse
from django.shortcuts import redirect, render
from user.models import User
from django.views.decorators.csrf import csrf_exempt



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
