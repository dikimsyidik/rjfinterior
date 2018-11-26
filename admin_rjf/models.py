from django.db import models
# Create your models here.
import os
from django.dispatch import receiver

 
KATEGORI_PRODUK = [
        ('backdrop', 'Back Drop'),
        ('bedroom', 'Bedroom'),
        ('meja_meeting', 'Meja Meeting'),
        ('front_office', 'Front Office'),
		('rak', 'Rak'),
		('tangga','Tangga'),

    ]


def path_and_rename(instance, filename):
    return (str(instance)+".jpg")


class Gallery_Foto(models.Model):
	"""docstring for Produk"""
		

	produk = models.CharField(max_length=200)
	post_thumbnail  = models.ImageField(default='default.jpg', upload_to=path_and_rename)
	kategori = models.CharField(max_length=200,choices=KATEGORI_PRODUK)
	


	def __str__(self):
		return self.produk
class Produk_Unggulan(models.Model):
	foto = models.ImageField(default='default.jpg', upload_to=path_and_rename)
	

	judul =  models.CharField(max_length=100)

	deskripsi = models.TextField()
	def __str__(self):
		return self.judul


class Testimoni(models.Model):
	"""docstring for Testimonial"""
	

	nama = models.CharField(max_length=100)

	project_dan_asal = models.CharField(max_length=100)


	komentar = models.TextField()

	def __str__(self):
		return self.nama

class Kontak(models.Model):


	alamat = models.CharField(max_length=100)

	no_hp = models.CharField(max_length=100)

	email = models.EmailField(max_length=100)


	facebook = models.URLField()
	twitter = models.URLField()
	instagram =  models.URLField()
	google_plus =  models.URLField()
	


