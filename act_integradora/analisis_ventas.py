# ============================================================
# ACTIVIDAD INTEGRADORA
# VISUALIZACIÓN DE INFORMACIÓN CON PYTHON
# ============================================================

# Permite leer archivos CSV, organizar tablas, filtrar,
# agrupar y realizar operaciones matemáticas.
import pandas as pd

# Librería utilizada para crear gráficas y visualizaciones.
import matplotlib.pyplot as plt
# ============================================================

# Se guarda el nombre del archivo CSV en una variable, ya que este contiene informacion de ventas de productos tecnológicos.
archivo = "ventas_tecnologia.csv"


# Lee el archivo CSV y convierte la información en una tabla llamada DataFrame que es una tabla de datos con filas y columnas.
df = pd.read_csv(archivo)

# ============================================================
# PROCESAMIENTO DE DATOS
# ============================================================

# Se crea una nueva columna llamada "ingresos" ya que esta permite calcular el dinero generado por cada venta.
# ingresos = cantidad * precio_unitario
df["ingresos"] = df["cantidad"] * df["precio_unitario"]
print("\n===== DATOS GENERALES =====")
print(df)
# ============================================================
# Obtiene la cantidad total vendida de cada producto.
ventas_producto = df.groupby("producto")["cantidad"].sum()

print("\n===== VENTAS TOTALES POR PRODUCTO =====")
print(ventas_producto)
# Esto permite identificar:
# - meses más rentables
ventas_mes = df.groupby("mes")["ingresos"].sum()

print("\n===== INGRESOS TOTALES POR MES =====")
print(ventas_mes)
# Sirve para saber:
# - qué producto genera más dinero
ingresos_producto = df.groupby("producto")["ingresos"].sum()

print("\n===== INGRESOS GENERADOS POR PRODUCTO =====")
print(ingresos_producto)
# En este caso devuelve el nombre del producto con mayor cantidad vendida.
producto_mas_vendido = ventas_producto.idxmax()

print("\n===== PRODUCTO MÁS VENDIDO =====")
print(producto_mas_vendido)

# Define el color azul claro de las barras.
ventas_producto.plot(kind='bar', color='hotpink')

# Coloca un título a la gráfica.
plt.title("Ventas por Producto")
# Nombre del eje horizontal.
plt.xlabel("Producto")
# Nombre del eje vertical.
plt.ylabel("Cantidad Vendida")
# Muestra la gráfica en pantalla.
plt.show()
# Se define el orden cronológico correcto.
orden_meses = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio"
]

# Convertir la columna "mes" en categórica
# para respetar el orden definido.
df["mes"] = pd.Categorical(
    df["mes"],
    categories=orden_meses,
    ordered=True
)
# Ahora sí se agrupan correctamente.
ventas_mes = df.groupby("mes")["ingresos"].sum()

# ============================================================
# GRÁFICA DE LÍNEAS
# ============================================================

ventas_mes.plot(kind='line', marker='o', color='deeppink')

plt.title("Evolución Mensual de Ventas")
plt.xlabel("Mes")
plt.ylabel("Ingresos")

plt.show()

# Lista de tonos rosa: Rosa claro, Rosa fuerte, Rosa pastel
tonos_rosa = ['#FFB6C1', '#FF69B4', '#FF1493']

ventas_producto.plot(kind='pie', autopct='%1.1f%%', colors=tonos_rosa)
plt.title("Porcentaje de Ventas por Producto")
plt.ylabel("") # Elimina la etiqueta lateral para que se vea limpio
plt.show()
# Devuelve el producto que genera más dinero.
producto_mayores_ingresos = ingresos_producto.idxmax()
# Devuelve el producto con menor cantidad vendida.
producto_menos_vendido = ventas_producto.idxmin()
# Busca el mes con mayores ingresos.
mes_mas_rentable = ventas_mes.idxmax()

print("\n===== ANALISIS FINAL (Jerarquía) =====")

print(f"Producto con mayores ingresos: {producto_mayores_ingresos}")

print(f"Producto menos vendido: {producto_menos_vendido}")

print(f"Mes más rentable: {mes_mas_rentable}")

print(f"Producto prioritario para inventario: {producto_mas_vendido}")

# Esta sección transforma los datos en conclusiones útiles para la empresa.

print("\n===== INTERPRETACIÓN PARA LA TOMA DE DECISIONES =====")

# Se considera más importante el producto que genera mayores ingresos.
print(f"1. Producto más importante: {producto_mayores_ingresos}, por su alto impacto financiero.")

# Explica cuál es la información más importante para apoyar decisiones empresariales.
print("2. Información crítica: La relación entre volumen de ventas y margen de utilidad por producto.")

# Se recomienda promocionar el producto con menos ventas para aumentar su rotación.
print(f"3. Promoción: Se recomienda promocionar el '{producto_menos_vendido}' para aumentar su rotación.")

# Indica el mes con mayores oportunidades comerciales.
print(f"4. Oportunidades: El mes de {mes_mas_rentable} representa la mayor oportunidad de venta.")