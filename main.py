import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('base_funcionarios.csv', delimiter=';')

st.title('Dashboard RH – Visualização de Perfil dos Servidores')

faixas_idade = st.multiselect('Faixa Idade:', df['Faixa Idade'].unique(), default=df['Faixa Idade'].unique())
genero = st.multiselect('Gênero:', df['Gênero'].unique(), default=df['Gênero'].unique())

df_filt = df[df['Faixa Idade'].isin(faixas_idade) & df['Gênero'].isin(genero)]

st.subheader('Distribuição por Faixa Etária e Gênero')
fig1 = px.bar(df_filt, x='Faixa Idade', color='Gênero', barmode='group')
st.plotly_chart(fig1)

st.subheader('Distribuição por Tempo de Casa')
fig2 = px.bar(df_filt, x='Faixa Tempo de Casa', color='Gênero', barmode='group')
st.plotly_chart(fig2)

st.subheader('Proporção de Gênero')
fig3 = px.pie(df_filt, names='Gênero')
st.plotly_chart(fig3)
