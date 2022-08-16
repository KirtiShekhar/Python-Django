from django.db import models

# Create your models here.
class ToDoTaskModel(models.Model):
    todotask = models.CharField(max_length = 75)