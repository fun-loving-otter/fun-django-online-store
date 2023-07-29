from django.urls import path

from . import views                                                                     #in the same directory

urlpatterns = [

    #Store homepage
    path('',views.store,name='store'),

    #Individual product
    path('product/<slug:product_slug>/',views.product_info,name='product-info'), #referencing a slug variable

    # Individual category, updating slug to reference category_slug from list_category function
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),  # referencing a slug variable

]