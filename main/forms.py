from django.forms import ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    class Meta:

#     class Meta:
#         model = User
#         fields = ['avatar', 'name', 'username', 'email', 'bio']        model = User
        fields = ['first_name', 'second_name', 'username', 'email', 'password1', 'password2']


# class UserForm(ModelForm):
