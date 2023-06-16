from django.contrib import admin
from .models import Employee, Users, Services, Ordered_Services, Orders

admin.site.register(Employee)
admin.site.register(Users) 
admin.site.register(Services) 
admin.site.register(Ordered_Services) 
admin.site.register(Orders) 