from django import forms
from .models import Todo ,TodoItem
class DateInput(forms.DateInput):
    input_type = 'date'
    
    
class TodoForm(forms.ModelForm):
    date_created = forms.DateField()
    class Meta:
        model = Todo
        fields = (
            "title",
            "date_created",
        )
        widgets = {
            "date_created": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    "type": "date",
                    "placeholder": "yyyy-mm-dd (DOB)",
                    "class": "form-control",
                },
            ),
        }
        

class ItemTodoForm(forms.ModelForm):
    date_created = forms.DateField()
    class Meta:
        model = TodoItem
        fields = '__all__'
        exclude = ["todo" , "is_completed"]

        widgets = {
            "date_created": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    "type": "date",
                    "placeholder": "yyyy-mm-dd (DOB)",
                    "class": "form-control",
                },
            ),
        }
