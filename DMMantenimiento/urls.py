
from django.urls import path
from .views import *

urlpatterns = [
    path('agrega-trabajo/<nombre>/<numero>', trabajo),
    path('', inicio, name="Inicio"),
    path('lista-trabajos/', listar_trabajos, name="ListaTrabajos"),
    path('trabajo/', trabajo, name="Trabajo"),
    path('trabajador/', trabajador,name="Trabajador"),
    path('entregas/', entregas,name="Entregas"),
    path('trabajoFormulario/', trabajo_formulario,name="TrabajoFormulario"),
    path('busqueda-trabajo/', busqueda_trabajo,name="BusquedaTrabajo"),
    path('buscar/', buscar ,name="Buscar"),
    path('trabajadorFormulario/', trabajador_formulario,name="TrabajadorFormulario"),
    path('entrega_Formulario/', entrega_formulario,name="EntregaFormulario"),
]

