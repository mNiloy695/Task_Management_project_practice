from django.db import models
from category.models import Category
# Create your models here.
class Task_model(models.Model):
   taskTitle =models.CharField(max_length=200)
   taskDescription =models.CharField(max_length=700)
   is_completed=models.BooleanField(default=False)
   task_assign_date=models.DateField(auto_now_add=True)
   category=models.ManyToManyField(Category)
   def __str__(self) -> str:
        return self.taskTitle
