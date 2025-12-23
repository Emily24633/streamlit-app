import streamlit as st

st.title("My first Streamlit program 🚀")

name = st.text_input("Whar is your name？")

if name:
    st.write(f"hello，{name}！welcome to use my program 😊")
st.title("声音测试")

if st.button("点我"):
    st.success("触发成功")
    st.audio("sound.mp3")



