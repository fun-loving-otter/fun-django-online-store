from django.contrib import admin


from .models import Category,Product,Tag                                            #registering the models
#prepopulated with name and title
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields={'slug':('name',)}                     #added automatically and sharing the name value

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields={'tag_slug':('tag_name',)}






