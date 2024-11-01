import baseDeDatos

def consulta_dos(conn):  #2. Lista completa de productos. 
    query = "SELECT * FROM productos;"
    cursor = conn.cursor()  
    cursor.execute(query)
    productos = cursor.fetchall()  
    for producto in productos:
        print(producto)
    cursor.close()  

def consulta_tres(conn):  #3. Clientes y sus direcciones.
    query = "SELECT clientes.idClientes, clientes.Nombre, clientes.Apellido, clientes.Correo, clientes.Teléfono, direcciones.Localidad, direcciones.Código_Postal, direcciones.Calle FROM clientes INNER JOIN direcciones ON clientes.idClientes = direcciones.Clientes_idClientes;"
    cursor = conn.cursor()  
    cursor.execute(query)
    productos = cursor.fetchall()  
    for producto in productos:
        print(producto)
    cursor.close()  

def consulta_cuatro(conn):  #4. Empleados activos y sus ventas.
    query = "SELECT e.Nombre AS Empleado, COUNT(v.idVentas) AS Ventas_Realizadas FROM empleado e LEFT JOIN ventas v ON e.idEmpleado = v.Empleado_idEmpleado WHERE e.Activo = 1 GROUP BY e.Nombre;"
    cursor = conn.cursor()  
    cursor.execute(query)
    productos = cursor.fetchall()  
    for producto in productos:
        print(producto)
    cursor.close()  

def consulta_cinco(conn):  #5. Resumen de ventas por área.
    query = "SELECT a.Nombre AS Area, COUNT(v.idVentas) AS Cantidad_Ventas, SUM(v.Total) AS Total_Ventas FROM ventas v JOIN empleado e ON v.Empleado_idEmpleado = e.idEmpleado JOIN area a ON e.Area_idArea = a.idArea GROUP BY a.Nombre;"
    cursor = conn.cursor()  
    cursor.execute(query)
    productos = cursor.fetchall()  
    for producto in productos:
        print(producto)
    cursor.close()  

def consulta_seis(conn):  #6. Satisfacción del cliente por empleado.
    query = "SELECT e.Nombre AS Empleado, AVG(sc.Puntos) AS Promedio_Puntos_Satisfaccion FROM satisfacción_cliente sc JOIN empleado e ON sc.Empleado_idEmpleado = e.idEmpleado GROUP BY e.Nombre;"
    cursor = conn.cursor()  
    cursor.execute(query)
    productos = cursor.fetchall()  
    for producto in productos:
        print(producto)
    cursor.close()  

def consulta_siete(conn):  #7. Ventas totales por empleado.
    query = "SELECT e.Nombre AS Empleado, SUM(v.Total) AS Total_Ventas FROM ventas v JOIN empleado e ON v.Empleado_idEmpleado = e.idEmpleado GROUP BY e.Nombre;"
    cursor = conn.cursor()
    cursor.execute(query)    
    resultados = cursor.fetchall()  
    for resultado in resultados:
        print(resultado)
    cursor.close()

def consulta_ocho(conn):  #8. Productos con el stock.
    query = "SELECT p.Nombre AS Producto, i.Stock_actual, i.Stock_minimo FROM inventario i JOIN productos p ON i.Productos_idProductos = p.idProductos;"
    cursor = conn.cursor()
    cursor.execute(query)    
    resultados = cursor.fetchall()  
    for resultado in resultados:
        print(resultado)
    cursor.close()

#---------------------------------------- CRUD EMPLEADO ---------------------------------------------------
def agregar_empleado(conn):
    nombre = input("Ingrese el nombre: ")  
    apellido = input("Ingrese el apellido: ")
    fecha = input("Digite la fecha de ingreso: ")
    activo = int(input("Ingrese si el empleado está activo con 1 o inactivo con 0: "))
    while activo > 1: 
        print("No ingresó 1 o 0.")
        activo = int(input("Ingrese si el empleado está activo con 1 o inactivo con 0: "))
    supervisor_celula = input("Ingrese la célula: ")
    area_idarea = input("Ingrese el id del área: ")
    
    query = "INSERT INTO empleado (Nombre, Apellido, Fecha_ingreso, Activo, Supervisor_Célula, Area_idArea) VALUES (%s, %s, %s, %s, %s, %s)" 
    values = (nombre, apellido, fecha, activo, supervisor_celula, area_idarea) 
    cursor = conn.cursor() 
    cursor.execute(query, values) 
    conn.commit() 
    cursor.close()
    
    print("Empleado registrado.")
    print(values)

def mostrar_empleados(conn):
    query = "SELECT * FROM empleado"
    cursor = conn.cursor()
    cursor.execute(query)
    empleados = cursor.fetchall()
    for empleado in empleados:
        print(empleado)
    cursor.close()

def modificar_empleado(conn):
    id = input("Ingrese el id del empleado: ")
    print("Ingrese qué desea cambiar: ")
    print("Nombre - Apellido - Fecha_ingreso - Activo - Supervisor_Célula")
    columna = input("Ingrese qué desea cambiar: ")
    cambio = input("Ingrese el cambio: ")
    
    columnas_permitidas = ["Nombre", "Apellido", "Fecha_ingreso", "Activo", "Supervisor_Célula"]
    if columna not in columnas_permitidas: 
        print("La columna ingresada no es válida.")
        return
    
    query = "UPDATE empleado SET {} = %s WHERE idEmpleado = %s".format(columna)
    values = (cambio, id)
    cursor = conn.cursor()
    cursor.execute(query, values) 
    conn.commit()
    cursor.close()

def eliminar_empleado(conn):
    id = int(input("Ingrese el id del empleado: "))
    query = "DELETE FROM empleado WHERE idEmpleado = %s"
    values = (id,)
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    cursor.close()