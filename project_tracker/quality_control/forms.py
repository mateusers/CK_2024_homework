from django import forms
from django.forms import ModelForm
from .models import BugReport, FeatureRequest
from tasks.models import Project, Task


# class FeedbackForm(forms.Form):
#     name = forms.CharField(label='Ваше имя', max_length=100)
#     email = forms.EmailField(label='Электронная почта')
#     message = forms.CharField(widget=forms.Textarea, label='Сообщение')


class BugReportForm(ModelForm):
    class Meta:
        model = BugReport
        fields = ['title', 'description', 'project', 'task', 'status', 'priority']
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'project': 'Название проекта',
            'task': 'Навзание задачи',
            'status': 'Статус',
            'priority': 'Приоритет'
        }


class FeatureRequestForm(ModelForm):
    class Meta:
        model = FeatureRequest
        fields = ['title', 'description', 'project', 'task', 'status', 'priority']
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'project': 'Название проекта',
            'task': 'Навзание задачи',
            'status': 'Статус',
            'priority': 'Приоритет'
        }

