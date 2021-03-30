from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class UserRegisterForm(UserCreationForm):#subclase 
    email = forms.EmailField()
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirma contraseña', widget=forms.PasswordInput)

    class meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:""for k in fields}

class PostForm(forms.ModelForm):
    content = forms.CharField(label='',widget=forms.Textarea(attrs={'rows':2, 'placeholder':'¿Que esta pasando?'}), required=True)

    class Meta:
        model = Post
        fields = ['content']

    

