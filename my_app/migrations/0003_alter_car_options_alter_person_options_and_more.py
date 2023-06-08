# Generated by Django 4.2.2 on 2023-06-08 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_car'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Машина', 'verbose_name_plural': 'Машины'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Человек', 'verbose_name_plural': 'Люди'},
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(max_length=30, verbose_name='Марка'),
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(max_length=30, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=30, verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='car',
            name='power',
            field=models.IntegerField(verbose_name='Мощнощность (л\\с)'),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(verbose_name='Год выпуска'),
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.CharField(max_length=100, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='person',
            name='is_activated',
            field=models.BooleanField(verbose_name='Активнация'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
    ]