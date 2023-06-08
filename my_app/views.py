from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Машины парка", 'url_name': 'cars'},
    {'title': "Водители парка", 'url_name': 'drivers'},
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
    context = {'title': title, 'menu': menu}
    return render(request, 'my_app/cars.html', context=context)


def drivers(request):
    title = 'Водители'
    context = {'title': title, 'menu': menu}
    return render(request, 'my_app/drivers.html', context=context)


def login(request):
    return HttpResponse('Page_login')


def contacts(request, id):
    url_id = id
    name = request.GET.get('name')  # То, что мы передаем через ? &
    age = request.GET.get('age')
    # return HttpResponse(f'Page_contacts, id = {id}')
    get_params = {'mane': name, "age": age}
    return HttpResponse(f'Page contacts, url_parametr_id = {url_id}, get_params = {get_params}')


