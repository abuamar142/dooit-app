from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
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


def dashboard_view(request):
    semua_pengguna = User.objects.all()
    context = {'daftar_pengguna': semua_pengguna}
    return render(request, 'dashboard_pengguna.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')
