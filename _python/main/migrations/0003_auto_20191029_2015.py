# Generated by Django 2.2.6 on 2019-10-29 20:15

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191007_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentnode',
            name='headnote',
            field=main.models.SanitizingTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='default',
            name='url',
            field=models.URLField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='textblock',
            name='content',
            field=main.models.SanitizingCharField(max_length=5242880),
        ),
    ]
