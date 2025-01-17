# Generated by Django 2.2.20 on 2021-09-27 09:52

from django.db import migrations


def copy_owners_to_owner(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(owner=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            owner_pure_phone=flat.owner_pure_phone)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_owner'),
    ]

    operations = [
        migrations.RunPython(copy_owners_to_owner),
    ]
