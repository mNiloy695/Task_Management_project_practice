from django.shortcuts import render,redirect
from .forms import CategoryForm
def add_category(request):
    if request.method=='POST':
        add_category_form=CategoryForm(request.POST)
        if add_category_form.is_valid():
            add_category_form.save()
            return redirect('add_category')
    else:
        add_category_form=CategoryForm()
    return render(request,'category_form.html',{'form':add_category_form})
            