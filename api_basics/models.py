from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tasks(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    Task_Name = models.CharField(max_length=20, default='')
    Task_Text = models.TextField(max_length=450, default='')
    Task_Done = models.BooleanField(default=False)


    def __str__(self):
        return self.Task_Name
    