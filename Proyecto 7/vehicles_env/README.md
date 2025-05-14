# vehicles_env

Proyecto final de Sprint 7 de Herramientas de Desarrollo de Software

📊 Vehículos Usados - Exploración de Datos  
Esta aplicación web fue desarrollada con Streamlit para realizar un análisis exploratorio de datos sobre un conjunto de anuncios de vehículos usados.

## 🚘 ¿Qué hace la aplicación?

La aplicación permite al usuario interactuar con diferentes visualizaciones de los datos mediante casillas de verificación:

- ✅ **Tabla de datos dinámica**: Muestra un resumen del conjunto de datos y permite controlar cuántas filas se visualizan mediante un control deslizante (slider).
- 📉 **Histograma del odómetro**: Muestra la distribución del kilometraje de los vehículos listados.
- 🔍 **Gráfico de dispersión (odómetro vs precio)**: Visualiza la relación entre el kilometraje y el precio de los vehículos.
- 🌳 **Treemap por tipo de combustible y modelo**: Representa jerárquicamente el precio agrupado por tipo de combustible y modelo del vehículo.
- 🧩 **Gráfico con textura (pattern shape)**: Gráfico de barras con patrones visuales para comparar el precio promedio por tipo de combustible.

## 🛠️ Tecnologías utilizadas

- Python  
- pandas  
- plotly-express  
- streamlit  

## ▶️ Cómo ejecutar

1. Clona el repositorio.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Ejecuta la aplicación con:

```bash
streamlit run app.py
