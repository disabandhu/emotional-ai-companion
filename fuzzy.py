# fuzzy.py

def triangular(x, a, b, c):
    # Peak point
    if x == b:
        return 1

    # Left side
    if a < x < b:
        return (x - a) / (b - a)

    # Right side
    if b < x < c:
        return (c - x) / (c - b)

    return 0


def get_membership_levels(value):
    return {
        "low": triangular(value, 0, 0, 0.5),
        "medium": triangular(value, 0, 0.5, 1),
        "high": triangular(value, 0.5, 1, 1.01)  # slight extension
    }

def infer_strategy(emotions):
    sadness = get_membership_levels(emotions["sadness"])
    anxiety = get_membership_levels(emotions["anxiety"])
    happiness = get_membership_levels(emotions["happiness"])
    anger = get_membership_levels(emotions["anger"])

    scores = {
        "comfort": sadness["high"] + sadness["medium"],
        "distract": anxiety["high"] + anxiety["medium"],
        "engage": happiness["high"] + happiness["medium"],
        "reflect": anger["high"] + anger["medium"]
    }

    strategy = max(scores, key=scores.get)
    return strategy, scores

    # Pick best strategy
    strategy = max(scores, key=scores.get)
    return strategy, scores