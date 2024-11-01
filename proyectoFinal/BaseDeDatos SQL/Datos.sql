INSERT INTO categoria (idCategoria, Tipo)  VALUES ( "1" , "Celulares"), ("2", "Computadoras"), ("3", "Perifericos");

INSERT INTO proveedor (idProveedor, Nombre, Dirección)
VALUES ("4141", "Tiendacel", "San Martin 234"), ("4142", "SamsungArg", "Duarte Quirós 1400"), ("4143", "MorolaArg", "Velez Sarfield 430");

INSERT INTO productos (idProductos, Nombre, Descripción, Marca, Submarca, Precio, Proveedor_idProveedor, Categoria_idCategoria)
VALUES ("010", "Moto E22 64 GB", NULL, "Motorola", "Motorola", 175999, "4143", "1"), ("011", "Moto G23 128 GB", NULL, "Motorola", "Motorola", 247999, "4143", "1"),
("012", "Samsung Galaxy A04 64 GB", "Pantalla Infinity-V de 6,5 pulgadas.", "Samsung", "Samsung", 202499, "4142", "1"),
("013", "Samsung Galaxy A34 5G 128 GB", NULL, "Samsung", "Samsung",  449999, "4142", "1"),
("014", "Moto G41 128 GB", "Pantalla Full HD+ de 6,5 pulgadas.", "Motorola", "Samsung",  279999,"4143", "1"),
("015", "Samsung Galaxy A15 128GB", NULL, "Samsung", "Samsung", 399999, "4142", "1"),
("016", "Samsung Galaxy A54 5G 256GB", "Características de última generación.", "Samsung", "Samsung", 999999, "4142", "1"),
("017", "Moto G13 128GB", NULL, "Motorola" , "Motorola", 269999, "4143", "1");

INSERT INTO clientes (idClientes, Nombre, Apellido, Correo, Teléfono)
VALUES ("1", "Olivia", "Gonzalez", "olivia@ejemplo.com", NULL), 
("2", "Agustina", "Molina", "agusmolina@ejemplo.com", 22211),
("3", "Juan", "Perez", "juan@ejemplo.com", NULL),
("4", "Victoria","Martinez", "victoria@ejemplo.com", 101010),
("5", "Santiago", "Cepeda", "santiago@ejemplo.com", 555000),
("6", "Pedro", "Garcia", "pedro@ejemplo.com", NULL);

INSERT INTO direcciones (idDirecciones, Localidad, Código_Postal, Calle, Clientes_idClientes)
VALUES ("1", "Córdoba", 5030, "Belgrano 1012", 1),
("2", "Córdoba", 5000, "Lima 800", 2),
("3", "Bell Ville", 2550, "General Paz 745", 3),
("4", "Córdoba", 5002, "Sam Martin 300", 4),
("5", "Córdoba", 5002, "Caseros 4510", 5),
("6", "Villa María", 5900, "9 de julio 1550", 6);

INSERT INTO area (idArea, Nombre) VALUE ("1", "Ventas Salon"), ("2", "Ventas Online"), ("3", "Caja"), ("4", "Deposito"), ("5", "Embalaje");

INSERT INTO supervisor (Nombre, Apellido, Célula)
VALUES ("Verónica", "Aguirre", 1),
("David", "Arias", 2),
("Maria", "Escalante", 3),
("Fernando", "Perez", 4);

INSERT INTO empleado (Nombre, Apellido, Fecha_ingreso, Supervisor_Célula, Activo, Area_idArea)
VALUES ("Eduardo", "Lopez", "2024-01-01", 2, 1, 1), 
("Lucia", "Acuña", "2020-01-02", 3, 1, 2),
("Rocio", "Pacheco", "2019-05-08", 1, 1, 3),
("Diego", "Zapata", "2022-09-01", 1, 1, 4), 
("Jorge", "Suarez", "2024-06-05", 3, 0, 1),
("Andrea", "Romero", "2019-05-08", 2, 0, 2);

INSERT INTO métodopago (idMétodoPago, Tipo)
VALUES ("5", "Tarjeta de Crédito"),
("6", "Tarjeta de Débito"),
("7", "Transferencia"),
("8", "Efectivo");

INSERT INTO tipo_venta (idTipo_venta, Tipo) VALUES
(1, 'Telefónica'),
(2, 'Online'),
(3, 'Prescencial');

INSERT INTO ventas (idVentas, Fecha, Total, Empleado_idEmpleado, Clientes_idClientes, MétodoPago_idMétodoPago, Tipo_venta_idTipo_venta) VALUES
(1, '2024-10-01', 175999, 1, 1, 5, 1),
(2, '2024-10-01', 247999, 2, 2, 6, 1),
(3, '2024-10-02', 202499, 3, 3, 5, 2),
(4, '2024-10-03', 399999, 4, 4, 7, 3),
(5, '2024-08-03', 999999, 5, 5, 5, 2),
(6, '2024-09-04', 279999, 6, 6, 8, 1),
(7, '2024-09-05', 449999, 1, 1, 6, 2),
(8, '2024-10-02', 150000, 2, 2, 5, 3),
(9, '2024-10-04', 300000, 3, 3, 6, 3),
(10, '2024-10-05', 450000, 1, 4, 5, 2),
(11, '2024-10-06', 220000, 2, 5, 6, 1),
(12, '2024-10-07', 120000, 4, 6, 5, 3),
(13, '2024-10-08', 600000, 5, 1, 6, 2),
(14, '2024-10-09', 350000, 1, 2, 5, 2);

INSERT INTO detalle_ventas (Ventas_idVentas, Productos_idProductos, Precio, Cantidad, Descuento, Nro_factura, CUIT) VALUES
(1, '010', 175999, 1, NULL, 1001, NULL),
(2, '011', 247999, 1, NULL, 1002, NULL),
(3, '012', 202499, 1, NULL, 1003, NULL),
(4, '013', 449999, 1, 0, 1004, NULL),
(5, '016', 999999, 1, NULL, 1005, NULL),
(6, '014', 279999, 1, 5, 1006, NULL),
(7, '015', 399999, 1, NULL, 1007, NULL),
(8, '010', 150000, 1, NULL, 1008, NULL),
(9, '012', 300000, 1, 10, 1009, NULL),
(10, '013', 450000, 1, 5, 1010, NULL),
(11, '014', 220000, 1, NULL, 1011, NULL),
(12, '015', 120000, 1, 0, 1012, NULL),
(13, '016', 600000, 1, NULL, 1013, NULL),
(14, '011', 350000, 1, NULL, 1014, NULL);

INSERT INTO inventario (Stock_actual, Stock_minimo, Stock_maximo, Productos_idProductos) VALUES
(100, 10, 200, '010'),
(50, 5, 100, '011'),
(75, 10, 150, '012'),
(30, 5, 60, '013'),
(10, 2, 20, '014'),
(25, 3, 50, '015'),
(15, 2, 30, '016'),
(80, 10, 150, '010'),
(60, 5, 100, '011'),
(50, 10, 150, '012'),
(25, 5, 60, '013'),
(15, 2, 30, '014'),
(40, 3, 50, '015'),
(20, 2, 30, '016');

INSERT INTO satisfacción_cliente (Puntos, Clientes_idClientes, Empleado_idEmpleado, Ventas_idVentas) VALUES
(5, 1, 1, 1),
(4, 2, 2, 2),
(3, 3, 3, 3),
(2, 4, 4, 4),
(5, 5, 5, 5),
(4, 6, 6, 6),
(3, 1, 1, 7),
(4, 2, 2, 8),
(5, 3, 3, 9),
(3, 4, 1, 10),
(2, 5, 2, 11),
(5, 6, 4, 12),
(4, 1, 5, 13),
(3, 2, 1, 14);
