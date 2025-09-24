import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('base_funcionarios.csv', delimiter=';')

st.title('Dashboard RH – Visualização de Perfil dos Servidores')

faixas_idade = st.multiselect('Faixa Idade:', df['Faixa Idade'].unique(), default=df['Faixa Idade'].unique())
genero = st.multiselect('Gênero:', df['Gênero'].unique(), default=df['Gênero'].unique())

df_filt = df[df['Faixa Idade'].isin(faixas_idade) & df['Gênero'].isin(genero)]

st.subheader('Distribuição por Faixa Etária e Gênero (Matplotlib)')
# Exemplo usando Matplotlib
fig, ax = plt.subplots(figsize=(8, 4))
df_grouped = df_filt.groupby(['Faixa Idade', 'Gênero']).size().unstack().fillna(0)
df_grouped.plot(kind='bar', ax=ax)
plt.ylabel('Qtd Funcionários')
plt.xlabel('Faixa Idade')
plt.title('Funcionários por Faixa Etária e Gênero')
plt.legend(title='Gênero')
st.pyplot(fig)
