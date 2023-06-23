from django import forms
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
     
        fields = ['codigo', 'marca', 'nombre', 'categoria', 'imagen']
        labels ={
            'codigo':'codigo',
            'marca' : 'Marca',
            'nombre': 'nombre',
            'categoria':'Categoria',
            'imagen':'Imagen'
        }
        widgets={

            'codigo':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese codigo..',
                    'id': 'codigo',
                    'class': 'form-control',
                }
            ),
            'marca': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese marca..',
                    'id':'marca',
                    'class':'form-control',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese nombre..',
                    'id':'nombre',
                    'class':'form-control',
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'id':'categoria',
                    'class':'form-control',
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class':'form-control',
                    'id': 'imagen',
                }
            )
        }