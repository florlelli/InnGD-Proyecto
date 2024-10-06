INSERT INTO productos (idProductos, Nombre, Descripción, Marca, Submarca, Precio, Proveedor_idProveedor, Categoria_idCategoria)
VALUES ("010", "Moto E22 64 GB", NULL, "Motorola", "Motorola", 175999, "4143", "1"), ("011", "Moto G23 128 GB", NULL, "Motorola", "Motorola", 247999, "4143", "1"),
("012", "Samsung Galaxy A04 64 GB", "Pantalla Infinity-V de 6,5 pulgadas.", "Samsung", "Samsung", 202499, "4142", "1"),
("013", "Samsung Galaxy A34 5G 128 GB", NULL, "Samsung", "Samsung",  449999, "4142", "1"),
("014", "Moto G41 128 GB", "Pantalla Full HD+ de 6,5 pulgadas.", "Motorola", "Samsung",  279999,"4143", "1"),
("015", "Samsung Galaxy A15 128GB", NULL, "Samsung", "Samsung", 399999, "4142", "1"),
("016", "Samsung Galaxy A54 5G 256GB", "Características de última generación.", "Samsung", "Samsung", 999999, "4142", "1"),
("017", "Moto G13 128GB", NULL, "Motorola" , "Motorola", 269999, "4143", "1");

INSERT INTO proveedor (idProveedor, Nombre, Dirección)
VALUES ("4141", "Tiendacel", "San Martin 234"), ("4142", "SamsungArg", "Duarte Quirós 1400"), ("4143", "MorolaArg", "Velez Sarfield 430");

INSERT INTO categoria (idCategoria, Tipo)  VALUES ( "1" , "Celulares"), ("2", "Computadoras"), ("3", "Perifericos");

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


INSERT INTO empleado (Nombre, Apellido, Fecha_ingreso, Supervisor_Célula, Activo)
VALUES ("Eduardo", "Lopez", "2024-01-01", 2, 1), 
("Lucia", "Acuña", "2020-01-02", 3, 1),
("Rocio", "Pacheco", "2019-05-08", 1, 1),
("Diego", "Zapata", "2022-09-01", 1, 1), 
("Jorge", "Suarez", "2024-06-05", 3, 0),
("Andrea", "Romero", "2019-05-08", 2, 0);


INSERT INTO métodopago (Tipo)
VALUES ("Tarjeta de Crédito"),
("Tarjeta de Débito"),
("Transferencia"),
("Efectivo");

INSERT INTO supervisor (Nombre, Apellido, Célula)
VALUES ("Verónica", "Aguirre", 1),
("David", "Arias", 2),
("Maria", "Escalante", 3),
("Fernando", "Perez", 4);
