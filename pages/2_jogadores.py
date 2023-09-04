import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Jogadores',
    layout='wide'
)

df =st.session_state['data']

clubes = df['Club'].value_counts().index
clube = st.sidebar.selectbox('Clubes', clubes)

df_jogadores = df[(df['Club'] == clube)]
jogadores= df_jogadores['Name'].value_counts().index
jogador = st.sidebar.selectbox('Jogadores',jogadores)

jogador_status = df[df['Name']==jogador].iloc[0]
st.image(jogador_status['Photo'])
st.title(jogador_status['Name'])

st.markdown(f'**Clube:** {jogador_status["Club"]}')
st.markdown(f'**Posição:** {jogador_status["Position"]}')

col1,col2,col3,col4= st.columns(4)
col1 = st.markdown(f'**Idade:** {jogador_status["Age"]}')
col2 = st.markdown(f'**Altura** {jogador_status["Height(cm.)"]/100}')
col3 = st.markdown(f'**Peso:** {jogador_status["Weight(lbs.)"]*0.453:.2f}')
st.divider()

st.subheader(f'OVERALL: {jogador_status["Overall"]}')
st.progress(int(jogador_status["Overall"]))

col1,col2,col3,col4= st.columns(4)
col1.metric(label='Valor de mercado (£)', value=f'{jogador_status["Value(£)"]}')
col2.metric(label='Multa recisória (£)', value=f'{jogador_status["Release Clause(£)"]}')
col3.metric(label='Remuneração (£)', value=f'{jogador_status["Wage(£)"]}')
