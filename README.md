# Gestión Integral de Ventas y Empleados (GIVE)
## Descripción
Este proyecto consiste en el desarrollo de una aplicación en Python que gestiona tanto las ventas como los empleados de una empresa. Además, se integra la administración del inventario, el registro de clientes y una función de evaluación de la satisfacción del cliente con el servicio recibido. El sistema utiliza una base de datos relacional y fue diseñado siguiendo el paradigma de programación orientada a objetos.
## Funcionalidades Principales
- Gestión de Ventas: Registro y consulta de todas las ventas realizadas, asociadas a clientes y empleados.
- Inventario: Control del stock de productos, con actualizaciones automáticas basadas en las ventas.
- Clientes: Registro y gestión de la información de los clientes.
- Empleados: Registro y seguimiento de empleados, con un sistema de estado (activo/inactivo) y evaluaciones de desempeño basadas en las puntuaciones de los clientes.
- Satisfacción del Cliente: Evaluación de la performance de los empleados por parte de los clientes, con la posibilidad de generar reportes para análisis.
## Instrucciones de Instalación y Ejecución
1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/usuario/repositorio.git
   ```
2. Asegúrate de tener Python instalado. No necesitas instalar paquetes externos para ejecutar este proyecto.
3. Ejecuta el archivo principal del programa:
   ```bash
   python main.py
   ```
## Funcionalidades de la Segunda Parte
- **Gestión de Usuarios**: 
  - El programa permite agregar, modificar, eliminar y buscar usuarios.
  - Los usuarios se almacenan en un archivo binario llamado `usuarios.ispc`.

- **Registro de Accesos**:
  - Cada vez que un usuario inicia sesión correctamente, se registra un acceso con la fecha de ingreso y salida en el archivo `accesos.ispc`.
  - Los intentos fallidos se registran en el archivo de texto `logs.txt`.
## Base de Datos
- **Consultas SQL**:
  Se utilizan las siguientes consultas SQL para la interacción con la base de datos:
  - `SELECT`, `INSERT`, `UPDATE`, `DELETE` para el CRUD de usuarios.
  - Consultas con `JOIN` para obtener los accesos de cada usuario.




