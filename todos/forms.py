from django import forms
from .models import Todo


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description')


class TodoUpdateForm(TodoCreateForm):
    class Meta(TodoCreateForm.Meta):
        fields = ('title', 'description', 'done')