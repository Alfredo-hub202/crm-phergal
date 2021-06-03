# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app import urls
from django.contrib import admin
from django.urls import path, include  # add this


urlpatterns = [
    path('admin/', admin.site.urls),           # Django admin route
    path('', include("authentication.urls")),  # Auth routes - login / register
    # path('',  include("app.urls")),             # UI Kits Html files
    path('',  include("retos.urls")),
    # path('', include("retos.urls")),           # Models retos

]

# Añadir Nombre panel Administración
admin.site.site_header = 'Retos Phergal'
