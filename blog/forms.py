from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm
from blog.models import Post2, Topic, PostBase
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class CommentForm(forms.Form):
    comment = forms.CharField(max_length=1000, widget=forms.Textarea)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post2
        fields = ['title', 'image', 'category', 'content']
    category = forms.TypedChoiceField(choices=PostBase.CATEGORY_CHOICES, coerce=str)


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'category', 'description']
    category = forms.TypedChoiceField(choices=PostBase.CATEGORY_CHOICES, coerce=str)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']