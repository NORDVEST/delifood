# Generated by Django 4.2 on 2023-05-05 22:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_post_cnt_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_deliver',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='time_deliver',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
