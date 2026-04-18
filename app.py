import streamlit as st
from emotion import detect_emotion
from fuzzy import infer_strategy
from responses import generate_response
from ga import run_ga

# ---------- GLOBAL UI STYLE (CONSTANT BACKGROUND) ----------
st.markdown("""
<style>

/* HIDE STREAMLIT UI */
header {visibility: hidden;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* MAIN BACKGROUND */
.stApp {
    background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #1e3c72);
    background-size: 400% 400%;
    animation: gradientMove 20s ease infinite;
    color: white;
}

/* GRADIENT ANIMATION */
@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* FLOATING PARTICLES */
.stApp::before {
    content: "";
    position: fixed;
    width: 200%;
    height: 200%;
    top: 0;
    left: 0;
    background-image: radial-gradient(rgba(255,255,255,0.08) 1px, transparent 1px);
    background-size: 40px 40px;
    animation: moveParticles 60s linear infinite;
    z-index: 0;
}

/* PARTICLE ANIMATION */
@keyframes moveParticles {
    from { transform: translate(0, 0); }
    to { transform: translate(-200px, -200px); }
}

/* CONTENT ABOVE PARTICLES */
.block-container {
    position: relative;
    z-index: 1;
    padding-top: 1rem;
}

/* INPUT BOX */
input {
    background: rgba(255,255,255,0.1) !important;
    backdrop-filter: blur(10px);
    border-radius: 10px !important;
    color: white !important;
}

/* TEXT */
h1, h2, h3, h4, h5, h6, p, label, span {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)
# ----------------------------------------------------------


st.title("🌌 Lily")

user_input = st.text_input("Say something...")

if user_input:
    emotions = detect_emotion(user_input)

    # (BACKGROUND LOGIC REMOVED — now constant)

    best_personality = run_ga(emotions)
    empathy, humor, directness = best_personality

    strategy, scores = infer_strategy(emotions)

    response = generate_response(strategy, {
        "empathy": empathy,
        "humor": humor,
        "directness": directness
    })

    st.write("Emotions:", emotions)
    st.write("Strategy:", strategy)
    import time

    st.write("Response:")

    placeholder = st.empty()
    typed_text = ""

    for char in response:
        typed_text += char
        placeholder.markdown(f"<div style='font-size:18px'>{typed_text}</div>", unsafe_allow_html=True)
        time.sleep(0.02)

    st.write("🧬 Evolved Personality:")
    st.write({
        "empathy": float(empathy),
        "humor": float(humor),
        "directness": float(directness)
    })

else:
    st.info("Start typing to activate the emotional AI.")