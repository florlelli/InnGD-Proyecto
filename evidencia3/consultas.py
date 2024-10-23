import baseDeDatos
def consulta_uno(): #1. Obtenemos todos los datos de productos 
    query = "SELECT * FROM productos;"
    baseDeDatos.cursor.execute(query)
    productos = baseDeDatos.cursor.fetchall()  
    for productos in productos:
        print(productos)

def consulta_dos():  # Muestra los nombres de los clientes
    query = "SELECT Nombre FROM clientes;"
    baseDeDatos.cursor.execute(query)
    ventas = baseDeDatos.cursor.fetchall()  
    for ventas in ventas:
        print(ventas)        

def consulta_tres(): #3. Insertar un nuevo producto
    query = """INSERT INTO productos (idProductos, Nombre, Descripción, Marca, Submarca, Precio, Proveedor_idProveedor, Categoria_idCategoria) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""
    values = (120, "Samsung Galaxy A05s 128 GB", None, "Samsung", "Samsung", 300499, 4141, 1)
    baseDeDatos.cursor.execute(query, values)
   

def consulta_cuatro(): #4. Actualiza el precio de un producto
    query = "UPDATE productos SET Precio = 300000 WHERE idProducto = 10"
    baseDeDatos.cursor.execute(query)
  

def consulta_cinco(): #5. Elimina una dirección 
    query = "DELETE FROM direcciones WHERE idDirecciones = 2;"
    baseDeDatos.cursor.execute(query)    
    ventas = baseDeDatos.cursor.fetchall()  
  

#6 INNER JOIN
def consulta_seis():  #Muestra los productos con sus proveedores
    query = "SELECT Productos.idProductos, Productos.Nombre AS Producto, Productos.Precio, Proveedor.Nombre AS Proveedor FROM Productos INNER JOIN Proveedor ON Productos.Proveedor_idProveedor = Proveedor.idProveedor;"
    baseDeDatos.cursor.execute(query)    
    ventas = baseDeDatos.cursor.fetchall()  
    for ventas in ventas:
        print(ventas) 

#7 INNER JOIN
def consulta_siete(): #Muestra los clientes y sus direcciones 
    query = "SELECT clientes.idClientes, clientes.Nombre, clientes.Apellido, clientes.Correo, clientes.Teléfono, direcciones.Localidad, direcciones.Código_Postal, direcciones.Calle FROM Clientes INNER JOIN direcciones ON clientes.idClientes = direcciones.Clientes_idClientes; " 
    baseDeDatos.cursor.execute(query)    
    ventas = baseDeDatos.cursor.fetchall()  
    for ventas in ventas:
        print(ventas) 