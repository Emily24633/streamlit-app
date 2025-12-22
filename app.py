import streamlit as st

st.title("my first Streamlit program 🚀")

name = st.text_input("Whar is your name？")

if name:
    st.write(f"hello，{name}！welcome to use my program 😊")

