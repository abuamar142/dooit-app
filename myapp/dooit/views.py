from django.shortcuts import render
from dooit.models import Pengguna

def index(request):
    semua_pengguna = Pengguna.objects.all()
    context = {'daftar_pengguna': semua_pengguna}
    return render(request, 'index.html', context)

