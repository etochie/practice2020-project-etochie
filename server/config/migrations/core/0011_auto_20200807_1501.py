# Generated by Django 3.0.8 on 2020-08-07 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0010_auto_20200730_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cafes', to=settings.AUTH_USER_MODEL, verbose_name='Владелец заведения'),
        ),
    ]
