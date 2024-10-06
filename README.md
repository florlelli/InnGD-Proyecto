# Gestión Integral de Ventas y Empleados (GIVE)
## Descripción
Este proyecto consiste en el desarrollo de una aplicación en Python que gestiona tanto las ventas como los empleados de una empresa. Además, se integra la administración del inventario, el registro de clientes y una función de evaluación de la satisfacción del cliente con el servicio recibido. El sistema utiliza una base de datos relacional y fue diseñado siguiendo el paradigma de programación orientada a objetos.
## Funcionalidades Principales
- Gestión de Ventas: Registro y consulta de todas las ventas realizadas, asociadas a clientes y empleados.
- Inventario: Control del stock de productos, con actualizaciones automáticas basadas en las ventas.
- Clientes: Registro y gestión de la información de los clientes.
- Empleados: Registro y seguimiento de empleados, con un sistema de estado (activo/inactivo) y evaluaciones de desempeño basadas en las puntuaciones de los clientes.
- Satisfacción del Cliente: Evaluación de la performance de los empleados por parte de los clientes, con la posibilidad de generar reportes para análisis.
## Estructura del Proyecto
El proyecto está dividido en diferentes módulos:
- Módulo de Autenticación: Permite registrar nuevos usuarios y autenticarse con nombre de usuario y contraseña.
- Módulo de Ventas: Gestiona las transacciones de venta y su relación con el inventario, los clientes y los empleados.
- Módulo de Aritmética: Realiza cálculos matemáticos básicos utilizados en el CAPTCHA y otras operaciones internas.
- Módulo de Inventario: Mantiene actualizada la cantidad de productos disponibles y alerta cuando el stock es bajo.
- Módulo de Clientes y Empleados: Registra y gestiona la información de los clientes y empleados, con seguimiento de su actividad y desempeño.
## Base de Datos
- **Estructura de la Base de Datos**: 
  La base de datos relacional en MySQL contiene las siguientes tablas:
  1. **Usuarios**: Registra la información de los usuarios.
  2. **Accesos**: Registra los accesos de los usuarios con fechas de ingreso y salida.
  
  Estas tablas están relacionadas a través de claves foráneas.

- **Consultas SQL**:
  Se utilizan las siguientes consultas SQL para la interacción con la base de datos:
  - `SELECT`, `INSERT`, `UPDATE`, `DELETE` para el CRUD de usuarios.
  - Consultas con `JOIN` para obtener los accesos de cada usuario.

