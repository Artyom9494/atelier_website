from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', views.main_page, name='home'),
    path('about/', views.main_about, name='about'),
    
    #Сотрудники
    path('createEmployee/', views.create_employee, name='createEmployee'),
    path('Employee/', views.Employee_view, name='Employee'),
    path('Employee/<int:id>/', views.Employee_detail_view),
    path('updateEmployee/<int:id>/', views.update_employee),
    path('deleteEmployee/<int:id>/', views.delete_employee),
    path('searchEmployee/', views.Employee_view, name='SearchEmployee'),
    #Клиенты
    path('createUsers/', views.create_user),
    path('Users/', views.Users_view, name='Users'),
    path('Users/<int:id>/', views.Users_detail_view),
    path('updateUsers/<int:id>/', views.update_user),
    path('deleteUsers/<int:id>/', views.delete_user),
    path('searchUsers/', views.Users_view, name='SearchUsers'),
    #Услуги
    path('createServices/', views.create_service),
    path('Services/', views.Services_view, name='Services'),
    path('Services/<int:id>/', views.Services_detail_view),
    path('updateServices/<int:id>/', views.update_service),
    path('deleteServices/<int:id>/', views.delete_service) ,
    path('searchService/', views.Services_view, name='SearchService'),
    path('ServicesUsr/', views.Services_view_usr, name='Services_Usr'),
    path('searchServiceByUser/', views.SearchServiceByUser, name='searchServiceByUser'),
    #Заказы
    path('createOrders/', views.create_order),
    path('Orders/', views.Orders_view, name='Orders'),
    path('Orders/<int:id>/', views.Orders_detail_view),
    path('updateOrders/<int:id>/', views.update_order),
    path('deleteOrders/<int:id>/', views.delete_order),
    path('searchOrders/', views.Orders_view, name='SearchOrder'),
    path('OrdersAllByUser/<int:id>/', views.Orders_all_detail_view, name='OrdersByUser'),
    path('searchOrderByUser/', views.SearchOrderByUser, name='searchOrderByUser'),
    #Авторизация для админа
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    #Главная
    path('contacts/', views.contacts, name='contacts'),
    path('about_us/', views.about_us, name='about_us'),
]