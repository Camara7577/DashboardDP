import streamlit as st
import pandas as pd

# Dados exemplo no formato DataFrame
data = [
    {"admissao":"09/04/2025","sexo":"M","nascimento":"20/01/1967","gênero":"Homem"},
    {"admissao":"03/02/2025","sexo":"M","nascimento":"16/06/1968","gênero":"Homem"},
    # ... adicione os demais registros
]
df = pd.DataFrame(data)

# Conversão para tipo de data (para filtros)
df['admissao'] = pd.to_datetime(df['admissao'], dayfirst=True, errors='coerce')
df['nascimento'] = pd.to_datetime(df['nascimento'], dayfirst=True, errors='coerce')

# Filtros
sexo = st.multiselect("Sexo", options=df['sexo'].unique(), default=df['sexo'].unique())
genero = st.multiselect("Gênero", options=df['gênero'].unique(), default=df['gênero'].unique())
ano_nasc = st.slider("Ano de nascimento", int(df['nascimento'].dt.year.min()), int(df['nascimento'].dt.year.max()),
                     (int(df['nascimento'].dt.year.min()), int(df['nascimento'].dt.year.max())))

# Aplicação dos filtros
filtered_df = df[
    (df['sexo'].isin(sexo)) &
    (df['gênero'].isin(genero)) &
    (df['nascimento'].dt.year.between(ano_nasc, ano_nasc[1]))
]

st.dataframe(filtered_df)
