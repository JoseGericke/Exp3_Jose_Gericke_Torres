from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='Inicio'), 
    path('Contactanos/', views.Contactanos, name="contactanos"),
    path('Razas/', views.Razas, name="razas"),
    path('sobrenosotros/', views.sobrenosotros, name="sobrenosotros"),
    path('tarjetas/', views.tarjetas, name="tarjetas"),
    path('otra/', views.otra, name="otra"),
    path('mostrar/', views.mostrar, name="mostrar"),
    path('registrar/', views.registrar, name="registrar"),
    path('crear/', views.crear, name='crear'),
    path('eliminar/<id>', views.eliminar, name="eliminar"),
    path('modificar/<id>', views.modificar, name="modificar"),
]