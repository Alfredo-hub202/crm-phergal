from django.conf.urls import url
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from bootstrap_modal_forms.generic import BSModalCreateView
from django.http import HttpResponse
from datetime import date
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import empleados_Form, Cliente_Form, Cli_retos_art_Form
from django.views.generic import ListView, DetailView
from django.template import loader

# Class de Empleados


def listar_empleados(request):
    empleados = Empleados.objects.filter(cliente_id=request.user.id)
    context = {'empleados': empleados}
    return render(request, 'retos/index.html', context)


def create(request):
    form = empleados_Form(request.POST)
    print(request.POST)
    # Le damos solo una opcion al campo status
    form.fields['cliente'].choices = [(request.user.id, request.user.id)]
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'retos/create.html', {'form': form})


def update(request, id):
    empleados = Empleados.objects.get(id=id)
    form = empleados_Form(instance=empleados)
    if request.method == 'POST':
        form = empleados_Form(request.POST, instance=empleados)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile details updated.')
        return redirect('index')
    # return render(request, 'retos/create_copy.html', {'form': form})
    return render(request, 'retos/edit.html', {'form': form})


# Class de Cliente


def update_cliente(request, id):
    empleados = Cliente.objects.get(id=id)
    form = Cliente_Form(instance=empleados)
    if request.method == 'POST':
        form = Cliente_Form(request.POST, instance=empleados)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile details updated.')
        return redirect('index')
    # return render(request, 'retos/create_copy.html', {'form': form})
    return render(request, 'retos/profile.html', {'form': form})

# Class de Tipos Retos


def listar_todos_retos(request):
    todos_retos = Cliente_retos.objects.filter(cliente_id=request.user.id)
    print(todos_retos)
    context = {'todos_retos': todos_retos}
    print(context)
    return render(request, 'retos/edit.html', context)


# Class de Tipos Retos
date = date.today()


def listar_detalles__retos(request, id):
    retos = Cliente_retos.objects.filter(
        cliente_id=id).filter(fecha_fin__gte=date).filter(estado=1)
    retos_finalizados = Cliente_retos.objects.filter(
        cliente_id=id).filter(fecha_fin__lte=date)
    return render(request, 'retos/ver_reto.html', {'retos': retos, 'retos_finalizados': retos_finalizados})


def create_detalles__productos(request, id):
    if request.method == 'POST':
        form = Cli_retos_art(request.POST, cliente_reto_id=id)
        form.fields['cliente_reto'].choices = [(id, 'hola')]

        if form.is_valid():
            form.save()
        return redirect('index')
    form = Cli_retos_art_Form()
    productos = Productos_retos.objects.filter(tipo_retos_id=id)
    # return render(request, 'retos/create_copy.html', {'form': form})
    return render(request, 'retos/ver_productos.html', {'form': form, 'productos': productos})


def listar_detalles__productos(request, id):
    productos = Cli_retos_art.objects.filter(cliente_reto_id=id)
    # productos = Cli_retos_art.objects.get(cliente_reto_id=id)
    context = {'productos': productos}
    return render(request, 'retos/ver_productos.html', context)


@login_required(login_url="/login/")
def index(request):

    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
