from django import forms 
from main.models import *

class EmployeeForm(forms.ModelForm): 
    class Meta: 
        model = Employee 
        fields = "__all__" 

class UsersForm(forms.ModelForm): 
    class Meta: 
        model = Users
        fields =['surname','name','name2','birthday','phone','email','orders_col','last_order_date']

class ServicesForm(forms.ModelForm): 
    class Meta: 
        model = Services
        fields = "__all__" 

class OrdersForm(forms.ModelForm): 
    class Meta: 
        model = Orders
        fields = "__all__" 