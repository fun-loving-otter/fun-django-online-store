from django.contrib import admin

# Register your models here.

from .models import Category,Product    #registering the models

admin.site.register(Category)

admin.site.register(Product)


