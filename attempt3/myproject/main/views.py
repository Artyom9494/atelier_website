from django.shortcuts import redirect, render, get_object_or_404
from main.models import Employee, Users, Services
from main.forms import *
from django.http import Http404
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.db.models import Q


def main_page(request):
    return render(request, 'main/index.html', {'title': 'Главная страница'})


def main_about(request):
    return render(request, 'main/about.html', {'title': 'О нас'})

def contacts(request):
    return render(request, 'test/contacts.html', {'title': 'Контакты'})

def about_us(request):
    return render(request, 'test/about_us.html', {'title': 'О нас'})


# -----------------------------Employee(Сотрдункии)-------------------------------------

def Employee_view(request):
    if 'q' in request.GET:
        q = request.GET['q']
        dataset = Employee.objects.filter(Q(surname__icontains=q) | Q(name__icontains=q) | Q(phone__icontains=q))
    else:
        dataset = Employee.objects.all()
    return render(request, 'test/view_Emp.html', {'dataset': dataset, 'tableName': 'Employee'})


def Employee_detail_view(request, id):
    try:
        # Получаем сотрудника по-определенному id
        data = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        raise Http404('Такого сотрудника не существует')

    return render(request, 'test/detail_view_Emp.html', {'data': data, 'tableName': 'Employee'})


def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Employee')
    else:
        form = EmployeeForm()
        context = {
            'form': form
        }
        return render(request, 'test/create_Emp.html', {'tableName': 'Employee', 'form': form})

    all_users = Users.objects.all()
    return render(request, 'index.html', context={'data': all_users})


def update_employee(request, id):
    try:
        old_data = get_object_or_404(Employee, id=id)
    except Exception:
        raise Http404('Такого сотрудника не существует')
    # Если метод POST, то это обновленные данные сотрдуника
    # Остальные методы - возврат данных для изменения
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=old_data)
        if form.is_valid():
            form.save()
            return redirect(f'/Employee/{id}')
    else:
        form = EmployeeForm(instance=old_data)
        context = {
            'form': form
        }
        return render(request, 'test/update_Emp.html', {'tableName': 'Employee', 'form': form})


def delete_employee(request, id):
    try:
        data = get_object_or_404(Employee, id=id)
    except Exception:
        raise Http404('Такого сотрудника не существует')

    if request.method == 'POST':
        data.delete()
        return redirect('/Employee')
    else:
        return render(request, 'test/delete.html', {'tableName': 'Employee'})


# --------------------------Users(Клиенты)---------------------------------

def Users_view(request):
    if 'q' in request.GET:
        q = request.GET['q']
        dataset = Users.objects.filter(name__icontains=q)
    else:
        dataset = Users.objects.all()
    # Получаем всех клиентов
    # dataset = Users.objects.all()
    return render(request, 'test/view_Usr.html', {'dataset': dataset, 'tableName': 'Users'})


def Users_detail_view(request, id):
    try:
        # Получаем клиента по-определенному id
        data = Users.objects.get(id=id)
    except Users.DoesNotExist:
        raise Http404('Такого клиента не существует')

    return render(request, 'test/detail_view_Usr.html', {'data': data, 'tableName': 'Users'})


def create_user(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Users')
    else:
        form = UsersForm()
        context = {
            'form': form
        }
        return render(request, 'test/create_Usr.html', {'tableName': 'Users', 'form': form})
    all_users = Users.objects.all()
    return render(request, 'index.html', context={'data': all_users})


def update_user(request, id):
    try:
        old_data = get_object_or_404(Users, id=id)
    except Exception:
        raise Http404('Такого клиента не существует')
    # Если метод POST, то это обновленные данные клиента
    # Остальные методы - возврат данных для изменения
    if request.method == 'POST':
        form = UsersForm(request.POST, instance=old_data)
        if form.is_valid():
            form.save()
            return redirect(f'/Users/{id}')
    else:
        form = UsersForm(instance=old_data)
        context = {
            'form': form
        }
        return render(request, 'test/update_Usr.html', {'tableName': 'Users', 'form': form})


def delete_user(request, id):
    try:
        data = get_object_or_404(Users, id=id)
    except Exception:
        raise Http404('Такого клиента не существует')

    if request.method == 'POST':
        data.delete()
        return redirect('/Users')
    else:
        return render(request, 'test/delete.html', {'tableName': 'Users'})


# ------------------------------Services(Услуги)---------------------------------

def Services_view(request):
    if 'q' in request.GET:
        q = request.GET['q']
        dataset = Services.objects.filter(Q(name__icontains=q))
    else:
        dataset = Services.objects.all()
    return render(request, 'test/view_Srv.html', {'dataset': dataset, 'tableName': 'Services'})

def Services_view_usr(request):
    if 'q' in request.GET:
        q = request.GET['q']
        dataset = Services.objects.filter(Q(name__icontains=q))
    else:
        dataset = Services.objects.all()
    return render(request, 'test/view_Srv_Usr.html', {'dataset': dataset, 'tableName': 'Services'})


def Services_detail_view(request, id):
    try:
        # Получаем услугу по-определенному id
        data = Services.objects.get(id=id)
    except Services.DoesNotExist:
        raise Http404('Такого клиента не существует')

    return render(request, 'test/detail_view_Srv.html', {'data': data, 'tableName': 'Services'})


def create_service(request):
    if request.method == 'POST':
        form = ServicesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Services')
    else:
        form = ServicesForm()
        return render(request, 'test/create_Srv.html', {'tableName': 'Services', 'form': form})


def update_service(request, id):
    try:
        old_data = get_object_or_404(Services, id=id)
    except Exception:
        raise Http404('Такой услуги не существует')
    # Если метод POST, то это обновленные данные услуги
    # Остальные методы - возврат данных для изменения
    if request.method == 'POST':
        form = ServicesForm(request.POST, instance=old_data)
        if form.is_valid():
            form.save()
            return redirect(f'/Services/{id}')
    else:
        form = ServicesForm(instance=old_data)
        context = {
            'form': form
        }
        return render(request, 'test/update_Srv.html', {'tableName': 'Services', 'form': form})


def delete_service(request, id):
    try:
        data = get_object_or_404(Orders, id=id)
    except Exception:
        raise Http404('Такого клиента не существует')

    if request.method == 'POST':
        data.delete()
        return redirect('/Services')
    else:
        return render(request, 'test/delete.html', {'tableName': 'Services'})

    # ---------------------Orders(Заказы)---------------------------------------


def Orders_view(request):
    if 'q' in request.GET:
        q = request.GET['q']
        dataset = Orders.objects.filter(id__icontains=q)
    else:
        dataset = Orders.objects.all()
    return render(request, 'test/view_Ord.html', {'dataset': dataset, 'tableName': 'Orders'})


def Orders_all_detail_view(request, id):
    dataset = Orders.objects.filter(user_id=id)
    info = Users.objects.get(id=id)
    return render(request, 'test/detail_view_Ord_all.html', {'dataset': dataset, 'tableName': 'Orders', 'info': info, })


def Orders_detail_view(request, id):
    try:
        # Получаем заказ по-определенному id
        data = Orders.objects.get(id=id)
    except Orders.DoesNotExist:
        raise Http404('Такого клиента не существует')

    return render(request, 'test/detail_view_Ord.html', {'data': data, 'tableName': 'Orders'})


def create_order(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Orders')
    else:
        form = OrdersForm()
        context = {
            'form': form
        }
        return render(request, 'test/create_Ord.html', {'tableName': 'Orders', 'form': form})

    all_orders = Orders.objects.all()
    return render(request, 'index.html', context={'data': all_orders})


def update_order(request, id):
    try:
        old_data = get_object_or_404(Orders, id=id)
    except Exception:
        raise Http404('Такой услуги не существует')
    # Если метод POST, то это обновленные данные заказа
    # Остальные методы - возврат данных для изменения
    if request.method == 'POST':
        form = OrdersForm(request.POST, instance=old_data)
        if form.is_valid():
            form.save()
            return redirect(f'/Orders/{id}')
    else:
        form = OrdersForm(instance=old_data)
        context = {
            'form': form
        }
        return render(request, 'test/update_Ord.html', {'tableName': 'Orders', 'form': form})


def delete_order(request, id):
    try:
        data = get_object_or_404(Orders, id=id)
    except Exception:
        raise Http404('Такого клиента не существует')

    if request.method == 'POST':
        data.delete()
        return redirect('/Orders')
    else:
        return render(request, 'test/delete.html', {'tableName': 'Services'})
    # -------------------------------Вход админа---------------------------------


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'test/Entrance.html'

    def get_success_url(self):
        return reverse_lazy('Orders')


def logout_user(request):
    logout(request)
    return redirect('home')


# --------------------Поиск заказа для клиента----------------
def SearchOrderByUser(request):
    if 'q' in request.GET:
        q = request.GET['q']
        dataset = Orders.objects.filter(id__icontains=q)
    else:
        dataset = []
    #     dataset = Orders.objects.all()
    return render(request, 'test/view_User_Search_Order.html', {'dataset': dataset, 'tableName': 'Orders'})

def SearchServiceByUser(request):
    if 'q' in request.GET:
        q = request.GET['q']
        dataset = Services.objects.filter(name__icontains=q)
    else:
        dataset = []
    #     dataset = Orders.objects.all()
    return render(request, 'test/view_User_Search_Service.html', {'dataset': dataset, 'tableName': 'Services'})
# class Search(ListView):
#     template_name = 'test/view_Usr.html'
#     context_object_name = 'Users'

#     def get_queryset(self):
#         return Users.objects.filter(name__iregex=self.request.GET.get('q'))

#     def get_context_data(self,*args, **kwargs):
#         context = super().get_context_data(*args,**kwargs)
#         context['q'] = self.request.GET.get('q')
#         return context