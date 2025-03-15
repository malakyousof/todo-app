from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
# class users(models.Model):
#     id_user= models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     email = models.EmailField()
#     password = models.CharField(max_length=30)