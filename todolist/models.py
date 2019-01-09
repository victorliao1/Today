from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.mixins import LoginRequiredMixin

#todo list models
class TodoItem(models.Model):
    content = models.TextField()
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete="models.CASCADE")

class MyView(LoginRequiredMixin, TodoItem):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

#blog models
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
 
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
