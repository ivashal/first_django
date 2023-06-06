from django.urls import path
from .views import about, login, contacts, index_my_app

urlpatterns = [
    path('', index_my_app),     # Путь "корень"
    path('about/', about),
    path('login/', login),
    path('contacts/<str:id>/', contacts)  # перед слешем долно быть цыфровое значение
]
