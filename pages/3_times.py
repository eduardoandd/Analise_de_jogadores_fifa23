import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Jogadores',
    layout='wide'
)

df=st.session_state['data']

clubes= df['Club'].value_counts().index
clube=st.sidebar.selectbox('Clube',clubes)

df_filtro=df[(df['Club']==clube)].set_index('Name')
st.image(df_filtro.iloc[0]['Club Logo'])


colunas=['Age','Photo','Flag','Overall','Value(£)','Wage(£)','Joined',
         'Height(cm.)','Weight(lbs.)','Contract Valid Until','Release Clause(£)']

st.dataframe(df_filtro[colunas],
             column_config={
                 'Overall':st.column_config.ProgressColumn(
                     'Overall', format='%d', min_value=0,max_value=100
                 ),
                 'Wage(£)':st.column_config.ProgressColumn('Salário\sem',format='£%f',
                                                                  min_value=0,max_value=df_filtro['Wage(£)'].max()),
                 'Photo':st.column_config.ImageColumn('Foto'),
                 'Flag':st.column_config.ImageColumn('Pais')
                 
             })



