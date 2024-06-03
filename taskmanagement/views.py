from django.shortcuts import render
from task.models import Task_model
def home(request):
    tasks=Task_model.objects.all()
    return render(request,'home.html',{'tasks':tasks})