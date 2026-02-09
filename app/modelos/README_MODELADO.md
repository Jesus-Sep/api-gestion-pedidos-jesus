Modelado del Sistema – Gestión de Pedidos

El sistema de Gestión de Pedidos es para que un negocio registrar y administrar pedidos realizados por usuarios, así como los productos incluidos en cada pedido y su estado actual.  
El dominio se centra en la relación entre usuarios, pedidos y productos, asegurando que cada pedido tenga un responsable, un conjunto de productos asociados y un estado que represente su avance dentro del proceso operativo.


se crearon las siguientes modelos User que Representa a las personas que interactúan con el sistema y realizan pedidos.Role Permite clasificar a los usuarios según su rol,Order entidad central del negocio, representa un pedido realizado por un usuario. OrderItem entidad de detalle que relaciona pedidos con productos, permitiendo manejar cantidades y precios unitarios. Producto representa los productos disponibles para ser incluidos en los pedidos. OrderStatus catálogo de estados posibles de un pedido 


Las relaciones se estableció una relación  entre usuario y orden, ya que un usuario puede tener múltiples pedidos.
Se implementó una relación orden y producto, resuelta mediante la entidad orden_item, lo cual permite registrar cantidades y precios por producto dentro de un pedido.
POr ultimo para Cada orden se asocia a un único orden_status.


Los campos clave como correos electrónicos y nombres de estados se definieron como unicos para garantizar integridad. se incluyeron campos de auditoría  en las entidades principales para dar seguimiento a los cambios.

Cosas a considerar un usuario siempre pertenece a un solo rol, un pedido pertenece a un solo usuario, un pedido siempre tiene al menos un estado asignado, los productos pueden participar en múltiples pedidos, el precio del producto se almacena en el detalle del pedido para preservar el historial.


Para el codigo los modelos del dominio fueron implementados en la capa de modelos utilizando SQLAlchemy. Cada entidad del dominio se representa como una clase ORM. Se definieron claves primarias, claves foráneas y relaciones entre modelos. 