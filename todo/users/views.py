from django.shortcuts import render , redirect
from .models import CustomUser
from django.contrib.auth import login , logout , authenticate
from .forms import RegisterationForm, UserLoginForm
# Create your views here.

def registration(request):
    if request.POST:
        form = RegisterationForm(request.POST)
        if form.is_valid():
            user=form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email , password = raw_password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            context={'form':form}
    else:
        form = RegisterationForm()
    context={'form':form}
    return render(request , 'register.html' , context)


def user_logout(request):
    logout(request)
    return redirect('home')
    
    
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request , user)
                return redirect('home')
    else:
        form = UserLoginForm()
    context = {"form" : form}
    return render(request , 'login.html' , context )

def base(request):
    users = CustomUser.objects.all()
    context={"users" :users}
    return render(request , 'base.html' , context)