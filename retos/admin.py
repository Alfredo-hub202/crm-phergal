from django.contrib import admin


# Register your models here.
from .models import *


class Tipo_retos_admin(admin.ModelAdmin):
    # Listado Tipo de Retos
    list_display = ['description', 'n_producto',
                    'estado', 'created', 'changed']
    list_filter = ['estado', 'created']
    search_fields = ['description']

    ordering = ['estado']


class Empleados_admin(admin.ModelAdmin):
    # Listado Empleados
    list_display = ['nombre', 'apellido',
                    'telefono', 'fecha_nacimiento', 'email']
    list_filter = ['nombre', 'apellido']
    search_fields = ['nombre']

    ordering = ['nombre']


class Productos_admin(admin.ModelAdmin):
    # Listado Productos
    list_display = ['nombre', 'description', 'tipo_articulo',
                    'marca', 'gama', 'activo_pedido', 'activo_devolucion']
    list_filter = ['nombre', 'description']
    search_fields = ['nombre']

    ordering = ['nombre']

# class Productos_retos_admin(admin.ModelAdmin):
#     # Listado Productos
#     list_display = ['nombre', 'description', 'tipo_articulo',
#                     'marca', 'gama', 'activo_pedido', 'activo_devolucion']
#     list_filter = ['nombre', 'description']
#     search_fields = ['nombre']

#     ordering = ['nombre']


class Cliente_admin(admin.ModelAdmin):
    # Listado Productos
    list_display = ['nombre', 'apellido', 'nif',
                    'acepta_el_contrato', 'acuerdo']
    list_filter = ['nombre', 'nif', 'apellido']
    search_fields = ['nombre', 'apellido', 'nif']

    ordering = ['nombre']


class Cliente_retos_admin(admin.ModelAdmin):
    # Listado Productos
    list_display = ['nombre', 'cliente', 'tipos_retos',
                    'fecha_ini', 'fecha_fin', 'max_venta', 'n_ventas_activas']
    list_filter = ['nombre', 'cliente', 'tipos_retos']
    search_fields = ['nombre', 'cliente', 'tipos_retos']

    ordering = ['nombre']


class Cliente_retos_admin_art(admin.ModelAdmin):
    # Listado Productos
    list_display = ['n_ticket', 'images', 'validar_foto', 'clave_reto_farmacia',
                    'fecha_alta', 'cliente_reto', 'Productos', 'productos_regalo']
    list_filter = ['n_ticket', 'images', 'validar_foto']
    search_fields = ['n_ticket', 'images', 'validar_foto']

    ordering = ['n_ticket']


# ---
# cliente_codigo
# forma_pago
# tipo_Negocio
# nombre
# apellido
# clasificacion_global_ano_act
# facturacion_ano_ant
# clasificacion_potencial
# acuerdo
# nif
# bloqueado
# grupo_compra
# clasificacion_global_ano_ant
# facturacion_ano_act
# acepta_el_contrato
# *---
admin.site.register(Tipo_retos, Tipo_retos_admin)
admin.site.register(Empleados, Empleados_admin)
admin.site.register(Productos, Productos_admin)
admin.site.register(Productos_retos)


admin.site.register(Gama)
admin.site.register(Marca)
admin.site.register(Tipo_producto)
admin.site.register(Productos_regalo)

admin.site.register(Forma_pago)
admin.site.register(Tipo_Negocio)
admin.site.register(Cliente, Cliente_admin)
admin.site.register(Cliente_retos, Cliente_retos_admin)
admin.site.register(Cli_retos_art, Cliente_retos_admin_art)
