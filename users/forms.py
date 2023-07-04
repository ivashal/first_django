from django.contrib.auth.models import User
from django import forms  ## Для переопределения полей в формах

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        help_text = {
            'username': 'Только буквы, цыфры и символы @/./+/-/_',
        }

        verbose_name = {
            'username': 'login',
        }

    def clean_password2(self):  ## Важно чтобы начиналось со слова clean_<имя поля>
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!')  ## raise в "ручном" режиме генерирует исключение
        return cd['password2']

