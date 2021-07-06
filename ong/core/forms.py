from django import forms
from django.forms import ModelForm
from .models import Proveedor

class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['rut','razon_social','descripcion','telefono','mail','fk_servicio']
        widgets = {
            'rut': forms.TextInput(attrs={'placeholder': 'Rut sin puntos ni guión',
            'autocomplete': 'off',
            'onKeypress':'if (event.keyCode < 48 || event.keyCode > 57) event.returnValue = false;'}),
            'razon_social': forms.TextInput(attrs={'autocomplete': 'off'}),
            'descripcion': forms.TextInput(attrs={'autocomplete': 'off'}),
            'telefono': forms.TextInput(attrs={'autocomplete': 'off',
            'maxlength':'10',
            'onKeypress':'if (event.keyCode < 48 || event.keyCode > 57) event.returnValue = false;'}),
            'mail': forms.TextInput(attrs={'autocomplete': 'off'}),
        }

class ProveedorFormEdit(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['razon_social','descripcion','telefono','mail','fk_servicio']
        widgets = {
            'razon_social': forms.TextInput(attrs={'autocomplete': 'off'}),
            'descripcion': forms.TextInput(attrs={'autocomplete': 'off'}),
            'telefono': forms.TextInput(attrs={'autocomplete': 'off',
            'maxlength':'10',
            'onKeypress':'if (event.keyCode < 48 || event.keyCode > 57) event.returnValue = false;'}),
            'mail': forms.TextInput(attrs={'autocomplete': 'off'}),
        }
