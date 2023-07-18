import phone_field
from django.db import models
from django.urls import reverse
from datetime import date
from phone_field import PhoneField

# 1. Create your models here.
# 2. Createmigrations: python manage.py makemigrations
# 3. python manage.py migrate

# Create your models here.
class Driver(models.Model):
    #id = models.AutoField(unique=True, primary_key=True) - Это поле есть по дефолту. Его можно поменять под себя.
    first_name = models.CharField(max_length=100, verbose_name='Имя', default=None)  ## Везде нужно ограничивать длину
    last_name = models.CharField(max_length=100, verbose_name='Имя', default='')
    birthday = models.DateField(verbose_name='Дата рождения', default=date.today)
    age = models.IntegerField(verbose_name='Возраст', null=True)
    city = models.CharField(max_length=100, verbose_name='Город', null=True)
    passport = models.CharField(max_length=15, verbose_name='Паспорт', unique=True, null=False, default=None)
    email = models.EmailField(verbose_name='Эл. почта', unique=True)
    is_activated = models.BooleanField(verbose_name='Активация', default=True)


    def __str__(self):  # Приватный метод который возвращает имя строчки
        return f'{self.first_name} {self.last_name} - {self.city}'
        # return ' '.join([str(self.first_name), str(self.last_name)])

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'
        ordering = ['last_name', '-birthday']  ## "-" Обратная сортировка
        unique_together = (
            ('first_name', 'last_name', 'passport')
        )



class CarBrand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):  ## Строковое представление объекта
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Car(models.Model):

    colors = (
        ('черный', 'черный'),
        ('желтый' , 'желтый'),
        ('белый', 'белый'),
        ('синий', 'синий'),
        ('зеленый', 'зеленый'),
        ('красный', 'красный'),
    )
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='cars', verbose_name='Марка')
    model = models.CharField(max_length=30, verbose_name='Модель')
    color = models.CharField(max_length=30,choices=colors, verbose_name='Цвет')
    power = models.IntegerField(verbose_name='Мощнощность (л\с)')
    year = models.IntegerField(verbose_name='Год выпуска')
    image = models.ImageField(upload_to='cars/', blank=True, null=True)

    #
    def __str__(self):  # Приватный метод который возвращает имя строчки
        return f'{self.brand} {self.model}'
        # return ' '.join([str(self.brand), str(self.model)])

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
        ordering = ['-year', 'model']  ## По дефолту "по возрастанию", Если поставить "-", то по убыванию.


class Client(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    age = models.IntegerField(verbose_name='Возраст', null=True)
    city = models.CharField(max_length=30, verbose_name='Город')
    phone = phone_field.PhoneField(blank=True, help_text='Ваш номер телефона', verbose_name='Телефон', unique=True)
    email = models.EmailField(verbose_name='Эл. почта', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ' '.join([self.name, self.last_name])

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['last_name']
        unique_together = (
            ('name', 'last_name', 'email')
        )



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


class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING, related_name='cars', verbose_name='Марка')
    driver = models.ForeignKey(Driver, on_delete=models.DO_NOTHING, related_name='driver', verbose_name='Водитель')
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, related_name='client', verbose_name='Клиент')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ' '.join([str(self.id), str(self.client)])

    def get_absolute_url(self):
        return reverse('my_app:order_list')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


