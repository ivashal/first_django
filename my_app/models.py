from django.db import models


# 1. Create your models here.
# 2. Createmigrations: python manage.py makemigrations
# 3. python manage.py migrate

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    age = models.IntegerField(verbose_name='Возраст')
    city = models.CharField(max_length=100, verbose_name='Город')
    is_activated = models.BooleanField(verbose_name='Активнация')

    def __str__(self):  # Приватный метод который возвращает имя строчки
        return f'{self.name} {self.city}'
        # return ' '.join([str(self.brand), str(self.model)])

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'


class Car(models.Model):
    brand = models.CharField(max_length=30, verbose_name='Марка')
    model = models.CharField(max_length=30, verbose_name='Модель')
    color = models.CharField(max_length=30, verbose_name='Цвет')
    power = models.IntegerField(verbose_name='Мощнощность (л\с)')
    year = models.IntegerField(verbose_name='Год выпуска')

    def __str__(self):  # Приватный метод который возвращает имя строчки
        return f'{self.brand} {self.model}'
        # return ' '.join([str(self.brand), str(self.model)])

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
