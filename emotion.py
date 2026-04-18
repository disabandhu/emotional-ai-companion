# emotion.py

def detect_emotion(text):
    text = text.lower()

    emotions = {
        "sadness": 0,
        "anxiety": 0,
        "happiness": 0,
        "anger": 0
    }

    # Keyword mapping (basic but effective)
    sadness_words = [
        "sad", "tired", "empty", "lonely", "depressed", "down", "hurt",
        "heartbroken", "hopeless", "worthless", "numb", "drained",
        "i feel alone", "no one cares", "nothing matters", "i miss them",
        "i feel lost", "everything feels pointless", "i feel empty inside",
        "i can't go on", "i feel broken", "i feel like giving up",
        "i hate my life", "i feel like a burden", "why am i like this",
        "i feel so low", "i just want to disappear", "i feel invisible",
        "nobody understands me", "i feel disconnected", "i feel abandoned",
        "everything is falling apart", "i'm not okay", "i feel weak",
        "i feel exhausted emotionally", "i feel dead inside",
        "i can't stop crying", "i feel unwanted", "i feel like nothing",
        "i feel stuck in life", "i feel rejected", "i feel like i'm failing"
    ]

    anxiety_words = [
        "worried", "anxious", "nervous", "stress", "panic", "overthinking",
        "restless", "uneasy", "tense", "on edge", "paranoid",
        "what if", "i can't stop thinking", "something will go wrong",
        "i feel uneasy", "i'm scared of what might happen",
        "i'm freaking out", "i feel like something bad will happen",
        "my mind won't stop", "i keep thinking about it",
        "i can't relax", "i feel overwhelmed", "i'm overthinking everything",
        "i'm scared", "i feel pressure", "i feel suffocated",
        "i feel like i'm losing control", "i feel shaky",
        "my heart is racing", "i can't breathe properly",
        "i'm constantly worried", "i feel tense all the time",
        "i feel trapped", "i'm spiraling", "i feel uncertain",
        "i don't know what to do", "i feel stressed out",
        "i feel like i'm going crazy", "i can't calm down",
        "i feel mentally overloaded"
    ]

    happiness_words = [
        "happy", "excited", "good", "great", "love", "amazing", "joy",
        "cheerful", "content", "peaceful", "grateful", "blessed",
        "best day ever", "so excited", "i feel amazing", "this is perfect",
        "i'm so grateful", "i feel so good", "i'm really happy",
        "i feel at peace", "life is good", "i'm enjoying this",
        "i feel fulfilled", "i feel positive", "i'm in a good mood",
        "i feel motivated", "i'm proud of myself",
        "everything is going well", "i feel lucky",
        "this made my day", "i'm smiling so much",
        "i feel light", "i feel calm and happy",
        "i feel appreciated", "i feel loved",
        "things are finally working out", "i feel confident",
        "i'm genuinely happy", "i feel satisfied"
    ]

    anger_words = [
        "angry", "mad", "frustrated", "annoyed", "irritated",
        "furious", "pissed", "rage", "resentful", "triggered",
        "this is unfair", "i hate this", "why would they do that",
        "this makes me so mad", "i'm so done", "i can't stand this",
        "this is ridiculous", "i'm fed up", "this is so annoying",
        "i'm losing my patience", "i feel disrespected",
        "i feel insulted", "this is bullshit", "i'm so frustrated right now",
        "nothing works", "why does this always happen",
        "i'm tired of this", "this is driving me crazy",
        "i feel like screaming", "i want to punch something",
        "i feel attacked", "this is unacceptable",
        "i can't deal with this", "this pisses me off",
        "i feel provoked", "i'm really upset about this",
        "i feel wronged", "this crossed the line"
    ]

    for word in sadness_words:
        if word in text:
            emotions["sadness"] += 1

    for word in anxiety_words:
        if word in text:
            emotions["anxiety"] += 1

    for word in happiness_words:
        if word in text:
            emotions["happiness"] += 1

    for word in anger_words:
        if word in text:
            emotions["anger"] += 1

    # Normalize (0 to 1 range)
    total = sum(emotions.values())
    if total > 0:
        for key in emotions:
            emotions[key] = round(emotions[key] / total, 2)

    return emotions