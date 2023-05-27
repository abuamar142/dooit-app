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
            pengguna = authenticate(request, username=username, password=password)
            if pengguna is not None:
                login(request, pengguna)
                request.session['pengguna_id'] = pengguna.id
                return redirect('dashboard')
    else:
        form = LoginForm()

    return render(request, 'login_pengguna.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('dashboard')
    else:
        form = RegisterForm()

    return render(request, 'register_pengguna.html', {'form': form})

@login_required
def dashboard_view(request):
    semua_pengguna = User.objects.all()
    print(request.session.get('pengguna.id'))
    context = {'daftar_pengguna': semua_pengguna}
    return render(request, 'dashboard_pengguna.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

def show_profile_view(request):
    data = request.session.get('pengguna_id')
    pengguna = User.objects.get(id=data) if data else None
    return render(request, 'show_profile.html', {'data_pengguna': pengguna})
