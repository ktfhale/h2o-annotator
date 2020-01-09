# Generated by Django 2.2.9 on 2020-01-08 20:00

from django.db import migrations

from urllib.parse import urlparse


def name_all_link_resources(apps, schema_editor):
    Resource = apps.get_model('main', 'Resource')
    Link = apps.get_model('main', 'Link')
    resources = Resource.objects.filter(resource_type='Link', title__isnull=True)
    links = {link.id: link for link in Link.objects.filter(id__in=[resource.resource_id for resource in resources])}
    for resource in resources:
        link = links[resource.resource_id]
        resource.title = link.name if link.name else "Link to {}".format(urlparse(link.url).netloc)
        resource.save()

def name_all_case_resources(apps, schema_editor):
    Resource = apps.get_model('main', 'Resource')
    Case = apps.get_model('main', 'Case')
    resources = Resource.objects.filter(resource_type='Case', title__isnull=True)
    cases = {case.id: case for case in Case.objects.filter(id__in=[resource.resource_id for resource in resources])}
    for resource in resources:
        case = cases[resource.resource_id]
        resource.title = case.name_abbreviation if case.name_abbreviation else case.name
        resource.save()

def name_all_text_resources(apps, schema_editor):
    Resource = apps.get_model('main', 'Resource')
    TextBlock = apps.get_model('main', 'TextBlock')
    resources = Resource.objects.filter(resource_type='TextBlock', title__isnull=True)
    texts = {text.id: text for text in TextBlock.objects.filter(id__in=[resource.resource_id for resource in resources])}
    for resource in resources:
        text = texts[resource.resource_id]
        resource.title = text.name
        resource.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20200108_1740'),
    ]

    operations = [
        migrations.RunPython(name_all_link_resources, migrations.RunPython.noop),
        migrations.RunPython(name_all_case_resources, migrations.RunPython.noop),
        migrations.RunPython(name_all_text_resources, migrations.RunPython.noop),
    ]
