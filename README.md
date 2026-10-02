# Regresión Lineal — Ingresos fiscales municipales 2024

Autora: Sandra Yurani Ayala Herrera — UdeC

## Objetivo
Estimar los ingresos tributarios y no tributarios per cápita de municipios colombianos en 2024 mediante regresión lineal múltiple.

## Fuentes
- CUIPO / ejecución de ingresos 2024: archivo `2024_Ejecución de Ingresos_AP_2.xlsx`.
- DANE, proyecciones municipales de población 2018–2042: `PPED-AreaMun-2018-2042_VP.xlsx`.
- IGAC: datos abiertos geoespaciales consultados como referencia para variables territoriales.

## Variables
Y: `ingresos_per_capita`.
X1: `poblacion_2024`.
X2: `pct_poblacion_cabecera`.
X3: `poblacion_rural_2024`.

## Ejecución
1. Instalar dependencias: `pip install -r requirements.txt`
2. Mantener las fuentes en rutas relativas.
3. Ejecutar `python scripts/modelo_regresion.py`.

Semilla: 42. División train/test: 80/20.
