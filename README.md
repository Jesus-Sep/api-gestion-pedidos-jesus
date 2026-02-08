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

En el apartadi de tecnologías elegidas tenemos la sugerida por el profesor FastAPI en Python con Uvicorn, tentativamente a PostgreSQL.


