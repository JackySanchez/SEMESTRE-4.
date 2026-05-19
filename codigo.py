import csv
import json
import time
import psutil
import os

# ==============================
# MEDICIÓN DE RECURSOS
# ==============================

def medir_memoria():
    proceso = psutil.Process(os.getpid())
    memoria = proceso.memory_info().rss / 1024 / 1024
    return memoria

# ==============================
# LECTURA CSV
# ==============================

inicio = time.time()
memoria_inicio = medir_memoria()

with open('datos.csv', 'r', encoding='utf-8') as archivo_csv:
    lector = list(csv.DictReader(archivo_csv))

memoria_final = medir_memoria()
fin = time.time()

print("LECTURA CSV")
print("Tiempo:", fin - inicio, "segundos")
print("Memoria usada:", memoria_final - memoria_inicio, "MB")

# ==============================
# LECTURA JSON
# ==============================

inicio = time.time()
memoria_inicio = medir_memoria()

with open('datos.json', 'r', encoding='utf-8') as archivo_json:
    datos_json = json.load(archivo_json)

memoria_final = medir_memoria()
fin = time.time()

print("\nLECTURA JSON")
print("Tiempo:", fin - inicio, "segundos")
print("Memoria usada:", memoria_final - memoria_inicio, "MB")

# ==============================
# CONVERSIÓN CSV A JSON
# ==============================

inicio = time.time()

with open('datos.csv', 'r', encoding='utf-8') as archivo_csv:
    lector = list(csv.DictReader(archivo_csv))

with open('convertido.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(lector, archivo_json, indent=4)

fin = time.time()

print("\nConversión CSV -> JSON")
print("Tiempo:", fin - inicio, "segundos")

# ==============================
# CONVERSIÓN JSON A CSV
# ==============================

inicio = time.time()

with open('datos.json', 'r', encoding='utf-8') as archivo_json:
    datos = json.load(archivo_json)

with open('convertido.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
    campos = datos[0].keys()
    escritor = csv.DictWriter(archivo_csv, fieldnames=campos)

    escritor.writeheader()
    escritor.writerows(datos)

fin = time.time()

print("\nConversión JSON -> CSV")
print("Tiempo:", fin - inicio, "segundos")