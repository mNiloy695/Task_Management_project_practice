from django.shortcuts import render,redirect
from .forms import Task_Form
from .models import Task_model
# Create your views here.
def add_task(request):
    if request.method=='POST':
        add_task_form=Task_Form(request.POST)
        if add_task_form.is_valid():
            add_task_form.save()
            return redirect('add_task')
    else:
        add_task_form=Task_Form()
    return render(request,'task_form.html',{'form':add_task_form})
def edit_task(request,id):
    task_object=Task_model.objects.all().get(pk=id)
    add_task_form=Task_Form(instance=task_object)
    if request.method=='POST':
        add_task_form=Task_Form(request.POST,instance=task_object)
        if add_task_form.is_valid():
            add_task_form.save()
            return redirect('add_task')
    return render(request,'task_form.html',{'form':add_task_form})
def delete_task(request,id):
    task_object=Task_model.objects.all().get(pk=id).delete()
    return redirect('home_page')
