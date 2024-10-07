-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema ventas_satisfacción
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema ventas_satisfacción
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ventas_satisfacción` DEFAULT CHARACTER SET utf8mb3 ;
USE `ventas_satisfacción` ;

-- -----------------------------------------------------
-- Table `ventas_satisfacción`.`area`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ventas_satisfacción`.`area` (
  `idArea` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idArea`),
  UNIQUE INDEX `idArea_UNIQUE` (`idArea` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ventas_satisfacción`.`categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ventas_satisfacción`.`categoria` (
  `idCategoria` INT NOT NULL,
  `Tipo` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCategoria`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ventas_satisfacción`.`clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ventas_satisfacción`.`clientes` (
  `idClientes` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  `Apellido` VARCHAR(45) NOT NULL,
  `Correo` VARCHAR(45) NULL DEFAULT NULL,
  `Teléfono` VARCHAR(20) NULL DEFAULT NULL,
  PRIMARY KEY (`idClientes`))
ENGINE = InnoDB
AUTO_INCREMENT = 13
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ventas_satisfacción`.`proveedor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ventas_satisfacción`.`proveedor` (
  `idProveedor` INT NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `Dirección` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idProveedor`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ventas_satisfacción`.`productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ventas_satisfacción`.`productos` (
  `idProductos` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  `Descripción` LONGTEXT NULL DEFAULT NULL,
  `Precio` FLOAT NOT NULL,
  `Marca` VARCHAR(45) NOT NULL,
  `Submarca` VARCHAR(45) NOT NULL,
  `Presentación` VARCHAR(145) NULL DEFAULT NULL,
  `Proveedor_idProveedor` INT NOT NULL,
  `Categoria_idCategoria` INT NOT NULL,
  PRIMARY KEY (`idProductos`),
  INDEX `fk_Productos_Proveedor1_idx` (`Proveedor_idProveedor` ASC) VISIBLE,
  INDEX `fk_Productos_Categoria1_idx` (`Categoria_idCategoria` ASC) VISIBLE,
  CONSTRAINT `fk_Productos_Categoria1`
    FOREIGN KEY (`Categoria_idCategoria`)
    REFERENCES `ventas_satisfacción`.`categoria` (`idCategoria`),
  CONSTRAINT `fk_Productos_Proveedor1`
    FOREIGN KEY (`Proveedor_idProveedor`)
    REFERENCES `ventas_satisfacción`.`proveedor` (`idProveedor`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 18
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ventas_satisfacción`.`supervisor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ventas_satisfacción`.`supervisor` (
  `idSupervisor` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  `Apellido` VARCHAR(45) NOT NULL,
  `Célula` INT NOT NULL,
  PRIMARY KEY (`idSupervisor`),
  UNIQUE INDEX `Célula_UNIQUE` (`Célula` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 9
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ventas_satisfacción`.`empleado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ventas_satisfacción`.`empleado` (
  `idEmpleado` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  `Apellido` VARCHAR(45) NOT NULL,
  `Fecha_ingreso` DATE NOT NULL,
  `Activo` TINYINT(1) NOT NULL,
  `Supervisor_Célula` INT NOT NULL,
  `Area_idArea` INT NOT NULL,
  PRIMARY KEY (`idEmpleado`),
  INDEX `celula_idx` (`Supervisor_Célula` ASC) VISIBLE,
  INDEX `fk_Empleado_Area1_idx` (`Area_idArea` ASC) VISIBLE,
  CONSTRAINT `fk_Empleado_Area1`
    FOREIGN KEY (`Area_idArea`)
    REFERENCES `ventas_satisfacción`.`area` (`idArea`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `Supervisor_Célula`
    FOREIGN KEY (`Supervisor_Célula`)
    REFERENCES `ventas_satisfacción`.`supervisor` (`Célula`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ventas_satisfacción`.`métodopago`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ventas_satisfacción`.`métodopago` (
  `idMétodoPago` INT NOT NULL AUTO_INCREMENT,
  `Tipo` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idMétodoPago`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ventas_satisfacción`.`tipo_venta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ventas_satisfacción`.`tipo_venta` (
  `idTipo_venta` INT NOT NULL,
  `Tipo` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idTipo_venta`),
  UNIQUE INDEX `Tipo_UNIQUE` (`Tipo` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ventas_satisfacción`.`ventas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ventas_satisfacción`.`ventas` (
  `idVentas` INT NOT NULL,
  `Fecha` DATE NOT NULL,
  `Total` FLOAT NOT NULL,
  `Nro_factura` INT NOT NULL AUTO_INCREMENT,
  `Empleado_idEmpleado` INT NOT NULL,
  `Clientes_idClientes` INT NOT NULL,
  `MétodoPago_idMétodoPago` INT NOT NULL,
  `Tipo_venta_idTipo_venta` INT NOT NULL,
  PRIMARY KEY (`idVentas`),
  UNIQUE INDEX `Nro_factura_UNIQUE` (`Nro_factura` ASC) VISIBLE,
  INDEX `fk_VENTAS_EMPLEADO1_idx` (`Empleado_idEmpleado` ASC) VISIBLE,
  INDEX `fk_Ventas_Clientes1_idx` (`Clientes_idClientes` ASC) VISIBLE,
  INDEX `fk_Ventas_MétodoPago1_idx` (`MétodoPago_idMétodoPago` ASC) VISIBLE,
  INDEX `fk_Ventas_Tipo_venta1_idx` (`Tipo_venta_idTipo_venta` ASC) INVISIBLE,
  INDEX `fecha` (`Fecha` ASC) INVISIBLE,
  CONSTRAINT `fk_Ventas_Clientes1`
    FOREIGN KEY (`Clientes_idClientes`)
    REFERENCES `ventas_satisfacción`.`clientes` (`idClientes`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_VENTAS_EMPLEADO1`
    FOREIGN KEY (`Empleado_idEmpleado`)
    REFERENCES `ventas_satisfacción`.`empleado` (`idEmpleado`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Ventas_MétodoPago1`
    FOREIGN KEY (`MétodoPago_idMétodoPago`)
    REFERENCES `ventas_satisfacción`.`métodopago` (`idMétodoPago`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Ventas_Tipo_venta1`
    FOREIGN KEY (`Tipo_venta_idTipo_venta`)
    REFERENCES `ventas_satisfacción`.`tipo_venta` (`idTipo_venta`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ventas_satisfacción`.`detalle_ventas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ventas_satisfacción`.`detalle_ventas` (
  `Ventas_idVentas` INT NOT NULL,
  `Productos_idProductos` INT NOT NULL,
  `Precio` FLOAT NOT NULL,
  `Cantidad` INT NOT NULL,
  `Descuento` FLOAT NULL DEFAULT NULL,
  `Nro_factura` INT NOT NULL,
  `CUIT` INT NULL DEFAULT NULL,
  PRIMARY KEY (`Ventas_idVentas`, `Productos_idProductos`),
  INDEX `fk_VENTAS_has_PRODUCTOS1_PRODUCTOS1_idx` (`Productos_idProductos` ASC) VISIBLE,
  INDEX `fk_VENTAS_has_PRODUCTOS1_VENTAS1_idx` (`Ventas_idVentas` ASC) VISIBLE,
  CONSTRAINT `fk_VENTAS_has_PRODUCTOS1_PRODUCTOS1`
    FOREIGN KEY (`Productos_idProductos`)
    REFERENCES `ventas_satisfacción`.`productos` (`idProductos`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_VENTAS_has_PRODUCTOS1_VENTAS1`
    FOREIGN KEY (`Ventas_idVentas`)
    REFERENCES `ventas_satisfacción`.`ventas` (`idVentas`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ventas_satisfacción`.`direcciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ventas_satisfacción`.`direcciones` (
  `idDirecciones` INT NOT NULL AUTO_INCREMENT,
  `Localidad` VARCHAR(45) NOT NULL,
  `Código_Postal` INT NOT NULL,
  `Calle` VARCHAR(45) NOT NULL,
  `Clientes_idClientes` INT NOT NULL,
  PRIMARY KEY (`idDirecciones`, `Clientes_idClientes`),
  INDEX `fk_Direcciones_Clientes1_idx` (`Clientes_idClientes` ASC) VISIBLE,
  CONSTRAINT `fk_Direcciones_Clientes1`
    FOREIGN KEY (`Clientes_idClientes`)
    REFERENCES `ventas_satisfacción`.`clientes` (`idClientes`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ventas_satisfacción`.`inventario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ventas_satisfacción`.`inventario` (
  `idInventario` INT NOT NULL AUTO_INCREMENT,
  `Stock_actual` INT NOT NULL,
  `Stock_minimo` INT NOT NULL,
  `Stock_maximo` INT NOT NULL,
  `Productos_idProductos` INT NOT NULL,
  PRIMARY KEY (`idInventario`),
  INDEX `idProductos_idx` (`Productos_idProductos` ASC) VISIBLE,
  CONSTRAINT `idProductos`
    FOREIGN KEY (`Productos_idProductos`)
    REFERENCES `ventas_satisfacción`.`productos` (`idProductos`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `ventas_satisfacción`.`satisfacción_cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ventas_satisfacción`.`satisfacción_cliente` (
  `idSatisfacción_Cliente` INT NOT NULL AUTO_INCREMENT,
  `Puntos` INT NOT NULL,
  `Clientes_idClientes` INT NOT NULL,
  `Empleado_idEmpleado` INT NOT NULL,
  `Ventas_idVentas` INT NOT NULL,
  PRIMARY KEY (`idSatisfacción_Cliente`, `Ventas_idVentas`),
  INDEX `fk_Clientes_has_Empleado_Empleado1_idx` (`Empleado_idEmpleado` ASC) VISIBLE,
  INDEX `fk_Clientes_has_Empleado_Clientes1_idx` (`Clientes_idClientes` ASC) VISIBLE,
  INDEX `fk_Satisfacción_Cliente_Ventas1_idx` (`Ventas_idVentas` ASC) VISIBLE,
  CONSTRAINT `fk_Clientes_has_Empleado_Clientes1`
    FOREIGN KEY (`Clientes_idClientes`)
    REFERENCES `ventas_satisfacción`.`clientes` (`idClientes`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Clientes_has_Empleado_Empleado1`
    FOREIGN KEY (`Empleado_idEmpleado`)
    REFERENCES `ventas_satisfacción`.`empleado` (`idEmpleado`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Satisfacción_Cliente_Ventas1`
    FOREIGN KEY (`Ventas_idVentas`)
    REFERENCES `ventas_satisfacción`.`ventas` (`idVentas`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 19
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
