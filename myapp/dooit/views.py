from .forms import LoginForm, RegisterForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from dooit.models import User, Kategori, Saldo


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            pengguna = authenticate(
                request, username=username, password=password)
            if pengguna is not None:
                login(request, pengguna)
                request.session['pengguna_id'] = pengguna.id
                return redirect('dashboard')
    else:
        form = LoginForm()

    quotes = [
        "'Tabungan adalah pondasi dari kebebasan finansial.' - T. Harv Eker",
        "'Menabung adalah kekuatan yang paling kuat di dunia.' - Albert Einstein",
        "'Menyimpan uang bukanlah tentang seberapa banyak yang Anda hasilkan, tetapi tentang seberapa banyak yang Anda simpan.' - Anonymous",
        "'Menabung adalah investasi terbaik yang bisa Anda lakukan pada masa depan Anda.' - Anonymous",
        "'Menyisihkan uang adalah bentuk penghormatan terhadap masa depan Anda.' - Dave Ramsey",
        "'Menabung adalah pintu menuju kebebasan finansial.' - Suze Orman",
        "'Jangan menabung sisa-sisa uang, tapi sisihkan uang untuk ditabung.' - Anonymous",
        "'Menabung adalah tanda kebijaksanaan dalam mengelola keuangan pribadi.' - Benjamin Franklin",
        "'Menabung adalah langkah awal untuk meraih impian finansial Anda.' - Dave Ramsey",
        "'Menabung bukanlah tentang seberapa banyak yang Anda hasilkan, tetapi tentang seberapa sedikit yang Anda habiskan.' - Robert Kiyosaki",
    ]

    context = {
        'form': form,
        'quotes': quotes,
    }

    return render(request, 'login_pengguna.html', context)


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data['username']
            pengguna = User.objects.get(username=username)

            Saldo.objects.get_or_create(pengguna=pengguna)

            if user is not None:
                return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register_pengguna.html', {'form': form})


@login_required
def dashboard_view(request):
    semua_pengguna = User.objects.all()
    id = request.session.get('pengguna_id')
    context = {
        'daftar_pengguna': semua_pengguna,
        'profile': User.objects.get(id=id),
        'saldo': Saldo.objects.get(pengguna=id)
    }
    return render(request, 'dashboard_pengguna.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def show_profile_view(request):
    data = request.session.get('pengguna_id')
    pengguna = User.objects.get(id=data) if data else None
    return render(request, 'show_profile.html', {'data_pengguna': pengguna})


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('show_profile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})


@login_required
def update_transaction():
    pass
