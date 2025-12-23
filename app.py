import streamlit as st

st.title("My first Streamlit program 🚀")

name = st.text_input("Whar is your name？")

if name:
    st.write(f"hello，{name}！welcome to use my program 😊")

import random

st.title("Note Recognition Game 🎵")

# ramdomize notes
if 'target' not in st.session_state:
    st.session_state.target = random.randint(1, 7)
if 'message' not in st.session_state:
    st.session_state.message = ""

# button
if st.button("Play Note") or st.session_state.played:
    st.session_state.played = True
    audio_file = open(f"project_folder/{st.session_state.target}.mp3", "rb")  # 假设音频文件是 .mp3 格式
    st.audio(audio_file, format="audio/mp3")
    st.session_state.message = ""

# user's input
guess = st.number_input("Please enter the musical note you guessed (1-7):", min_value=1, max_value=7, step=1)

if st.button("Submit"):
    if guess < st.session_state.target:
        st.session_state.message = "It's a bit low, try a higher one!"
    elif guess > st.session_state.target:
        st.session_state.message = "It's a bit high, try a lower one!"
    else:
        st.session_state.message = "Congratulations on answering correctly 🎉! To try again, please click to play the musical note."
        # sellect another note after answering
        st.session_state.target = random.randint(1, 7)

# display result
st.write(st.session_state.message)













