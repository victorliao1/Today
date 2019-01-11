from django.urls import path
from todolist.views import todoView, addTodo, deleteTodo, loginpage, favicon_view, post_list, post_detail, post_new, post_edit
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('blog/', post_list),
    path('blog/post/<int:pk>/', views.post_detail, name='post_detail'),
    path('blog/post/new/', views.post_new, name='post_new'),
    path('blog/post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
