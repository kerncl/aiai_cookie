from django.urls import resolve, reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group, Permission
from .forms import RegisterForm


# Create your views here.
def loginpage(request):
    if request.method == 'POST':
        next = request.GET.get('next')
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            if next:
                # redirect back to previous url
                return resolve(next).func(request)
            return redirect('shop:homepage')
        messages.error(request, 'Invalid Username/Password')
    return render(request, 'account/registration/login.html', {'loginform': RegisterForm()})


def logoutpage(request):
    logout(request)
    return redirect('shop:homepage')


def registerpage(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        username = request.POST.get('username')
        try:
            User.objects.get(username=username)
            messages.error(request, 'Username already exists. Please use other username')
            return render(request, 'account/registration/register.html', {'form': form})
        except User.DoesNotExist:
            # User Doest not exist
            user = User.objects.create_user(username=username, password=request.POST.get('password'))

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('account:login')
            # return redirect('shop:homepage')
    else:
        form = RegisterForm()
    return render(request, 'account/registration/register.html', {'form': form})


@login_required(login_url=reverse_lazy('account:login'))
def profilepage(request):
    UserModel = get_user_model()
    user = UserModel.objects.get(username=request.user.username)
    return render(request, 'account/profile.html', {'user': user})


def login_firebase(request):
    return render(request, 'account/registration/login_auth.html')

def register_auth(request):
    return render(request, 'account/registration/register_auth.html')

