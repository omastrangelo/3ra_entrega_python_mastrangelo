   las listas que se pueden utilizar son las siguientes:
   
   
    path('agrega-trabajo/<nombre>/<numero>', trabajo),
    path('', inicio, name="Inicio"), (muestra el inicio)
    path('lista-trabajos/', listar_trabajos, name="ListaTrabajos"),  (presenta la lista de los trabajos agregados)
    path('trabajo/', trabajo, name="Trabajo"), (ruta)
    path('trabajador/', trabajador,name="Trabajador"),(ruta)
    path('entregas/', entregas,name="Entregas"), (ruta)
    path('trabajoFormulario/', trabajo_formulario,name="TrabajoFormulario"), (formulario para crear trabajo)
    path('busqueda-trabajo/', busqueda_trabajo,name="BusquedaTrabajo"), (busqueda de trabajo por nombre)
    path('buscar/', buscar ,name="Buscar"),
    path('trabajadorFormulario/', trabajador_formulario,name="TrabajadorFormulario"), (crear trabajador por datos)
    path('entregaFormulario/', entrega_formulario,name="EntregaFormulario"), (formulario de entrega, no funciona)

