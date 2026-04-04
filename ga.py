import numpy as np
import random

# Personality = [empathy, humor, directness]

# -----------------------------
# Initialize population
# -----------------------------
def init_population(size=20):
    return [np.random.rand(3) for _ in range(size)]


# -----------------------------
# Fitness function
# emotions = dict from your emotion.py
# -----------------------------
def fitness(personality, emotions):
    empathy, humor, directness = personality

    score = 0

    # Sadness → empathy
    score += emotions["sadness"] * empathy

    # Anxiety → empathy high, humor low
    score += emotions["anxiety"] * (0.7 * empathy + 0.3 * (1 - humor))

    # Happiness → humor
    score += emotions["happiness"] * humor

    # Anger → directness
    score += emotions["anger"] * directness

    return score


# -----------------------------
# Selection (top k)
# -----------------------------
def select(population, emotions, k=10):
    scored = [(p, fitness(p, emotions)) for p in population]
    scored.sort(key=lambda x: x[1], reverse=True)
    return [p for p, _ in scored[:k]]


# -----------------------------
# Crossover
# -----------------------------
def crossover(parent1, parent2):
    child = np.array([
        random.choice([parent1[0], parent2[0]]),
        random.choice([parent1[1], parent2[1]]),
        random.choice([parent1[2], parent2[2]])
    ])
    return child


# -----------------------------
# Mutation
# -----------------------------
def mutate(personality, rate=0.1):
    for i in range(len(personality)):
        if random.random() < rate:
            personality[i] += np.random.normal(0, 0.1)

    # Keep values in [0,1]
    personality = np.clip(personality, 0, 1)
    return personality


# -----------------------------
# Run GA
# -----------------------------
def run_ga(emotions, generations=20, pop_size=20):
    population = init_population(pop_size)

    for _ in range(generations):
        selected = select(population, emotions, k=pop_size // 2)

        new_population = selected.copy()

        while len(new_population) < pop_size:
            p1, p2 = random.sample(selected, 2)
            child = crossover(p1, p2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

    # Return best personality
    best = max(population, key=lambda p: fitness(p, emotions))
    return best