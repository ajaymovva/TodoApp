from django.db import models
import datetime


# Create your models here.
class Todo_info(models.Model):
    task_title = models.CharField(max_length=128)
    task_info = models.TextField()
    actual_date = models.DateTimeField()
    status = models.CharField(max_length=128)

    def __str__(self):
        return self.task_title
