from django.http import HttpResponse
from .forms import CarForm, DriverForm, ClientForm
from .models import Car, Client, Driver
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
# Create your views here.

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Машины парка", 'url_name': 'cars'},
    {'title': "Водители парка", 'url_name': 'drivers'},
    {'title': "Клиенты", 'url_name': 'clients'}
]


def index_main(request):
    return HttpResponse('<h1>Main page</h1>')  # Всегда веб-страничка долна возвращаться (результат ответа на запрос


def index_my_app(request):
    title = 'Моя главная страница'
    context = {'title': title, 'menu': menu}
    return render(request, 'my_app/index.html', context=context)


def about(request):
    title = 'О сайте'
    context = {'title': title, 'menu': menu}
    return render(request, 'my_app/about.html', context=context)


def cars(request):
    title = 'Машины'
    car = Car.objects.all()

    context = {'title': title, 'menu': menu}
    return render(request, 'my_app/cars.html', context=context)


def drivers(request):
    title = 'Водители'
    context = {'title': title, 'menu': menu}
    return render(request, 'my_app/drivers.html', context=context)


@csrf_protect
def login(request):
    title = 'Войти'
    context = {'title': title, 'menu': menu}

    if request.method == 'POST':
        username = request.POST.get('username')  # Получение данных из POST запроса
        password = request.POST.get('password')  # оно не связано с маршрутом
        return HttpResponse(f'Login - {username}, Password - {password}')

    if request.method == 'GET':
        return render(request, 'my_app/login.html', context=context)


def contacts(request, id):
    url_id = id
    name = request.GET.get('name')  # То, что мы передаем через ? &
    age = request.GET.get('age')
    # return HttpResponse(f'Page_contacts, id = {id}')
    get_params = {'mane': name, "age": age}
    return HttpResponse(f'Page contacts, url_parametr_id = {url_id}, get_params = {get_params}')


def clients(request):
    title = 'Клиенты'
    context = {'title': title, 'menu': menu}
    return render(request, 'my_app/clients.html', context=context)


def add_car(request):
    if request.method == 'GET':
        title = 'Добавить машину'
        form = CarForm()
        context = {'title': title, 'menu': menu, 'form': form}
        return render(request, 'my_app/car_add.html', context=context)

    if request.method == 'POST':
        carform = CarForm(request.POST)
        if carform.is_valid():
            car = Car()
            car.brand = carform.cleaned_data['brand']
            car.model = carform.cleaned_data['model']
            car.color = carform.cleaned_data['color']
            car.power = carform.cleaned_data['power']
            car.year = carform.cleaned_data['year']
            car.save()
        return cars(request)


def add_driver(request):
    title = 'Добавить водителя'
    form = DriverForm()
    context = {'title': title, 'menu': menu, 'form': form}
    return render(request, 'my_app/driver_add.html', context=context)


def add_client(request):
    title = 'Добавить клиента'
    form = ClientForm()
    context = {'title': title, 'menu': menu, 'form': form}
    return render(request, 'my_app/client_add.html', context=context)


