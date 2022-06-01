from django import forms  
from .models import Exam
class QuestionForm(forms.ModelForm):  
    class Meta:  
        model = Exam  
        fields = "__all__" 