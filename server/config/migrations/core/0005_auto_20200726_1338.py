# Generated by Django 3.0.8 on 2020-07-26 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200724_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='photo',
            field=models.ImageField(blank=True, upload_to='cafe_photos', verbose_name='Фотография заведения'),
        ),
    ]
