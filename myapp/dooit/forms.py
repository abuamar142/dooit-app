from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from . models import Transaksi, Kategori, Saldo


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={'placeholder':'Enter your username', 'class': 'text-input'}))
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'placeholder':'Insert password', 'class': 'text-input'}))

    class Meta:
        model = User
        fields = ('username', 'password')

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='first_name',widget=forms.TextInput(attrs={'placeholder':'Enter your first name', 'class': 'text-input'}))
    last_name = forms.CharField(label='last_name',widget=forms.TextInput(attrs={'placeholder':'Enter your last name', 'class': 'text-input'}))
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={'placeholder':'Enter your username', 'class': 'text-input'}))
    email = forms.EmailField(label='email',widget=forms.EmailInput(attrs={'placeholder':'Enter your email', 'class': 'text-input'}))
    password1 = forms.CharField(label='password1',widget=forms.PasswordInput(attrs={'placeholder':'Insert password', 'class': 'text-input'}))
    password2 = forms.CharField(label='password2',widget=forms.PasswordInput(attrs={'placeholder':'Insert password again', 'class': 'text-input'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class TransaksiForm(forms.ModelForm):
    JENIS_TRANSAKSI_CHOICES = (
        ('pemasukan', 'Pemasukan'),
        ('pengeluaran', 'Pengeluaran'),
    )

    tanggal_transaksi = forms.DateInput(attrs={'class': 'datepicker'})
    jenis_transaksi = forms.ChoiceField(choices= JENIS_TRANSAKSI_CHOICES)
    kategori = forms.ChoiceField()
    deskripsi = forms.Textarea(attrs={'rows': 3})
    nominal = forms.IntegerField()

    class Meta:
        model = Transaksi
        fields = ['tanggal_transaksi', 'jenis_transaksi', 'kategori', 'deskripsi', 'nominal']

class KategoriForm(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ('nama_kategori', 'keterangan')
        widgets = {
            'keterangan': forms.Textarea(attrs={'rows': 3}),
        }

class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(label='first_name',widget=forms.TextInput(attrs={'placeholder':'Enter your first name', 'class': 'text-input form-control'}))
    last_name = forms.CharField(label='last_name',widget=forms.TextInput(attrs={'placeholder':'Enter your last name', 'class': 'text-input form-control'}))
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={'placeholder':'Enter your username', 'class': 'text-input form-control'}))
    email = forms.EmailField(label='email',widget=forms.EmailInput(attrs={'placeholder':'Insert email', 'class': 'text-input form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')