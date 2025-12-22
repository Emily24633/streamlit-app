import streamlit as st

st.title("我的第一个 Streamlit 小程序 🚀")

name = st.text_input("你叫什么名字？")

if name:
    st.write(f"你好，{name}！欢迎使用我的程序 😊")
