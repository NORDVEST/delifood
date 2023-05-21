# Generated by Django 4.2 on 2023-05-09 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='profile',
            name='last',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Фамилия'),
        ),
    ]
