# from django.http import HttpResponse
# from .forms import CarForm, DriverForm, ClientForm
# from .models import Car, Client, Driver
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_protect
import datetime
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.http import HttpResponse
from .forms import *
from .models import *
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required  ## Требует авторизации пользователя
from django.contrib.admin.views.decorators import staff_member_required  ## Требует авторизации Админа

# Create your views here.

menu = [{'title': "О сайте", 'url_name': 'my_app:about'},
        {'title': "Машины парка", 'url_name': 'my_app:cars'},
        {'title': "Водители парка", 'url_name': 'my_app:drivers'},
        {'title': "Клиенты", 'url_name': 'my_app:clients'},
        {'title': "Сотрудники", 'url_name': 'my_app:employee_list'},
        {'title': "Заказы", 'url_name': 'my_app:order_list'},

        ]


# def index_main(request):
#     return HttpResponse('<h1>Main page</h1>')  # Всегда веб-страничка долна возвращаться (результат ответа на запрос


def index_my_app(request):
    title = 'Моя главная страница'
    context = {'title': title, 'menu': menu}
    return render(request, 'my_app/index.html', context=context)


def about(request):
    title = 'О сайте'
    context = {'title': title, 'menu': menu}
    return render(request, 'my_app/about.html', context=context)


def contacts(request, id):
    url_id = id
    name = request.GET.get('name')  # То, что мы передаем через ? &
    age = request.GET.get('age')
    # return HttpResponse(f'Page_contacts, id = {id}')
    get_params = {'mane': name, "age": age}
    return HttpResponse(f'Page contacts, url_parametr_id = {url_id}, get_params = {get_params}')


@login_required()  ## Декоратор который ограничивает доступ к ссылкам незарег-м пользователям
def cars(request):
    title = 'Машины'
    cars = Car.objects.all()

    context = {'title': title, 'menu': menu, 'cars': cars}
    return render(request, 'my_app/cars.html', context=context)


@login_required
def drivers(request):
    title = 'Водители'
    drivers = Driver.objects.all()
    context = {'title': title, 'menu': menu, 'drivers': drivers}
    return render(request, 'my_app/drivers.html', context=context)


def driver_card(request, pk):
    title = 'Driver info'
    driver = get_object_or_404(Driver, pk=pk)
    context = {'menu': menu, 'title': title, 'driver': driver}
    return render(request, 'my_app/driver_card.html', context=context)

@staff_member_required()  ## Вход только суперпользователям или админам
def clients(request):
    title = 'Клиенты'
    clients = Client.objects.all()
    paginator = Paginator(clients, 2)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'title': title, 'menu': menu, 'clients': clients, 'page_obj': page_obj}

    return render(request, 'my_app/clients.html', context=context)


def add_car(request):
    if request.method == 'GET':
        title = 'Добавить машину'
        form = CarForm()
        context = {'title': title, 'menu': menu, 'form': form}
        return render(request, 'my_app/car_add.html', context=context)

    if request.method == 'POST':
        carform = CarForm(request.POST, request.FILES)
        if carform.is_valid():
            car = Car()
            car.brand = carform.cleaned_data['brand']
            car.model = carform.cleaned_data['model']
            car.color = carform.cleaned_data['color']
            car.power = carform.cleaned_data['power']
            car.year = carform.cleaned_data['year']
            car.image = carform.cleaned_data['image']
            car.save()
        return cars(request)


def car_detail(request, pk):
    car = Car.objects.get(pk=pk)
    title = 'Car detail'
    context = {'object': car, 'title': title}

    return render(request, 'my_app/car_detail.html', context=context)


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


def clients(request):
    title = 'Клиенты'
    clients = Client.objects.all()
    context = {'title': title, 'menu': menu, 'clients': clients}
    return render(request, 'my_app/clients.html', context=context)


def add_client(request):

    title = 'Добавить клиента'

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            age = datetime.date.today().year - form.cleaned_data['birthday'].year
            instance.age = age
            instance.save()
            # form.save()
            return clients(request)
    else:
        form = ClientForm()
    context = {'title': title, 'menu': menu, 'form': form}
    return render(request, 'my_app/client_add.html', context=context)


def client_card(request, pk):
    title = 'Client info'
    # client = Client.objects.get(pk=pk)
    client = get_object_or_404(Client, pk=pk)
    context = {'menu': menu, 'title': title, 'client': client}

    return render(request, 'my_app/client_card.html', context=context)


def add_driver(request):
    title = 'Добавить водителя'
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return drivers(request)
    else:
        form = DriverForm()
    context = {'title': title, 'menu': menu, 'form': form}
    return render(request, 'my_app/driver_add.html', context=context)



class EmployeeList(ListView):
    model = Employee
    template_name = 'main/employee_list.html'
    context_object_name = 'employees'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        # получение общего контекста из родительского класса
        context = super().get_context_data(**kwargs)
        # изменение родительского контекста (добавление ключей словаря)

        context['title'] = 'Сотрудники'
        context["count"] = Employee.objects.count()
        context['menu'] = menu
        return context


class EmployeeDetail(DetailView):
    model = Employee
    template_name = 'main/employee_detail.html'
    context_object_name = 'employee'

    def get_context_data(self, **kwargs):
        # получение общего контекста из родительского класса
        context = super().get_context_data(**kwargs)
        context['title'] = 'Информация о сотруднике'
        context['menu'] = menu

        return context


class EmployeeCreate(CreateView):
    model = Employee
    # fields = '__all__'
    form_class = EmployeeForm
    template_name = 'my_app/employee_form.html'




class EmployeeUpdate(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'my_app/employee_update.html'


class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'my_app/delete.html'
    success_url = reverse_lazy('my_app:employee_list')


class OrderCreate(CreateView):  ##
    model = Order
    fields = '__all__'
    template_name = 'my_app/order_form.html'


class OrderList(ListView):
    model = Order
    template_name = 'my_app/order_list.html'
    context_object_name = 'objects'