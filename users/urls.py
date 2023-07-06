from django.urls import path
from .views import *

app_name = 'users'  ## Стандартная переменная, префикс для обращения к маршруту (префикс приложения)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
]