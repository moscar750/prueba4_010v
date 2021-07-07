from django.urls import path, include
from .views import inicio, contacto, enviado, exito, login1, gatos, perros, prov, form_proveedor,envio_proveedor, edit, actualizar_proveedor, eliminar, ProveedorViewset,ProveedorList
from rest_framework import routers
from rest_framework.authtoken import views


urlpatterns = [
    path('', inicio, name="inicio"),
    path('inicio', inicio, name="inicio"),
    path('contacto', contacto, name="contacto"),
    path('enviado', enviado, name="enviado"),
    path('exito', exito, name="exito"),
    path('login', login1, name="login"),
    path('seccion-gatos', gatos, name="gatos"),
    path('seccion-perros', perros, name="perros"),
    path('proveedor', prov, name="proveedor"),
    path('form-proveedor', form_proveedor, name="form-proveedor"),
    path('guardar-proveedor', envio_proveedor, name="guardar-proveedor"),
    path('editar-proveedor/<str:idProveedor>', edit, name="editar-proveedor"),
    path('actualizar_proveedor/<str:idProveedor>', actualizar_proveedor, name="actualizar-proveedor"),
    path('eliminar/<str:idProveedor>', eliminar, name="eliminar-proveedor"),

    path('api_generate_token/', views.obtain_auth_token),



    path('proveedor_rest/',ProveedorList.as_view(), name="proveedor_list"),
]
