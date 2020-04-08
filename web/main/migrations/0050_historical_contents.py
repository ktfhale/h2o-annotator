# Generated by Django 2.2.10 on 2020-04-07 12:20

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0049_deref_old_casebooks'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalTextBlock',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=5242880, null=True)),
                ('content', models.CharField(max_length=5242880)),
                ('public', models.BooleanField(blank=True, default=True, null=True)),
                ('created_via_import', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical text block',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalLink',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('name', models.CharField(blank=True, max_length=1024, null=True)),
                ('description', models.CharField(blank=True, max_length=5242880, null=True)),
                ('url', models.URLField(max_length=1024)),
                ('public', models.BooleanField(default=True, null=True)),
                ('content_type', models.CharField(blank=True, max_length=255, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical link',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalContentNode',
            fields=[
                ('id', models.BigIntegerField(blank=True, db_index=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('ordinals', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=None)),
                ('provenance', django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(), default=list, size=None)),
                ('title', models.CharField(default='Untitled', max_length=10000)),
                ('subtitle', models.CharField(blank=True, max_length=10000, null=True)),
                ('headnote', models.TextField(blank=True, null=True)),
                ('raw_headnote', models.TextField(blank=True, null=True)),
                ('public', models.BooleanField(default=False)),
                ('draft_mode_of_published_casebook', models.BooleanField(blank=True, help_text='Unknown (None) or True; never False', null=True)),
                ('resource_type', models.CharField(blank=True, max_length=255, null=True)),
                ('resource_id', models.BigIntegerField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('casebook', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='main.ContentNode')),
                ('copy_of', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='main.ContentNode')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('new_casebook', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='main.Casebook')),
            ],
            options={
                'verbose_name': 'historical content node',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalContentAnnotation',
            fields=[
                ('id', models.BigIntegerField(blank=True, db_index=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('kind', models.CharField(choices=[('replace', 'replace'), ('highlight', 'highlight'), ('elide', 'elide'), ('note', 'note'), ('link', 'link')], max_length=255)),
                ('content', models.TextField(blank=True, null=True)),
                ('global_start_offset', models.IntegerField(blank=True, null=True)),
                ('global_end_offset', models.IntegerField(blank=True, null=True)),
                ('start_paragraph', models.IntegerField(blank=True, null=True)),
                ('end_paragraph', models.IntegerField(blank=True, null=True)),
                ('start_offset', models.IntegerField(blank=True, null=True)),
                ('end_offset', models.IntegerField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('resource', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='main.Resource')),
            ],
            options={
                'verbose_name': 'historical content annotation',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
