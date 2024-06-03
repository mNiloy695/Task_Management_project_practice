from .models import Task_model
from django import forms
class Task_Form(forms.ModelForm):
    class Meta:
        model=Task_model
        fields='__all__'
        # exclude=['is_completed',]
