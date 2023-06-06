from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index_main(request):
    return HttpResponse('<h1>Main page</h1>')


def index_my_app(request):
    return HttpResponse('<h1>My_app_page</h1>')


def about(request):
    return HttpResponse('<h1>About_site</h1>')


def login(request):
    return HttpResponse('Page_login')


def contacts(request, id):
    url_id = id
    name = request.GET.get('name')  # То, что мы передаем через ? &
    age = request.GET.get('age')
    # return HttpResponse(f'Page_contacts, id = {id}')
    get_params = {'mane': name, "age": age}
    return HttpResponse(f'Page contacts, url_parametr_id = {url_id}, get_params = {get_params}')
