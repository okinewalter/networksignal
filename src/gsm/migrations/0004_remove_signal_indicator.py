# Generated by Django 4.1.2 on 2022-11-23 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gsm', '0003_topsearch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signal',
            name='indicator',
        ),
    ]