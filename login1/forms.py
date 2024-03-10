from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms



class Registration(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'abc'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'abc'}))

   # password1=forms.CharField(label1="passw1")
   # password2=forms.CharField(label2="passw2")

    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        widgets={
            'username':forms.TextInput(attrs={'class':'abc'}),
            'first_name':forms.TextInput(attrs={'class':'abc'}),
            'last_name':forms.TextInput(attrs={'class':'abc'}),
            'email':forms.TextInput(attrs={'class':'abc'})
              }

class LoginForm(AuthenticationForm):
    pass


