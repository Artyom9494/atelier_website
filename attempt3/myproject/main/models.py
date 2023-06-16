from django.db import models
from datetime import date
from django.db.models import F
from django.utils.dateparse import parse_date

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    surname = models.CharField (max_length=35,blank=False, verbose_name="Фамилия")
    name = models.CharField (max_length=35, blank=False, verbose_name="Имя")
    name2 = models.CharField (max_length=35, verbose_name="Отчетсво")
    position = models.CharField (max_length=35, verbose_name="Должность",blank=False)
    birthday = models.DateField(blank=False, verbose_name="Дата рождения")
    phone = models.CharField(max_length=35, blank=False, verbose_name="Телефон")
    email = models.EmailField(max_length=35, blank=False)

    def __str__(self):
        return f'{self.surname} {self.name}'


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    surname = models.CharField (max_length=35,blank=False,verbose_name="Фамилия")
    name = models.CharField (max_length=35, blank=False,verbose_name="Имя")
    name2 = models.CharField (max_length=35,verbose_name="Отчетсво")
    birthday = models.DateField(blank=False,verbose_name="Дата рождения")
    phone = models.CharField(max_length=11, blank=False,verbose_name="Телефон")
    email = models.EmailField(max_length=35, blank=False)
    orders_col = models.IntegerField(default = 0)
    last_order_date = models.DateField(default=date.today,verbose_name="Дата последнего заказа")

    def __str__(self):
        return f'{self.surname} {self.name}'
    
class Services(models.Model):  
    id = models.AutoField(primary_key=True)
    name = models.CharField (max_length=35, blank=False,verbose_name="Услуга")
    price = models.FloatField (blank=False, verbose_name="Стоимость")
    def __str__(self):
        return f'{self.name} {self.price}р.'
    
class Ordered_Services(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey ('Orders', on_delete=models.CASCADE)
    services = models.ForeignKey('Services', on_delete=models.CASCADE)

    def __str__(self):
        return f'Услуги заказа: {self.order}'

class Orders(models.Model):
    ACCEPTED = 'Принят'
    IN_PROGRESS = 'В работе'
    READY = 'Готов к выдаче'
    GIVEN = 'Выдан'
    CANCELLED = 'Отменен'
    STATUS = [
        (ACCEPTED, 'Принят'),
        (IN_PROGRESS, 'В работе'),
        (READY, 'Готов к выдаче'),
        (GIVEN, 'Выдан'),
        (CANCELLED, 'Отменен'),
    ]
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey ('Users', on_delete=models.CASCADE,verbose_name="Заказчик")
    employee_id = models.ForeignKey('Employee', on_delete=models.CASCADE, null=True,verbose_name="Исполнитель")
    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default=ACCEPTED,
        verbose_name="Статус заказа"
    )
    service = models.ForeignKey('Services', on_delete=models.CASCADE, null=True,verbose_name="Услуга")
    connected_order = models.ForeignKey('Orders',on_delete=models.CASCADE, null=True,blank = True, verbose_name="Связанный заказ")
    order_date =  models.DateField(default=date.today,verbose_name="Дата заказа")
    comment = models.CharField (max_length=200, default='Пусто',verbose_name="Комментарий")

    def __str__(self):
        return f'Заказ: {self.id}'
    
    def save(self, *args, **kwargs):
        if not self.pk:
            Users.objects.filter(pk=self.user_id_id).update(orders_col=F('orders_col')+1)
            #Users.objects.filter(pk=self.user_id_id).update(last_order_date=date.today)
        super().save(*args, **kwargs)
     



    
    