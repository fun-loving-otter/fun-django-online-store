from django.contrib import admin

# Register your models here.

from .models import Category,Product    #registering the models
#prepopulated with name and title
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields={'slug':('name',)}#added automatically and sharing the name value

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title')}






