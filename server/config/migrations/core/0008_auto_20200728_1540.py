# Generated by Django 3.0.8 on 2020-07-28 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_dish_cafe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='ingredients',
            field=models.ManyToManyField(to='core.Ingredient', verbose_name='Ингредиенты блюда'),
        ),
    ]