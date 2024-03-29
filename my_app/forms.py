from django import forms
from django.forms import ModelForm
from .models import *
import datetime
from f_project.settings import DATE_INPUT_FORMATS



def year_choices():
    return [(r,r) for r in range(1950, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year


# class CarForm(forms.Form):
#     brand = forms.CharField(max_length=50, label='Марка')
#     model = forms.CharField(max_length=50, label='Модель')
#     color = forms.CharField(max_length=30, label='Цвет', required=False)
#     power = forms.IntegerField(label='Мощность (л/с)', required=False, min_value=1, max_value=600)
#     year = forms.ChoiceField(label='Год выпуска', choices=year_choices, initial=current_year)

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'



class DriverForm(ModelForm):
    # name = forms.CharField(max_length=50, label='Имя водителя')
    # age = forms.IntegerField(label='Возраст', min_value=18, max_value=120)
    # city = forms.CharField(max_length=50, label='Город', required=False)
    birthday = forms.DateField(
        input_formats=DATE_INPUT_FORMATS,
        label='Дата рождения',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    class Meta:
        model = Driver
        fields = '__all__'
        exclude = ['age']

class ClientForm(forms.ModelForm):
    birthday = forms.DateField(
        input_formats=DATE_INPUT_FORMATS,
        label='Дата рождения',
        widget=forms.DateInput(attrs={'type': 'date'})
        )
    class Meta:
        model = Client
        exclude = ['age', 'created_at']




class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class EmployeeForm(forms.ModelForm):
    birthday = forms.DateField(input_formats=DATE_INPUT_FORMATS, label='Дата рождения', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Employee
        fields = '__all__'