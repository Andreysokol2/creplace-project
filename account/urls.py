from django.urls import path
from django.contrib.auth import views as standart_views

from . import views

urlpatterns = [
    path('account/', views.user_account, name = 'user_account'),
    # path('id<int:account_id>/', views.account, name = 'account'),
    ]