import pandas as pd
import numpy as np

# PASO 1 - CARGAR EL DATASET
df = pd.read_csv(
    'pedidos_ruta_verde.csv',
    parse_dates=['fecha']
)

# Información general del dataset
print("\n=== INFORMACIÓN DEL DATASET ===")
df.info()

# Valores nulos
print("\n=== VALORES NULOS ===")
print(df.isna().sum())


#   PASO 2 - RECONOCER EL DATASET
print("\n=== CANTIDAD DE PEDIDOS ===")
print(len(df))

print("\n=== RESTAURANTES DISTINTOS ===")
print(df['restaurante'].nunique())

print("\n=== RANGO DE FECHAS ===")
print("Fecha mínima:", df['fecha'].min())
print("Fecha máxima:", df['fecha'].max())

print("\n=== TIEMPO DE ENTREGA ===")
print("Mínimo:", df['tiempo_entrega_min'].min())
print("Máximo:", df['tiempo_entrega_min'].max())