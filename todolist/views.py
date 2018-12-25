from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@login_required
def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html',
        {"all_items": all_todo_items})

# @login_required
# def todoView(request):
#     all_todo_items = TodoItem.objects.filter(user=request.user).order_by('-date_added')
# #     all_todo_items = TodoItem.objects.all()
#     return render(request, 'todo.html',
#         {"all_items": all_todo_items})

def addTodo(request):
    #create new todo all_items
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/')

# def addTodo(request):
#     #create new todo all_items
#     user = request.user
#     new_item = TodoItem(content = request.POST['content'])
#     gta = user.TodoItem.create(content = new_item)
#     return render(request, 'todo.html', {'form' : form})

def deleteTodo(request, todo_id):
    TodoItem.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')