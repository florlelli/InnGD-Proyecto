import baseDeDatos

def consulta_uno(conn):  # 1. Obtenemos todos los datos de productos 
    query = "SELECT * FROM productos;"
    cursor = conn.cursor()  
    cursor.execute(query)
    productos = cursor.fetchall()  
    for producto in productos:
        print(producto)
    cursor.close()  

def consulta_dos(conn):  # Muestra los nombres de los clientes
    query = "SELECT Nombre FROM clientes;"
    cursor = conn.cursor()
    cursor.execute(query)
    nombres = cursor.fetchall()  
    for nombre in nombres:
        print(nombre)        
    cursor.close()

def consulta_tres(conn):  # 3. Insertar un nuevo producto
    query = """INSERT INTO productos (idProductos, Nombre, Descripción, Marca, Submarca, Precio, Proveedor_idProveedor, Categoria_idCategoria) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""
    values = (120, "Samsung Galaxy A05s 128 GB", None, "Samsung", "Samsung", 300499, 4141, 1)
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()  
    cursor.close()

def consulta_cuatro(conn):  # 4. Actualiza el precio de un producto
    query = "UPDATE productos SET Precio = 300000 WHERE idProductos = 10"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()  
    cursor.close()

def consulta_cinco(conn):  # 5. Elimina una dirección 
    query = "DELETE FROM direcciones WHERE idDirecciones = 2;"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()  
    cursor.close()

def consulta_seis(conn):  # 6. Muestra los productos con sus proveedores
    query = """SELECT Productos.idProductos, Productos.Nombre AS Producto, Productos.Precio, Proveedor.Nombre AS Proveedor 
               FROM Productos 
               INNER JOIN Proveedor ON Productos.Proveedor_idProveedor = Proveedor.idProveedor;"""
    cursor = conn.cursor()
    cursor.execute(query)    
    resultados = cursor.fetchall()  
    for resultado in resultados:
        print(resultado)
    cursor.close()

def consulta_siete(conn):  # 7. Muestra los clientes y sus direcciones 
    query = """SELECT clientes.idClientes, clientes.Nombre, clientes.Apellido, clientes.Correo, clientes.Teléfono, 
               direcciones.Localidad, direcciones.Código_Postal, direcciones.Calle 
               FROM Clientes 
               INNER JOIN direcciones ON clientes.idClientes = direcciones.Clientes_idClientes;"""
    cursor = conn.cursor()
    cursor.execute(query)    
    resultados = cursor.fetchall()  
    for resultado in resultados:
        print(resultado)
    cursor.close()