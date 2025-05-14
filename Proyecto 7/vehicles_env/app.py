import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado de la aplicación
st.header('Exploración de Datos de Vehículos Usados')

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Casilla de verificación para mostrar tabla
build_tabla = st.checkbox('Mostrar tabla de datos')
if build_tabla:
    st.subheader('Tabla de datos')
    st.write('Datos de vehículos usados en venta')
    st.write('Número total de registros:', len(car_data))
    st.write('Número total de columnas:', len(car_data.columns))
    st.write('Número total de valores nulos:', car_data.isnull().sum().sum())

    # Slider para seleccionar cuántas filas mostrar
    num_filas = st.slider('Selecciona cuántas filas mostrar', min_value=5, max_value=100, value=5, step=5)

    st.subheader(f'Vista previa de los primeros {num_filas} registros')
    st.write(car_data.head(num_filas))


# Casilla de verificación para construir histograma
build_histogram = st.checkbox('Mostrar histograma del odómetro')
if build_histogram:
    st.subheader('Histograma del odómetro')
    st.write('Distribución de kilometraje en los anuncios de venta de coches')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla de verificación para gráfico de dispersión
build_scatter = st.checkbox('Odómetro vs precio')
if build_scatter:
    st.subheader('Dispersión entre odómetro y precio')
    st.write('Relación entre el kilometraje y el precio de los vehículos')
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Relación entre el kilometraje y el precio"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# Casilla de verificación para treemap
build_treemap = st.checkbox('Precio por combustible y modelo')
if build_treemap:
    st.subheader('Treemap de precios por tipo de combustible y modelo')
    st.write('Visualización jerárquica del precio por tipo de combustible y modelo')
    fig_treemap = px.treemap(car_data, path=['fuel', 'model'], values='price')
    st.plotly_chart(fig_treemap, use_container_width=True)

# Casilla de verificación para gráfico con patrón de forma (pattern_shape)
build_pattern_shape = st.checkbox('Construir gráfico con patrón de forma')
if build_pattern_shape:
    st.subheader('Gráfico con textura')
    st.write('Creación de un gráfico de patrón de forma: precio promedio por tipo de combustible')

    # Agrupar datos por tipo de combustible
    grouped_data = car_data.groupby('fuel', as_index=False)['price'].mean()

    # Crear gráfico de barras con patrones
    fig_pattern = px.bar(
        grouped_data,
        x='fuel',
        y='price',
        pattern_shape='fuel',  # patrón por categoría
        title='Precio promedio por tipo de combustible',
        labels={'price': 'Precio promedio', 'fuel': 'Tipo de combustible'}
    )
    st.plotly_chart(fig_pattern, use_container_width=True)
