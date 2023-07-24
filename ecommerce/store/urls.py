from django.urls import path

from . import views #in teh same directory

urlpatterns = [

    path('',views.store,name='store'),



]