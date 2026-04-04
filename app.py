import streamlit as st
from emotion import detect_emotion

st.title("🌌 Emotional AI Companion")

user_input = st.text_input("Say something...")

if user_input:
    emotions = detect_emotion(user_input)
    st.write("Detected Emotions:", emotions)