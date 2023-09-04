import streamlit as st
import webbrowser
import pandas as pd

if 'data' not in st.session_state:
    df = pd.read_csv('datasets\CLEAN_FIFA23_official_data.csv',index_col=0)
    df=df.sort_values(by='Overall', ascending=False)
    st.session_state['data']=df
    

st.markdown('# FIFA 23')
st.sidebar.markdown('Desenvolvido por [mim](https://github.com/eduardoandd)')

btn = st.button('Dados retirados do Kaggles')

if btn:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets')