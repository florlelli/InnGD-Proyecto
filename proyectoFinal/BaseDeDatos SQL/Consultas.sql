#1. Obtenemos todos los datos de productos
SELECT * FROM productos;

#2.Muestra los nombres de los clientes
SELECT Nombre FROM clientes;

#3. Insertar un nuevo producto
 INSERT INTO productos (idProductos, Nombre, Descripción, Marca, Submarca, Precio, Proveedor_idProveedor, Categoria_idCategoria) VALUES ("Samsung Galaxy A05s 128 GB", "NULL", "Samsung", "Samsung",300499) ;

#4. Actualiza el precio de un producto
UPDATE productos 
SET Precio = 300000 
WHERE idProducto = 10;

#5. Elimina una dirección 
DELETE FROM direcciones  
WHERE idDirecciones = 2;

#6 INNER JOIN
 #Muestra los productos con sus proveedores
SELECT Productos.idProductos, Productos.Nombre AS Producto, Productos.Precio, Proveedor.Nombre AS Proveedor
FROM Productos
INNER JOIN Proveedor ON Productos.Proveedor_idProveedor = Proveedor.idProveedor;


#7 INNER JOIN 
#Muestra los clientes y sus direcciones 
SELECT clientes.idClientes, clientes.Nombre, clientes.Apellido, clientes.Correo, clientes.Teléfono, direcciones.Localidad, direcciones.Código_Postal, direcciones.Calle
FROM clientes
INNER JOIN direcciones ON clientes.idClientes = direcciones.Clientes_idClientes; 