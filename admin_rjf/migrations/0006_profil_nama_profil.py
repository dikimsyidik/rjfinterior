# Generated by Django 2.1.2 on 2018-11-28 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_rjf', '0005_auto_20181127_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='nama_profil',
            field=models.CharField(default='profilnya', max_length=100),
        ),
    ]
