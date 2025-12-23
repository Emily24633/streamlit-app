import streamlit as st

st.title("My first Streamlit program 🚀")

name = st.text_input("Whar is your name？")

if name:
    st.write(f"hello，{name}！welcome to use my program 😊")
st.title("声音测试")

if st.button("点我"):
    st.success("触发成功")
    st.audio("sound.mp3")
import streamlit as st
import random

st.title("音符听辨小游戏 🎵")
st.write("听音符并猜它是 1-7 中的哪一个！")

# 初始化状态
if 'target' not in st.session_state:
    st.session_state.target = random.randint(1, 7)
if 'message' not in st.session_state:
    st.session_state.message = ""

# 播放音符按钮
if st.button("播放音符"):
    audio_file = open(f"music/{st.session_state.target}.mp3", "rb")
    st.audio(audio_file, format="audio/mp3")
    st.session_state.message = ""  # 清空提示

# 用户输入猜测
guess = st.number_input("请输入你猜的音符 (1-7):", min_value=1, max_value=7, step=1)

if st.button("提交答案"):
    if guess < st.session_state.target:
        st.session_state.message = "有点低哦，试试高一点的吧！"
    elif guess > st.session_state.target:
        st.session_state.message = "有点高哦，试试低一点的吧！"
    else:
        st.session_state.message = "恭喜答对了 🎉！再来一次请点击播放音符。"
        # 重新生成下一个音符
        st.session_state.target = random.randint(1, 7)

st.write(st.session_state.message)



