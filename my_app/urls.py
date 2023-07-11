from django.urls import path
from .views import *

app_name = 'my_app'

urlpatterns = [
    path('', index_my_app, name='index'),     # Путь "корень"
    path('about/', about, name='about'),
    path('contacts/<str:id>/', contacts, name='contacts'),  # перед слешем долно быть цыфровое значение

    path('cars/<int:pk>/', car_detail, name='car_detail'),
    path('cars/', cars, name='cars'),

    path('drivers/<int:pk>/', driver_card, name='driver_card'),
    path('drivers/', drivers, name='drivers'),

    path('clients/<int:pk>/', client_card, name='client_card'),
    path('clients/', clients, name='clients'),

    path('add_car/', add_car, name='add_car'),
    path('add_driver/', add_driver, name='add_driver'),
    path('add_client/', add_client, name='add_client'),

    path('employees/<int:pk>/update/', EmployeeUpdate.as_view(), name='employee-update'),
    path('employees/<int:pk>/delete/', EmployeeDelete.as_view(), name='employee-delete'),
    path('employees/', EmployeeList.as_view(), name='employee_list'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
    path('employee_form/', EmployeeCreate.as_view(), name='employee-form'),

    path('orders/', OrderList.as_view(), name='order_list'),
    path('order_form/', OrderCreate.as_view(), name='order-form'),

    # path('cars/search/', car_search, name='car-search'),

]
