# Generated by Django 2.2.20 on 2021-09-27 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20210924_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.Flat', verbose_name='Квартира, на которую пожаловались'),
        ),
    ]
