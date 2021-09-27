# Generated by Django 2.2.20 on 2021-09-27 09:05

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20210927_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('owners_phonenumber', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('owner_pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Нормализованный номер владельца')),
                ('flat', models.ManyToManyField(related_name='flats', to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]
