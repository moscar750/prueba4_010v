from django.shortcuts import render,redirect
from rest_framework import generics
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Proveedor
from .serializers import ProveedorSerilizer
from .forms import ProveedorForm, ProveedorFormEdit
from django.contrib import messages
from rest_framework import viewsets


# Create your views here.
def inicio(request):
    return render(request,'core/index.html')
def contacto(request):
    return render(request,'core/contacto.html')
def enviado(request):
    return render(request,'core/formulario-enviado.html')
def exito(request):
    return render(request,'core/login-exitoso.html')
def login1(request):
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


class ProveedorList(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerilizer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class Login(FormView):
    template_name = "core/login_rest.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('Proveedor_rest:proveedor_list')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,*kwargs)

    def form_valid(self,form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user = user)
        if token:
            login(self.request, form.get_user())
            return super(Login,self).form_valid(form)

class Logout(APIView):
    def get(self,request, format = None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status = status.HTTP_200_OK)

class ProveedorViewset(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerilizer

    def get_queryset(self):
        proveedores = Proveedor.objects.all()
        rut = self.request.GET.get('rut')

        if rut:
            proveedores = proveedores.filter(rut=rut)

        return proveedores
