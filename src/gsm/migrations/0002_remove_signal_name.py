# Generated by Django 4.1.2 on 2022-10-19 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gsm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signal',
            name='name',
        ),
    ]
