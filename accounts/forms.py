from django import forms
from django.contrib.auth.forms import UserCreationForm



class UserRegisterationForm(UserCreationForm):
    '''
        UserCreationForm by default has only 3 fields (username, password1, password2).
        So i did override it to add 2 optional fields (first_name, last_name).
        Only works for the built-in User model.

    '''
    class Meta(UserCreationForm.Meta):
        fields = ('first_name', 'last_name', 'username')