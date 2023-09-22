
from django import forms


class TrabajoFormulario(forms.Form):
    trabajo=forms.CharField()
    numero=forms.IntegerField()
    
class TrabajadorFormulario(forms.Form):
    nombre =forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    
class EntregaFormulario(forms.Form): 
    nombre = forms.CharField(max_length=40)
    fechaDeEntrega = forms.DateField()
    entregado = forms.BooleanField()
    link = forms.CharField(max_length=256)