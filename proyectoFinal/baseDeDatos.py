import mysql.connector

HOST = "localhost"
BD = "ventas_satisfacción"

def obtener_conexion(user_base, pass_base):
    conn = mysql.connector.connect(
        host=HOST,
        user=user_base,
        password=pass_base,
        database=BD
    )
    return conn

def cerrar_conexion(conn):
    if conn.is_connected():
        conn.close()