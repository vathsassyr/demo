# Generated by Django 5.1.6 on 2025-03-11 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codecamp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]
