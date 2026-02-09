# api-gestion-pedidos-jesus
Sistema de gestión de pedidos como proyecto para materia desarollo de  Software Backend 2.
Esta API REST permite gestionar pedidos de cualquier tipo de clientes pensando en negocios pequeños. El sistema deberia poder hacer la creación de pedidos, el manejo de productos y el seguimiento del estado de cada pedido. Estoy como propuesta inicial ya se puede expander a mas opciones como cuidados de paquetes, cancelacion de servio o manejos personalizados.

El publico objetico son negocios en crecimiento que necesitan actualizarce a esta era de envios, de clientes deben poder registrar pedidos y empleados que deben actualizar su estado.

Recursos principales son usuarios, prdocutos, ordenes y objetos. En usuarios GET/ usario, POST/ usuario, GET/usuario/{id}. Prodcutos igual con GET/productos, POST/productos y PUT/productos/{id}. Ordenes con GET/ordenes, POST/Ordenes, GET/ordenes/{id}, PUT/ordenes/{id}/status. Por ultimo objetos es POST/ orders/{id} y DELETE /ordenes/{id}/items/{item_id}

Reglas de negocio

- No se puede crear un pedido sin al menos un producto.
- El stock del producto debe .
- El estado de un pedido solo pueden ser tres que son pendiente, enviado y entregado.
- Una vez entregado un producto solo se podra consultar informacion de este.
- Una funcion para calclular el costo del envio o productos a enviar.

Contrato preliminar, esta parte no la entendi bien asi que pense que podria hacer la creacion de un pedido, POST/ordenes

Request (json):
{
  "user_id": 1,
  "items": [
    { "product_id": 2, "quantity": 3 }
  ]
}
regresa:
{
  "order_id": 10,
  "status": "pending",
  "total": 650.00
}

segundo endpoint obtener un pedido por id, GET/ordenes/{id}

Request:  GET/ordenes/10
La API devuelve:
{
  "order_id": 10,
  "user_id": 1,
  "status": "pending",
  "items": [
    {
      "product_id": 2,
      "quantity": 3,
      "price": 150.00
    }
  ],
  "total": 450.00
}
Para la parte de instalacion y ejecucion digital no se si queria una imagen o solo instrucciones como iniciar el entorno virtual:
python -m venv venv
instalar dependencias con
pip install -r requirements.txt
ejecutar servidor.

En el apartadi de tecnologías elegidas tenemos la sugerida por el profesor FastAPI en Python con Uvicorn, tentativamente a SQL.
Configuración de rutas y controladores
Para la configuracion como pidio lo separamos en rutas y controladores, simplemente por orden y limpieza de codigo. La estrucura del codigo es:

app/
- main.py  
- rutas/  
- controladores/  

Una explicacion de estas carpetas es por ejemplo que app donde se encuentra todo.Las rutas contiene los archivos donde estas los endpoints con la responsabilidad de los
URLs, metodos HTTP y logica existente. Los controladores como dicta el nombre es la logica del negocio para procesar la informacion para devolver respuestas.
Motivo de la separacion es una limpieza del codigo ya que un codigo limpio facilita el mantenimiento a futuro y mas en proyecto como este que se hara actualizaciones para 
crecer para el proyecto.

Para la creacion de esta nueva parte fue crear las carpetas para iniciar con la logica inicial de cada recurso, iniciamos con estado_controlador y orden_controlador.
Para las rutas como su funcion es los endpoints con APIrouter estan estado_ruta y orden_ruta. la conexion de estos radita que las rutas importan la funcion desde el controlador
y ejecutan una peticion HTTP como se solicito. Por ultimo en el registro de las rutas en el main solo importamos routers y registramos para permitir que Fastapi reconozca los endpoints.
y
Endpoints implementados son Health check con el metodo GET, ruta /estado y proposito es verificar que el api funciona correctamente mostrando texto como "texto de prueba o algo asi". Para el segundo que Listar pedidos es metodo GET, ruta ordenes y funcion de obtener la lista de pedidos que creamos para visualizar. El ultimo es crear pedido con el metodo POST,
ruta controladores con el fin de crear un nuevo pedido con datos enviados en el cuerpo de la peticion.

Para comprobar esto solo tenemos que levantar el servidor y en el navegador cargar los URLs http://127.0.0.1:8000/health, http://127.0.0.1:8000/orders y http://127.0.0.1:8000/docs.
Algunas respuestas son:
Health check:
json
{
  "status": "ok",
  "message": "API funcionando correctamente"
}
Lista de pedidos:
[
  {
    "order_id": 1,
    "status": "pending",
    "total": 250.0
  },
  {
    "order_id": 2,
    "status": "delivered",
    "total": 430.0
  }
]
y crear pedido:
{
  "order_id": 3,
  "status": "pending",
  "total": 300.0,
  "data_received": {
    "user_id": 1,
    "items": [
      {
        "product_id": 2,
        "quantity": 1
      }
    ]
  }
}




