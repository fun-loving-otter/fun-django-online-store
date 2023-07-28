from django.urls import path

from . import views #in the same directory

urlpatterns = [

        path('register',views.register,name='register'),

]