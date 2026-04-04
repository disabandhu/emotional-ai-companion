import streamlit as st
from emotion import detect_emotion
from fuzzy import infer_strategy
from responses import generate_response
from ga import run_ga

st.title("🌌 Emotional AI Companion")

user_input = st.text_input("Say something...")

emotions = detect_emotion(user_input)

best_personality = run_ga(emotions)

empathy, humor, directness = best_personality

if user_input:
    emotions = detect_emotion(user_input)
    strategy, scores = infer_strategy(emotions)
    response = generate_response(strategy, {
    "empathy": empathy,
    "humor": humor,
    "directness": directness
})

    st.write("Emotions:", emotions)
    st.write("Strategy:", strategy)
    st.write("Response:", response)
    st.write("🧬 Evolved Personality:")
st.write({
    "empathy": float(empathy),
    "humor": float(humor),
    "directness": float(directness)
})