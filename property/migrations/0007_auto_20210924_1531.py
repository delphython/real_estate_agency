# Generated by Django 2.2.20 on 2021-09-24 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0006_flat_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='user',
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat', models.IntegerField(db_index=True, verbose_name='Квартира, на которую пожаловались')),
                ('compliant_text', models.TextField(db_index=True, verbose_name='Текст жалобы')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался')),
            ],
        ),
    ]
