import random
import numpy as np

def genetic_algorithm(individual_size, population_size, fitness_fn, max_fitness, generations):
    population = [
        np.random.uniform(-1, 1, individual_size)
        for _ in range(population_size)
    ]

    for gen in range(generations):
        seed = random.randint(0, 100000)

        scored = []
        for ind in population:
            fit = fitness_fn(ind, seed)
            scored.append((ind, fit))

        scored.sort(key=lambda x: x[1], reverse=True)

        best_ind, best_fit = scored[0]
        print(f'Gen {gen} | Best fitness: {best_fit}')

        if best_fit >= max_fitness:
            return best_ind, best_fit

        # Elitismo
        new_population = [best_ind.copy()]

        while len(new_population) < population_size:
            p1 = tournament(scored)
            p2 = tournament(scored)
            child = crossover(p1, p2)
            mutate(child)
            new_population.append(child)

        population = new_population

    return scored[0]


def tournament(scored, k=3):
    competitors = random.sample(scored, k)
    return max(competitors, key=lambda x: x[1])[0]


def crossover(p1, p2):
    point = random.randint(1, len(p1)-1)
    return np.concatenate((p1[:point], p2[point:]))


def mutate(ind, rate=0.05, scale=0.3):
    for i in range(len(ind)):
        if random.random() < rate:
            ind[i] += random.gauss(0, scale)