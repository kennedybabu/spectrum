from django.forms import ModelForm
from.models import Interest, User, Post, Comment
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class InterestForm(ModelForm):
    class Meta:
        model = Interest
        fields = '__all__'
        exclude = ['host', 'members', ]


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name','username','email','profile_pic','bio']

