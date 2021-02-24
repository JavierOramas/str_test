import streamlit as st

A = st.number_input('a')
B = st.number_input('b')

if st.button('caluclar'):
    st.text(f'{A+B}')