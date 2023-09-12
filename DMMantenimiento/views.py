from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Trabajo, Trabajador, Entregas
from .forms import TrabajoFormulario, TrabajadorFormulario, EntregaFormulario

# Create your views here.

def trabajo(req, nombre, numero):
    
    trabajo = Trabajo(nombre=nombre, numero=numero)
    trabajo.save()
    
    return HttpResponse(f"""
    <p>Trabajo: {trabajo.nombre} - Número: {trabajo.numero} creado con exito </p>
    """)

def listar_trabajos(req):
    lista = Trabajo.objects.all()
    
    return render(req, "lista_trabajos.html", {"lista_trabajos": lista})

def inicio(req):
    
    return render(req, "inicio.html")

def trabajo(req):
    
    return render(req, "trabajo.html")

def trabajador(req):
    
    return render(req, "trabajador.html")

def entregas(req):
    
    return render(req, "entregas.html")

def trabajo_formulario (req):
    
    
    if req.method == 'POST':    
        miFormulario = TrabajoFormulario(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            trabajo = Trabajo(nombre=data["trabajo"], numero=data["numero"])
            trabajo.save()
        return render(req,"inicio.html")
    else:
        miFormulario = TrabajoFormulario()
        return render(req, "trabajoFormulario.html", {"miFormulario": miFormulario})


def busqueda_trabajo (req):
    return render(req, "busquedaTrabajo.html")

def buscar(req: HttpRequest):
    
    if req.GET["nombre"]:
        nombre = req.GET["nombre"]
        nombre = Trabajo.objects.get(nombre=nombre)
        return render(req, "resultadoBusqueda.html", {"nombre": nombre})
    else:
        return HttpResponse(f"Debe agregar un trabajo")



    return HttpResponse(f'Buscando el trabajo {req.GET["trabajo"]}')


    

def trabajador_formulario(req):
    if req.method == 'POST':
        miFormularioTrab = TrabajadorFormulario(req.POST) 
        if miFormularioTrab.is_valid():
            data = miFormularioTrab.cleaned_data
            trabajador = Trabajador(nombre=data["nombre"], apellido=data["apellido"], email=data["email"])  
            trabajador.save()
            return render(req, "inicio.html")
    else:
        miFormularioTrab = TrabajadorFormulario()
    return render(req, "trabajadorFormulario.html", {"miFormularioTrab": miFormularioTrab})

def entrega_formulario(req):
    if req.method == 'POST':
        miFormularioEnt = EntregaFormulario(req.POST) 
        if miFormularioEnt.is_valid():
            data = miFormularioEnt.cleaned_data
            entrega = Entregas(nombre=data["nombre"], fechaDeEntrega=data["fechaDeEntrega"], entregado=data["entregado"], link=data["link"]) 
            entrega.save()
            return render(req, "inicio.html")
    else:
        miFormularioTrab = TrabajadorFormulario()
    return render(req, "trabajadorFormulario.html", {"miFormularioTrab": miFormularioTrab})