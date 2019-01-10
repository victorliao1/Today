from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem, Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import RedirectView
from django.utils import timezone

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

@login_required
def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html',
        {"all_items": all_todo_items})

def addTodo(request):
    #create new todo all_items
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/')

def deleteTodo(request, todo_id):
    TodoItem.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')

def loginpage(request):
    return HttpResponseRedirect('/accounts/login/')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
