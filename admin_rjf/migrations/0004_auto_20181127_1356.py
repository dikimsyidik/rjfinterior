# Generated by Django 2.1.2 on 2018-11-27 06:56

import admin_rjf.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_rjf', '0003_auto_20181124_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_perusahaan', models.ImageField(default='default.jpg', upload_to=admin_rjf.models.path_and_rename)),
                ('deskripsi_perusahaan', models.TextField()),
                ('foto1', models.ImageField(default='default.jpg', upload_to=admin_rjf.models.path_and_rename)),
                ('nama_produk', models.CharField(max_length=100)),
                ('deskripsi_produk', models.TextField()),
                ('foto2', models.ImageField(default='default.jpg', upload_to=admin_rjf.models.path_and_rename)),
                ('nama_produk2', models.CharField(max_length=100)),
                ('deskripsi_produk2', models.TextField()),
                ('foto3', models.ImageField(default='default.jpg', upload_to=admin_rjf.models.path_and_rename)),
                ('nama_produk3', models.CharField(max_length=100)),
                ('deskripsi_produk3', models.TextField()),
                ('nama_dan_pekerjaan', models.CharField(max_length=100)),
                ('project_dan_asal', models.CharField(max_length=100)),
                ('komentar', models.TextField()),
                ('alamat', models.CharField(max_length=100)),
                ('no_hp', models.CharField(max_length=100)),
                ('whatsapp', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
                ('instagram', models.URLField()),
                ('google_plus', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='Kontak',
        ),
        migrations.DeleteModel(
            name='Produk_Unggulan',
        ),
        migrations.DeleteModel(
            name='Testimoni',
        ),
    ]