from django.conf import settings
from django.db import models
from django.utils import timezone


class TodoItem(models.Model):
    content = models.TextField()
