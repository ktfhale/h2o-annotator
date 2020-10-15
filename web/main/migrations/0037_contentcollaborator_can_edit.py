# Generated by Django 2.2.9 on 2020-02-11 13:25

from django.db import migrations, models

def root_users_to_collaborators(app, schema):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_contentnode_provenance'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentcollaborator',
            name='can_edit',
            field=models.BooleanField(default=True),
        ),
        migrations.RemoveField(
            model_name='contentcollaborator',
            name='role',
        ),
        migrations.RunPython(root_users_to_collaborators, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='contentcollaborator',
            name='can_edit',
            field=models.BooleanField(default=False),
        ),
    ]
