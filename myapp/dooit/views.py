from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from dooit.models import User

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()

    return render(request, 'login_pengguna.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request, data=request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = [first_name, last_name, username, password]
            if user is not None:
                return redirect('dashboard')
    else:
        form = RegisterForm()

    return render(request, 'register_pengguna.html', {'form': form})

@login_required
def dashboard_view(request):
    semua_pengguna = User.objects.all()
    context = {'daftar_pengguna': semua_pengguna}
    return render(request, 'dashboard_pengguna.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')
