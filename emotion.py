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
    sadness_words = ["sad", "tired", "empty", "lonely", "depressed", "down", "hurt"]
    anxiety_words = ["worried", "anxious", "nervous", "stress", "panic", "overthinking"]
    happiness_words = ["happy", "excited", "good", "great", "love", "amazing", "joy"]
    anger_words = ["angry", "mad", "frustrated", "annoyed", "irritated"]

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