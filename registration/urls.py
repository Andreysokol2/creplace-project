from django.urls import path
from django.contrib.auth import views as standart_views

from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('reg/', views.register, name = 'register'),
    path('email_confirmation/<email>', views.email_confirmation, name = 'email_confirmation'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', standart_views.LogoutView.as_view(), name='logout'),
    path('donat/', views.donat, name='donat'),
    path('aboutdata/', views.aboutdata, name='aboutdata'),
    ]
