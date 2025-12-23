import streamlit as st

st.title("My first Streamlit program 🚀")

name = st.text_input("Whar is your name？")

if name:
    st.write(f"hello，{name}！welcome to use my program 😊")

import random

st.title("Note recognition game 🎵")

# 初始化随机音符
if 'target' not in st.session_state:
    st.session_state.target = random.randint(1, 7)
if 'message' not in st.session_state:
    st.session_state.message = ""

# 播放音符按钮
if st.button("play note"):
    audio_file = open(f"project folder/{st.session_state.target}.wave.mp3", "rb")
    st.audio(audio_file, format="audio/mp3")
    st.session_state.message = ""

# 用户输入猜测
guess = st.number_input("Please enter the musical note you guessed (1-7):", min_value=1, max_value=7, step=1)

if st.button("submit"):
    if guess < st.session_state.target:
        st.session_state.message = "It's a bit low, try a higher one！"
    elif guess > st.session_state.target:
        st.session_state.message = "It's a bit high, try a lower one！"
    else:
        st.session_state.message = "Congratulations on answering correctly 🎉! To try again, please click to play the musical note."
        st.session_state.target = random.randint(1, 7)

st.write(st.session_state.message)




