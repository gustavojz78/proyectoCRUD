from django.urls import path
from TiendApp.views import *

 
urlpatterns = [
    path("", inicio, name="Inicio"),
    path("tiendas/", tiendas, name = "Tiendas"),
    path("contactos/", agenda, name = "Contacto"),
    path("staff/", staff, name ="Staff"),
    path("ventas/", ventas, name= "Ventas"),
    path("formulario/", entrar, name="Entrar"),
    path("buscarProducto/", buscarProducto, name="Buscar"),
    path("buscar/", buscar),
    path("borrarEmpleado/<empleados_dni>/", eliminarStaff, name="eliminarEmpleado"),
    path("editarEmpleado/<empleados_dni>/", actualizar, name="editarEmpleado")
#recordar que esta ultima url es la que uso en el template para buscar productos
]

