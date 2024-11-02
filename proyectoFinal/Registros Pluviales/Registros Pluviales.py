import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Configurar la ruta de archivos #
path = os.path.dirname(os.path.abspath("__file__")) + "/"

# Crear directorio para los datos analizados si no existe #
datos_dir = path + "datosAnalizados/"
if not os.path.exists(datos_dir):
    os.makedirs(datos_dir)

# Solicitar el año y validacion de rango de años #
try:
    año = int(input("Ingresar el año a analizar: "))
    if año < 1990 or año > 2025:  
        raise ValueError("El año debe estar entre 1990 y 2025")
    archivo = f"{datos_dir}registroPluvial{año}.csv"
except ValueError as e:
    print("Por favor ingrese un año válido")
    exit()

# Verificar si existe el archivo #
if os.path.exists(f"registroPluvial{año}.csv"):
    df_precipitaciones = pd.read_csv(f"registroPluvial{año}.csv")
else:
    # Generar datos aleatorios # 
    # Considerando años no bisiestos #
    np.random.seed(42)
    precipitaciones = np.round(np.random.rand(372) * 100, 2)
    precipitaciones = precipitaciones.reshape(31, 12)
    
    # Crear DataFrame #
    columnas = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    df_precipitaciones = pd.DataFrame(precipitaciones, columns=columnas)
    
    # Guardar archivo CSV # 
    df_precipitaciones.to_csv(f"registroPluvial{año}.csv", index=False)

# 1. Estadisticas anuales #
print(f"\nEstadísticas del año {año}:")
print(f"Precipitación máxima: {df_precipitaciones.values.max():.2f} mm")
print(f"Precipitación mínima: {df_precipitaciones.values.min():.2f} mm")
print(f"Precipitación promedio: {df_precipitaciones.values.mean():.2f} mm")

# Graficos anuales solo los guarda#
#  Grafico de barras anual #
plt.figure(figsize=(12, 6))
df_precipitaciones.mean().plot(kind='bar')
plt.title(f'Precipitación promedio mensual - {año}')
plt.xlabel('Mes')
plt.ylabel('Precipitación (mm)')
plt.tight_layout()
plt.savefig(f"{datos_dir}barras_anual_{año}.png")
plt.close()

#  Grafico de dispersion #
plt.figure(figsize=(12, 6))
for mes in range(12):
    plt.scatter([mes+1]*31, range(1,32), c=df_precipitaciones.iloc[:,mes], cmap='Blues')
plt.colorbar(label='Precipitación (mm)')
plt.title(f'Distribución de lluvias - {año}')
plt.xlabel('Mes')
plt.ylabel('Día')
plt.tight_layout()
plt.savefig(f"{datos_dir}dispersion_{año}.png")
plt.close()

# Grafico circular anual #
plt.figure(figsize=(10, 10))
plt.pie(df_precipitaciones.mean(), labels=df_precipitaciones.columns, autopct='%1.1f%%')
plt.title(f'Distribución porcentual de lluvias por mes - {año}')
plt.savefig(f"{datos_dir}circular_anual_{año}.png")
plt.close()

# 2. Analisis mensual #
try:
    # Solicitar y corroborar el mes #
    mes = int(input("\nIngrese el mes para analizar (1-12): "))
    if mes < 1 or mes > 12:
        raise ValueError("El mes debe estar entre 1 y 12")
    
    mes_idx = mes - 1
    mes_nombre = df_precipitaciones.columns[mes_idx]
    
    #  Mostrar registros del mes # 
    print(f"\nRegistros de {mes_nombre}:")
    print("Día    Precipitación (mm)")
    print("-" * 25)
    datos_mes = df_precipitaciones[mes_nombre].copy()  # Crear una copia de los datos del mes #
    for dia, valor in enumerate(datos_mes, 1):
        print(f"{dia:2d}     {valor:6.2f}")

    # Estadisticas mensuales #
    print(f"\nEstadisticas de {mes_nombre}:")
    print(f"Precipitación máxima: {datos_mes.max():.2f} mm")
    print(f"Precipitación mínima: {datos_mes.min():.2f} mm")
    print(f"Precipitación promedio: {datos_mes.mean():.2f} mm")

    # Grafico circular mensual #
    # Muestra el grafico en pantalla y lo guarda #
    plt.figure(figsize=(10, 10))
    
    # Filtrar valores mayores que 0 para el grafico #
    datos_grafico = datos_mes[datos_mes > 0]
    if len(datos_grafico) > 0:
        plt.pie(datos_grafico, 
                labels=[f'Día {i+1}' for i in datos_grafico.index], 
                autopct='%1.1f%%')
        plt.title(f'Distribución porcentual de lluvias - {mes_nombre} {año}')
        plt.savefig(f"{datos_dir}circular_mensual_{mes_nombre}_{año}.png")
        plt.show()
        plt.close()
    else:
        print(f"No hay datos de precipitación mayores que 0 para {mes_nombre}")

except ValueError as e:
    print(f"Error: {e}")
    print("Por favor, ingrese un número válido entre 1 y 12")
except Exception as e:
    print(f"Error inesperado: {e}")


