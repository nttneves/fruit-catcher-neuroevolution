import random
import numpy as np
import inspect

def create_individual(individual_size):
    return [random.uniform(-1, 1) for _ in range(individual_size)]

def generate_population(individual_size, population_size):
    return [create_individual(individual_size) for _ in range(population_size)]

def crossover(parent1, parent2):
    split_point = random.randint(1, len(parent1) - 1)
    child = parent1[:split_point] + parent2[split_point:]
    return child

def mutate(individual, mutation_rate, mutation_std=0.1):
    mutated = []
    for gene in individual:
        if random.random() < mutation_rate:
            gene += np.random.normal(0, mutation_std)
        mutated.append(gene)
    return mutated

def tournament_selection(scored_population, k=3):
    selected = random.sample(scored_population, k)
    selected.sort(key=lambda x: x[1], reverse=True)
    return selected[0][0]

def evaluate_fitness(fitness_function, individual, seed=None):
    sig = inspect.signature(fitness_function)
    if len(sig.parameters) == 2:
        return fitness_function(individual, seed)
    return fitness_function(individual)

def genetic_algorithm(individual_size, population_size, fitness_function, target_fitness, generations, 
                      elite_rate=0.3, mutation_rate=0.2, mutation_std=0.1, tournament_k=3):

    population = generate_population(individual_size, population_size)
    num_elites = max(1, int(elite_rate * population_size))
    best_individual = None
    best_score = float('-inf')

    for gen in range(generations):
        scored = [(ind, evaluate_fitness(fitness_function, ind, seed=gen)) for ind in population]
        scored.sort(key=lambda x: x[1], reverse=True)

        if scored[0][1] > best_score:
            best_individual, best_score = scored[0]

        if best_score >= target_fitness:
            print(f"Alvo atingido na geração {gen}")
            break

        elites = [ind for ind, _ in scored[:num_elites]]
        new_population = elites.copy()

        while len(new_population) < population_size:
            p1 = tournament_selection(scored, tournament_k)
            p2 = tournament_selection(scored, tournament_k)
            while p1 == p2:
                p2 = tournament_selection(scored, tournament_k)
            child = crossover(p1, p2)
            child = mutate(child, mutation_rate, mutation_std)
            new_population.append(child)

        population = new_population

        print(f"Geração {gen}: Melhor fitness da população = {scored[0][1]:.2f}, Global = {best_score:.2f}")

    return best_individual, best_score