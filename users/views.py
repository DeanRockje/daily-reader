from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
# Create your views here.



def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        if form.is_valid:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect('/category/')
                else:
                    return HttpResponseRedirect('Account disabled')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'users/authentication.html', {'form':form})


def RegisterNewUser(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if form.is_valid:
            user = User.objects.create_user(username=username, password=password, email=email)
            return HttpResponseRedirect('/users/login/')
        else:
            return HttpResponse('Invalid login or password')
    else:
        form = RegisterForm()
    return render(request,'users/registration.html', {'form':form})


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/users/')