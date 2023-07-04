from django.db import models
from django.urls import reverse


# 1. Create your models here.
# 2. Createmigrations: python manage.py makemigrations
# 3. python manage.py migrate

# Create your models here.
class Driver(models.Model):
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


class Client(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    age = models.IntegerField(verbose_name='Возраст')
    city = models.CharField(max_length=30, verbose_name='Город')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Эл. почта')
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return ' '.join([self.name, self.last_name])

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'



class Employee(models.Model):
    edu_choises = [('middle', 'среднее'),
                   ('high', 'высшее'),
                   ('profesional', 'профессиональное'),
                   ]

    firstname = models.CharField(max_length=50, verbose_name='Имя')
    lastname = models.CharField(max_length=50, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    position = models.CharField(max_length=50, verbose_name='Должность')
    education = models.CharField(max_length=30, choices=edu_choises)

    def str(self):
        return ' '.join([str(self.firstname), str(self.lastname)])

    def get_absolute_url(self):
        return reverse('my_app:employee_list')

    # def get_absolute_url(self):
    #     return reverse("author-detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'