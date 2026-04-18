# responses.py

import random

last_response = None 

responses = {
    "comfort": [
        "That sounds really heavy… do you want to talk about it?",
        "I’m here for you. You don’t have to go through this alone.",
        "It’s okay to feel this way. What’s been weighing on you?",
        "That must be really hard to deal with… I’m listening.",
        "You don’t have to carry all of this by yourself.",
        "I’m really glad you shared this with me.",
        "That sounds overwhelming… do you want to unpack it together?",
        "It’s completely valid to feel like this.",
        "I can imagine how draining that must feel.",
        "You’re not alone in this, even if it feels like it.",
        "That kind of feeling can really take a toll… I’m here.",
        "It makes sense that this would affect you.",
        "Take your time—there’s no rush to figure everything out.",
        "I’m right here with you. What part of this feels the hardest?",
        "Even saying this out loud takes strength.",
        "You don’t need to have everything sorted right now.",
        "It’s okay if things feel messy. We can sort through it slowly.",
        "I hear you… and I’m not going anywhere.",
        "That sounds like a lot to handle emotionally.",
        "You’re allowed to feel this, no matter what."
    ],

    "distract": [
        "Let’s take your mind off things for a bit. What do you enjoy?",
        "Maybe a small break could help. Want something light?",
        "Let’s switch gears—tell me something random.",
        "How about we reset for a moment—what usually cheers you up?",
        "Let’s pause this for a second. Want to talk about something fun?",
        "Okay, mini escape time—movies, music, or chaos?",
        "Let’s give your brain a breather. What sounds nice right now?",
        "We could shift focus for a bit—sometimes that helps.",
        "Tell me something completely unrelated, I’m curious.",
        "Let’s lighten the mood—what’s something you like talking about?",
        "Quick distraction break—favorite food or comfort show?",
        "Let’s step out of this loop for a minute.",
        "Want me to throw a random topic your way?",
        "Let’s hit pause and reset your headspace.",
        "Sometimes a small mental detour helps more than we think.",
        "Let’s just vibe for a second—no pressure.",
        "What’s something simple that makes you smile?",
        "We can come back to this later—what do you feel like doing now?",
        "Let’s take a tiny break from overthinking.",
        "Okay, brain break activated 😄 what’s up?"
    ],

    "engage": [
        "That’s amazing! Tell me more.",
        "I love that energy. What’s going right?",
        "This sounds great—what’s the highlight?",
        "Wait, I’m invested now—what happened next?",
        "That’s actually really interesting.",
        "Okay, I need more details on this.",
        "This has good vibes written all over it.",
        "Tell me everything, don’t skip the good parts.",
        "That sounds like a win—what made it special?",
        "I’m curious now, keep going.",
        "This is the kind of energy I like to see.",
        "What part of this made you the happiest?",
        "That sounds like it meant a lot to you.",
        "Okay yeah, I’m listening—go on.",
        "This feels like a moment worth celebrating.",
        "I can feel the excitement through the screen 😄",
        "What’s the best part about all this?",
        "This sounds like progress honestly.",
        "You’ve got my attention—tell me more.",
        "I like where this is going."
    ],

    "reflect": [
        "Let’s slow this down—what exactly made you feel this way?",
        "Why do you think this affected you so much?",
        "Let’s unpack this together.",
        "What part of this stuck with you the most?",
        "If you think about it, where did this feeling start?",
        "What do you think is at the core of this?",
        "Let’s take it step by step—what happened first?",
        "Which part of this situation feels the heaviest?",
        "If you had to describe it in one thought, what would it be?",
        "What do you think you needed in that moment?",
        "Is this something that’s been building up over time?",
        "What about this situation made it hit harder?",
        "Let’s try to break this into smaller pieces.",
        "What’s the underlying thought behind this feeling?",
        "Do you think this connects to something bigger?",
        "What would you say is bothering you the most right now?",
        "If you zoom out, what stands out to you?",
        "What do you wish had gone differently?",
        "What does this situation mean to you personally?",
        "Let’s explore this a bit deeper, at your pace."
    ]
}


def apply_personality(response, personality):
    empathy = personality["empathy"]
    humor = personality["humor"]
    directness = personality["directness"]

    # ---------------- EMPATHY ----------------
    if empathy > 0.75:
        empathy_prefixes = [
            "I really hear you.",
            "That sounds genuinely tough.",
            "I get why that would feel this way.",
            "I’m here with you."
        ]
        response = random.choice(empathy_prefixes) + " " + response

    elif empathy < 0.3:
        remove_phrases = [
            "I’m here for you.",
            "I’m here with you.",
            "I understand how you feel.",
            "That sounds really heavy…"
        ]
        for phrase in remove_phrases:
            response = response.replace(phrase, "").strip()

    # ---------------- HUMOR ----------------
    if humor > 0.75:
        humor_suffixes = [
            " 😄",
            " — we’ve got this though",
            " (lowkey you’ll get through this)",
            " — not the best vibe, but we move"
        ]
        response += random.choice(humor_suffixes)

    elif humor < 0.3:
        response = response.replace("!", ".")
        response = response.replace("😄", "")
        response = response.replace("haha", "")

    # ---------------- DIRECTNESS ----------------
    if directness > 0.75:
        response = response.replace("do you want to", "want to")
        response = response.replace("would you like to", "try to")
        response = response.replace("maybe", "")
        response = response.replace("let’s", "we can")

    elif directness < 0.3:
        softeners = [
            "Maybe we can explore this gently.",
            "If you're okay with it,",
            "We can take this slowly,"
        ]
        response = random.choice(softeners) + " " + response

    # ---------------- FLOW CLEANUP ----------------
    response = " ".join(response.split())  # remove extra spaces

    return response


 # define this globally

def generate_response(strategy, personality):
    global last_response

    options = responses[strategy]

    if last_response in options and len(options) > 1:
        options = [r for r in options if r != last_response]

    base = random.choice(options)
    last_response = base

    return apply_personality(base, personality)