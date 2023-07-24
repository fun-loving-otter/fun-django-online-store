from django.urls import path

from . import views #in teh same directory

urlpatterns = [

    path('',views.store,name='store'),

    path('product/<slug:slug>/',views.product_info,name='product-info'), #referencing a slug variable



]