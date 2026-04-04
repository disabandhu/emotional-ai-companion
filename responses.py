# responses.py

import random

responses = {
    "comfort": [
        "That sounds really heavy… do you want to talk about it?",
        "I’m here for you. You don’t have to go through this alone.",
        "It’s okay to feel this way. What’s been weighing on you?"
    ],
    "distract": [
        "Hey, let’s take your mind off things for a bit. What do you usually enjoy?",
        "Maybe a small break could help. Want to talk about something lighter?",
        "Let’s shift gears for a moment—tell me something random or fun."
    ],
    "engage": [
        "That’s amazing! Tell me more about what’s making you feel this way.",
        "I love that energy. What’s been going right?",
        "You sound really positive—what’s the highlight of your day?"
    ],
    "reflect": [
        "It seems like something is bothering you. Want to unpack it together?",
        "Let’s slow this down—what exactly made you feel this way?",
        "I hear you. Why do you think this situation affected you so much?"
    ]
}


def generate_response(strategy):
    return random.choice(responses[strategy])