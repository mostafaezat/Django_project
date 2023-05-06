from django.shortcuts import redirect, render

from .forms import TodoForm , ItemTodoForm
from .models import Todo , TodoItem
from django.contrib.auth.decorators import login_required

from users.models import CustomUser


# Create your views here.
@login_required(login_url="login")
def home(request):
    if request.user:
        todos = Todo.objects.filter( user = request.user)
        todos = todos.order_by("date_created")
    else:
        return redirect("login")
    context = {"user": request.user, "todos": todos}
    return render(request, "home.html", context)

@login_required(login_url="login")
def create_todo(request):
    user = request.user
    form = TodoForm()
    if request.method =="POST":
        form = TodoForm(request.POST)
        if form.is_valid:
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('home')
    else:
        context= {'form':form}
    context= {'form':form}
    return render(request , 'create_todo.html' , context)




@login_required(login_url="login")
def create_item_todo(request , id):
    todo = Todo.objects.get(id=id)
    form = ItemTodoForm(request.POST)
    if request.method =="POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        date_created = request.POST.get("date_created")
        item = TodoItem.objects.create(todo = todo , description=description , title=title , date_created=date_created)
        item.save()
        return redirect('home')
    else:
        context= {'form':form}
    context= {'form':form}
    return render(request , 'create_item_todo.html' , context)


def updatetodo(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(instance=todo)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {
        "form": form,
    }
    return render(request, "updatetodo.html", context)

@login_required
def detailed(request, id):
    Todoitem = TodoItem.objects.get(id=id)
    context = {"Todoitem": Todoitem}
    return render(request, "detailed.html", context)


def deletetodo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect("home")


def completed(request, id):
    todoitem = TodoItem.objects.get(id=id)
    todoitem.is_completed = True
    todoitem.save()
    return redirect("home")

