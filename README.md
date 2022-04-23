# proyectoCRUD
Proyecto coder hasta CRUD
Este proyecto trata sobre una app para ingresar datos en una tienda de ropa. En el terminal colocaremos /tiendapp para ingresar a la pagina. 
Ahi nos encontraremos en un template donde tenemos varios botonos de acceso. Los principales son ENTRAR y BUSCAR.
En ENTRAR podemos insertar productos. Tendran un codigo, nombre y precio.
Si escribimos el mismo codigo de un producto ya existente, podriamos cambiar el articulo y su precio.
En BUSCAR, podemos buscar un articulo, ya sea por el nombre especifico o por alguna letra que este contenida en su nombre. 
Ejemplo, coloco r, va a listar, remeras, camperas, jogger, relojes, etc.
Luego tenemos otros botones de acción arriba. Inicio, Tiendas, Staff y Contacto. 
Hasta ahora solo modfificamos Staff, por medio del CRUD. Podemos ingresar, modoficar y borrar a un miembro del staff.
En Staff, cuando ingresamos a alguien, aparecera el mensaje de Ingrese el NUEVO empleado. Cuando editamos, aparecerá Ingrese datos MODIFICADOS.
Cabe destacar que podemos modificar todos los datos, pero si cambiamos el DNI, al ser un primary key, creara un nuevo empleado.
Despues podemos borrar el empleado con el DNI erróneo. 
Trataremos por CBV (Vistas basadas en clases) aplicar lo que hicimos con Staff a Tiendas y Contactos.

