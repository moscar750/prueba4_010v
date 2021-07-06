from django.shortcuts import render
from .models import Proveedor
from .forms import ProveedorForm, ProveedorFormEdit
from django.contrib import messages
from rest_framework import viewsets
from .serializers import ProveedorSerilizer

# Create your views here.
def inicio(request):
    return render(request,'core/index.html')
def contacto(request):
    return render(request,'core/contacto.html')
def enviado(request):
    return render(request,'core/formulario-enviado.html')
def exito(request):
    return render(request,'core/login-exitoso.html')
def login(request):
    return render(request,'core/login.html')
def gatos(request):
    return render(request,'core/seccion-gatos.html')
def perros(request):
    return render(request,'core/seccion-perros.html')

def prov(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'core/proveedor.html', {'proveedores':proveedores})

def form_proveedor(request):
    proveedor = ProveedorForm()
    return render(request, 'core/form_proveedor.html', {"form":proveedor})

def envio_proveedor(request):
    form = ProveedorForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Guardado Correctamente")
        proveedor = ProveedorForm()
    return render(request, 'core/form_proveedor.html', {"form":proveedor})

def edit(request, idProveedor):
    proveedor = Proveedor.objects.filter(rut=idProveedor).first()
    form = ProveedorFormEdit(instance=proveedor)
    return render(request,'core/form_edit.html',{'form':form, 'proveedor':proveedor})

def actualizar_proveedor(request, idProveedor):
    proveedor = Proveedor.objects.get(rut=idProveedor)
    form = ProveedorFormEdit(request.POST, instance=proveedor)
    if form.is_valid():
        form.save()
        messages.success(request, "modificado Correctamente")
    proveedores = Proveedor.objects.all()
    return render(request,'core/proveedor.html',{'proveedores':proveedores})

def eliminar(request, idProveedor):
    proveedor = Proveedor.objects.get(pk = idProveedor)
    proveedor.delete()
    proveedores = Proveedor.objects.all()
    return render(request, 'core/proveedor.html', {'proveedores':proveedores, "mensaje": 'OK'})


class ProveedorViewset(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerilizer

    def get_queryset(self):
        proveedores = Proveedor.objects.all()
        rut = self.request.GET.get('rut')

        if rut:
            proveedores = proveedores.filter(rut=rut)

        return proveedores
