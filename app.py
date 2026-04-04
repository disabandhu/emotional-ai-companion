import streamlit as st
from emotion import detect_emotion
from fuzzy import infer_strategy
from responses import generate_response

st.title("🌌 Emotional AI Companion")

user_input = st.text_input("Say something...")

personality = {
    "empathy": 0.2,
    "humor": 0.9,
    "directness": 0.8
}

if user_input:
    emotions = detect_emotion(user_input)
    strategy, scores = infer_strategy(emotions)
    reply = generate_response(strategy, personality)

    st.write("Emotions:", emotions)
    st.write("Strategy:", strategy)
    st.write("Response:", reply)