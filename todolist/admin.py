from django.contrib import admin
from .models import TodoItem, Post

admin.site.register(TodoItem)
admin.site.register(Post)

