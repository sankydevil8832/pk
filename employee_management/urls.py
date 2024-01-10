from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('create/', employee_create, name='employee_create'),
    path('<int:pk>/edit/', employee_update, name='employee_update'),
    path('<int:pk>/delete/', employee_delete, name='employee_delete'),
    path('register/', register,name='register'),
    path('login/', login,name='login'),
    path('logout/', logout,name='logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
