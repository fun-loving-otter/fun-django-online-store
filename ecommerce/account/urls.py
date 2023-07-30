from django.urls import path

from . import views #in the same directory

urlpatterns = [

        path('register',views.register,name='register'),

        path('email-verification/<str:uidb64><str:token>/', views.email_verification, name='email-verification'),       #making url dynamic

        path('email-verification-sent', views.email_verification_sent, name='email-verification-sent'),

        path('email-verification-success', views.email_verification_success, name='email-verification-success'),

        path('email-verification-failed', views.email_verification_failed, name='email-verification-failed'),


        path('my-login', views.my_login, name='my-login'),


        path('dashboard',views.dashboard,name='dashboard'),

]