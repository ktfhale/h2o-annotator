# Generated by Django 2.2.9 on 2019-12-19 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20191219_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='default',
            name='user',
        ),
        migrations.RemoveField(
            model_name='textblock',
            name='user',
        ),
    ]
