# Laboratorio 09 — Estrategias de Partición de Datos

**Universidad Rafael Landívar**  
**Facultad de Ingeniería**  
**Curso:** Ciencia de Datos  
**Laboratorio 09:** ¿Importa cómo partimos los datos?

## Integrantes

- Nombre: Susana Paola García García 
- Nombre: Harriett Alexandra Guzmán López

## Descripción

En este laboratorio se analiza cómo diferentes estrategias de partición de datos pueden afectar la evaluación de un mismo modelo de Machine Learning.

Se utiliza una regresión logística (M1) y un modelo Dummy como baseline (M0), manteniendo los modelos constantes y modificando únicamente la forma en que los datos se dividen en entrenamiento y prueba.

## Estrategias evaluadas

- División aleatoria con diferentes semillas.
- División estratificada (`stratify`).
- División temporal.
- División por restaurante.
- Comparación del cálculo de variables antes y después de separar los datos.

## Archivos

- `Laboratorio 09.ipynb`: desarrollo completo del laboratorio.
- `pedidos_ruta_verde.csv`: dataset utilizado.
- `README.md`: descripción general del proyecto.

## Estructura del proyecto

```text
Laboratorio 09/
│
├── Laboratorio 09.ipynb
│   └── Notebook principal que contiene:
│       ├── Preparación y reconocimiento del dataset
│       ├── Definición de las preguntas de negocio
│       ├── Modelo M1 - Regresión Logística
│       ├── Modelo M0 - Baseline
│       ├── Parte A - División aleatoria
│       ├── Parte B - División con stratify
│       ├── Parte C - División por fecha
│       ├── Parte D - División por restaurante
│       ├── Parte E - Comparación de riesgo_rest
│       ├── Parte F - Recomendación final
│       ├── Respuestas a las 17 preguntas
│       ├── Tabla comparativa
│       └── Reflexión para llevar a clase
│
├── pedidos_ruta_verde.csv
│   └── Dataset utilizado para realizar los experimentos.
│
└── README.md
    └── Descripción, estructura y herramientas utilizadas en el laboratorio.
```

## Herramientas utilizadas

- Python
- PyCharm
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

## Uso de Inteligencia Artificial

Se utilizó ChatGPT como herramienta de apoyo para comprender las instrucciones del laboratorio, organizar el desarrollo del notebook, revisar el código y apoyar la interpretación de los resultados obtenidos.

Las métricas y resultados presentados fueron obtenidos mediante la ejecución del código sobre el dataset proporcionado.