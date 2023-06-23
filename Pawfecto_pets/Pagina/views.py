from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm,RegistroUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test

def inicio(request):
    return render(request, 'inicio.html')

def Contactanos(request):
    return render(request, 'Contactanos.html')

def Razas(request):
    return render(request, 'Razas.html')

def sobrenosotros(request):
    return render(request, 'sobrenosotros.html')

def mostrar(request):
    return render(request, 'mostrar.html')


@staff_member_required
def otra(request):
    productos = Producto.objects.all()
    return render(request, 'otra.html', {'Productos': productos})

def tarjetas(request):
    productos = Producto.objects.all()
    return render(request, 'tarjetas.html', {'Productos': productos})

def mostrar(request):
    productos = Producto.objects.all()
    return render(request, 'mostrar.html', {'Productos': productos})

@login_required
def crear(request):
    if request.method=="POST":
        productoForm=ProductoForm(request.POST,request.FILES)
        if productoForm.is_valid():
            productoForm.save()     #similar al insert en función
            return redirect ('otra')
    else:
        productoForm=ProductoForm()
    return render (request, 'crear.html', {'productoForm': productoForm})

@login_required
def eliminar(request, id): 
    productoEliminado = Producto.objects.get(codigo=id) #similar a select * from... where...
    productoEliminado.delete()
    return redirect ('otra')


@login_required
def modificar(request, id): 
    productoModificado=Producto.objects.get(codigo=id) #buscamos el objeto
    datos ={
        'form':ProductoForm(instance=productoModificado)
    }
    if request.method=="POST":
        formulario = ProductoForm(data=request.POST, instance=productoModificado)
        if formulario.is_valid():
            formulario.save()
            return redirect ('otra')
    return render(request, 'modificar.html', datos)


def registrar(request):
    data = {
        'form' : RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], 
                                password = formulario.cleaned_data["password1"])
            login(request, user)
            return redirect ('Inicio')
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)


def mostrar(request):
    productito = Producto.objects.all()
    datos={
        'productito': productito
    }
    return render(request, 'mostrar.html', datos)

