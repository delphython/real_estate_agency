# Generated by Django 2.2.20 on 2021-09-27 08:19

import phonenumbers
from django.db import migrations


def set_normalized_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        for match in phonenumbers.PhoneNumberMatcher(flat.owners_phonenumber,
                                                     "RU"):
            flat.owner_pure_phone = phonenumbers.format_number(match.number,
                phonenumbers.PhoneNumberFormat.E164)
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(set_normalized_phonenumbers),
    ]
