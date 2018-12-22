from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

class TodoItem(models.Model):
    content = models.TextField()
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete="models.CASCADE")
    
class MyView(LoginRequiredMixin, TodoItem):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'