import streamlit as st
import pandas as pd
import plotly.express as px

# Título do aplicativo
st.header('Análise de Veículos')

# Carregar dados
df = pd.read_csv('vehicles_us.csv')

# Mostrar dados
st.subheader('Dados dos Veículos')
st.dataframe(df.head())

# Criar histograma
st.subheader('Histograma de Preços')
fig_hist = px.histogram(df, x='price', title='Distribuição de Preços')
st.plotly_chart(fig_hist)

# Criar gráfico de dispersão
st.subheader('Gráfico de Dispersão')
fig_scatter = px.scatter(df, x='odometer', y='price', title='Preço vs Quilometragem')
st.plotly_chart(fig_scatter)

# Adicionar checkbox
if st.checkbox('Mostrar apenas carros com preço acima de $10,000'):
    df_filtered = df[df['price'] > 10000]
    st.write(f'Mostrando {len(df_filtered)} veículos')
    st.dataframe(df_filtered)
