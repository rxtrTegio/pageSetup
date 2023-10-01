import streamlit as st
from st_functions import st_button, load_css

load_css()

col1, col2, col3 = st.columns(3)

st.header('Rexter Tegio')

st.info('cactus')

icon_size = 20

st_button('docs', 'https://docs.google.com/document/d/1lJCRoc76GWTZ_Aqlsw6Gtnmrj7GCaGxKg2oSeWnwKWI/edit?usp=sharing', icon_size)
