import streamlit as st
col1, col2 = st.columns(2)
col1.image("Herunterladen.png")
col2.image("Herunterladen (1).png")

st.write("This is a test")

choice = st.selectbox("Choose your element here:", ["Option1", "Option2", "Option3"])

st.write(f'this is my selected option: {choice}')

