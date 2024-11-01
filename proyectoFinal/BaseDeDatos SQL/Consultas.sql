#2. Lista completa de productos.
SELECT * FROM productos;

#3. Clientes y sus direcciones.
SELECT clientes.idClientes, clientes.Nombre, clientes.Apellido, clientes.Correo, clientes.Teléfono, direcciones.Localidad, direcciones.Código_Postal, direcciones.Calle
FROM clientes
INNER JOIN direcciones ON clientes.idClientes = direcciones.Clientes_idClientes; 

#4. Empleados activos y sus ventas.
SELECT e.Nombre AS Empleado, COUNT(v.idVentas) AS Ventas_Realizadas
FROM empleado e
LEFT JOIN ventas v ON e.idEmpleado = v.Empleado_idEmpleado
WHERE e.Activo = 1
GROUP BY e.Nombre;
    
#5. Resumen de ventas por área.
SELECT a.Nombre AS Area, COUNT(v.idVentas) AS Cantidad_Ventas, SUM(v.Total) AS Total_Ventas
FROM ventas v
JOIN empleado e ON v.Empleado_idEmpleado = e.idEmpleado
JOIN area a ON e.Area_idArea = a.idArea
GROUP BY a.Nombre;

#6. Satisfacción del cliente por empleado.
SELECT e.Nombre AS Empleado, AVG(sc.Puntos) AS Promedio_Puntos_Satisfaccion
FROM satisfacción_cliente sc
JOIN empleado e ON sc.Empleado_idEmpleado = e.idEmpleado
GROUP BY e.Nombre;

#7. Ventas totales por empleado.
SELECT e.Nombre AS Empleado, SUM(v.Total) AS Total_Ventas
FROM ventas v
JOIN empleado e ON v.Empleado_idEmpleado = e.idEmpleado
GROUP BY e.Nombre;

#8. Productos con el stock. 
SELECT p.Nombre AS Producto, i.Stock_actual, i.Stock_minimo
FROM inventario i
JOIN productos p ON i.Productos_idProductos = p.idProductos;
