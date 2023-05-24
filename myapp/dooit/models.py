from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Pengguna(models.Model):
    id_pengguna = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    nama = models.CharField(max_length=255)
    saldo = models.IntegerField(default=0)

    class Meta:
        ordering = ('id_pengguna',)

    def __str__(self):
        return self.nama

class Kategori(models.Model):
    id_kategori = models.AutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=255)
    keterangan = models.TextField()

    class Meta:
        ordering = ('id_kategori',)

    def __str__(self):
        return self.nama_kategori

class Transaksi(models.Model):
    JENIS_TRANSAKSI_CHOICES = [
        ('pemasukan', 'Pemasukan'),
        ('pengeluaran', 'Pengeluaran'),
    ]

    id_transaksi = models.AutoField(primary_key=True)
    pengguna = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    tanggal_transaksi = models.DateField()
    jenis_transaksi = models.CharField(max_length=255, choices=JENIS_TRANSAKSI_CHOICES)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    deskripsi = models.TextField(blank=True)
    nominal = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('tanggal_transaksi',)

    def __str__(self):
        return self.deskripsi