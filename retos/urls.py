from django.contrib import admin
from django.urls import path, re_path
from retos import views

from django.contrib.auth.views import LogoutView
urlpatterns = [

    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.tipo_retosDetailView.as_view(), name='detail'),


    path('', views.listar_empleados, name='index'),
    path('create_copy', views.create, name='create'),
    path('edit/<id>/', views.update, name='edit'),
    path('edit/<id>/', views.listar_todos_retos, name='tipo de retos'),
    path('profile/<id>/', views.update_cliente, name='update_cliente'),
    # path('delete/<int:pk>/', views.delete, name='delete'),
    path('ver_reto/<id>/', views.listar_detalles__retos, name='tipo de retos'),
    path('ver_productos/<id>/', views.create_detalles__productos,
         name='tipo de productos '),
    path('ver_productos/<id>/', views.listar_detalles__productos,
         name='tipo de productos '),
    # The home page
    path('', views.index, name='index'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),


]
