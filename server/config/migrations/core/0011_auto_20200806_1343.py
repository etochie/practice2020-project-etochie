# Generated by Django 3.0.8 on 2020-08-06 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200730_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='cafe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='core.Cafe'),
        ),
    ]
