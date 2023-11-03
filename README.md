# API-REST para Productos
API REST para mostrar productos de acuerdo a ciertas lógicas de negocio. Aún en elaboración...
### Logrado:
* No se requiere registro para visualizar Nombre y Estado del producto
* Se requiere registro para visualizar Nombre, Estado, Categorías e Imágenes del
producto
* Usar jwt para el manejo de sesión
* Se requiere usuario aprobado para crear, modificar y eliminar productos.
### En progreso
* Colección de postman para pruebas()
### Siguientes pasos: 
* El listado de productos debe tener filtros de búsqueda por nombre, estado y
categorías
* Constuir una interfaz con angular como Frontend

## Endpoints
* `/products`: Lista solo de nombre y estado del producto
* `/products/<int:pk>`: Ver un producto en detalle(solo usuarios con jwt válido)

## Paquetes y entorno de ejecución
`Ubuntu` 22.08
`asgiref==`3.7.2
`Django==`4.2.5
`django-cors-headers==`4.3.0
`djangorestframework==`3.14.0
`djangorestframework-simplejwt==`5.3.0
`Pillow==`10.1.0
`PyJWT==`2.8.0
