from django.urls import path
from .views import about, login, contacts, index_my_app, cars, drivers

urlpatterns = [
    path('', index_my_app, name='index'),     # Путь "корень"
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('cars/', cars, name='cars'),
    path('drivers/', drivers, name='drivers'),
    path('contacts/<str:id>/', contacts, name='contacts')  # перед слешем долно быть цыфровое значение
]
