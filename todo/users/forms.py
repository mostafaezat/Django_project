from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth import authenticate

class RegisterationForm(UserCreationForm):
    email = forms.EmailField(max_length=60 , help_text='Required . add a valid email address')
    
    class Meta:
        model = CustomUser
        fields = ('email' , 'user_name' , 'password1', 'password2')
        
class UserLoginForm(forms.ModelForm):
    password = forms.CharField(label='password' , widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ('email' , 'password')
    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email , password = password):
            raise forms.ValidationError('Invalid login')