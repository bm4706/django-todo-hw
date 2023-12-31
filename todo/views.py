
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from todo.models import Todo

def index(request):
    if request.method =="GET":
        todos = Todo.objects.all() # read
        # print(todos)
        context = {
            "todos":todos
        }
        return render(request, "todo/index.html", context)
    else:
        return HttpResponse("타당하지않은", status=405)
# Create your views here.


# def create(request):
#     # print(request.POST) # post로 내가 원하는 값을 넣을수잇께함
#     Todo.objects.create(content=request.POST["content"])
#     return HttpResponse('create')

# def create_page(request):
#     return render(request, "todo/create.html")

# 하나로 합치기 위해

@login_required(login_url='/user/login/') # 이거는 아래 if구문 로그인여부에따라 글작성 여부를 한줄로 줄임
@csrf_exempt
def create(request):
    # if request.user.is_authenticated: # 로그인 되어있을때 글 작성 가능하게 하기
    if request.method == "POST":
        # 이미지 파일 추가  image=request.FILES.get("image")
        Todo.objects.create(content=request.POST["content"],
                            user=request.user, 
                            image=request.FILES.get("image"))
        return redirect("/todo/")
    elif request.method == "GET":
        return render(request, "todo/create.html")
    else:
        return HttpResponse("타당하지않은", status=405)
    # else: # 로그인 안한상태로 글 작성할려면 로그인 페이지로 넘겨주기
    #     return  redirect("/user/login/")
def read(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
            "todo":todo
        }
    return render(request, "todo/detail.html", context)

@csrf_exempt
def delete(request, todo_id):
    if request.method == "POST":
        todo = Todo.objects.get(id=todo_id)
        # 백엔드에서도 삭제하기 못하게 추가
        if request.user == todo.user:
            
            todo.delete()
            return redirect("/todo/")
        else:
            return HttpResponse("타당하지않은", status=405)
    else:
        return HttpResponse("타당하지않은", status=405)
    
@csrf_exempt 
def update(request, todo_id):
    if request.method == "POST":
        todo = Todo.objects.get(id=todo_id)
        # 백엔드에서 수정못하게 막기
        if request.user == todo.user:
            todo.content = request.POST["content"]
            todo.save() # db에 저장해줘야함
            return redirect(f"/todo/{todo_id}/")
        else:
            return HttpResponse("타당하지않은", status=405)
    elif request.method == "GET":
        todo = Todo.objects.get(id=todo_id)
        context = {
            "todo":todo,
        }
        return render(request, "todo/update.html",context)
    else:
        return HttpResponse("타당하지않은", status=405)