# responses.py

import random

responses = {
    "comfort": [
        "That sounds really heavy… do you want to talk about it?",
        "I’m here for you. You don’t have to go through this alone.",
        "It’s okay to feel this way. What’s been weighing on you?"
    ],
    "distract": [
        "Let’s take your mind off things for a bit. What do you enjoy?",
        "Maybe a small break could help. Want something light?",
        "Let’s switch gears—tell me something random."
    ],
    "engage": [
        "That’s amazing! Tell me more.",
        "I love that energy. What’s going right?",
        "This sounds great—what’s the highlight?"
    ],
    "reflect": [
        "Let’s slow this down—what exactly made you feel this way?",
        "Why do you think this affected you so much?",
        "Let’s unpack this together."
    ]
}


def apply_personality(response, personality):
    empathy = personality["empathy"]
    humor = personality["humor"]
    directness = personality["directness"]

    # Empathy effect
    if empathy > 0.7:
        response = "I really understand how you feel. " + response
    elif empathy < 0.3:
        response = response.replace("I’m here for you.", "").strip()

    # Humor effect
    if humor > 0.7:
        response += " 😄"
    elif humor < 0.3:
        response = response.replace("!", ".")

    # Directness effect
    if directness > 0.7:
        response = response.replace("do you want to", "just")

    return response


def generate_response(strategy, personality):
    base = random.choice(responses[strategy])
    return apply_personality(base, personality)