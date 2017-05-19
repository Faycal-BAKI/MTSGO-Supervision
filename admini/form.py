from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

class SpotForm(forms.Form):
    centrex=forms.IntegerField()
    centrey=forms.IntegerField()
    centrez=forms.IntegerField()
    rayon=forms.IntegerField()
    currentQuestion=forms.IntegerField()
    questionList=forms.CharField()
    #startTime
    delay=forms.IntegerField()
