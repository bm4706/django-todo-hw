
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
# def create(request):
#     # print(request.POST) # post로 내가 원하는 값을 넣을수잇께함
#     Todo.objects.create(content=request.POST["content"])
#     return HttpResponse('create')

# def create_page(request):
#     return render(request, "todo/create.html")

# 하나로 합치기 위해
def create(request):
    if request.method == "POST":
        Todo.objects.create(content=request.POST["content"], user=request.user)
        return redirect("/todo/")
    elif request.method == "GET":
        return render(request, "todo/create.html")
    else:
        return HttpResponse("타당하지않은", status=405)
    
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
        todo.delete()
        return redirect("/todo/")
    else:
        return HttpResponse("타당하지않은", status=405)
    
@csrf_exempt 
def update(request, todo_id):
    if request.method == "POST":
        todo = Todo.objects.get(id=todo_id)
        todo.content = request.POST["content"]
        todo.save() # db에 저장해줘야함
        return redirect(f"/todo/{todo_id}/")
    elif request.method == "GET":
        todo = Todo.objects.get(id=todo_id)
        context = {
            "todo":todo,
        }
        return render(request, "todo/update.html",context)
    else:
        return HttpResponse("타당하지않은", status=405)