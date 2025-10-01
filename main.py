import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar a base de dados do mesmo diretório do script
df = pd.read_csv('base_funcionarios.csv', delimiter='\t')

st.title('Dashboard RH – Visualização de Perfil dos Servidores')

# Filtros interativos conforme as colunas da base
faixas_idade = st.multiselect(
    'Faixa Idade:',
    df['Faixa Idade'].unique(),
    default=df['Faixa Idade'].unique()
)
genero = st.multiselect(
    'Gênero:',
    df['Gênero'].unique(),
    default=df['Gênero'].unique()
)

# Filtro aplicado ao DataFrame
df_filt = df[df['Faixa Idade'].isin(faixas_idade) & df['Gênero'].isin(genero)]

# Gráfico: Distribuição por Faixa Etária e Gênero
st.subheader('Distribuição por Faixa Etária e Gênero')
fig1 = px.bar(
    df_filt,
    x='Faixa Idade',
    color='Gênero',
    barmode='group',
    labels={'count':'Total'}
)
st.plotly_chart(fig1)

# Gráfico: Distribuição por Tempo de Casa
st.subheader('Distribuição por Tempo de Casa')
fig2 = px.bar(
    df_filt,
    x='Faixa Tempo de Casa',
    color='Gênero',
    barmode='group',
    labels={'count':'Total'}
)
st.plotly_chart(fig2)

# Gráfico: Proporção de Gênero
st.subheader('Proporção de Gênero')
fig3 = px.pie(
    df_filt,
    names='Gênero',
    title='Proporção de colaboradores por gênero'
)
st.plotly_chart(fig3)

# Opcional: Caso queira visualizar nomes das colunas para debug inicial, descomente:
# st.write('Colunas disponíveis:', df.columns.tolist())
