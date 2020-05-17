from django.contrib import admin
from .models import Battery, Order


admin.site.site_header = "Car Battery Admin"
admin.site.site_title = "Car Battery Admin area"
admin.site.index_title = "Добро Пожаловать в Админку Car Battery"


admin.site.register(Battery)
admin.site.register(Order)