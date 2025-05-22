import random

def create_individual(individual_size):
    return [random.uniform(-1, 1) for _ in range(individual_size)]

def generate_population(individual_size, population_size):
    return [create_individual(individual_size) for _ in range(population_size)]

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:]

def mutate(individual, mutation_rate):
    return [gene + random.uniform(-0.5, 0.5) if random.random() < mutation_rate else gene for gene in individual]

def genetic_algorithm(individual_size, population_size, fitness_function, target_fitness, generations, elite_rate=0.2, mutation_rate=0.05):
    population = generate_population(individual_size, population_size)
    best_individual = None
    best_fitness = float('-inf')

    elite_count = int(population_size * elite_rate)

    for generation in range(generations):
        # Avaliar fitness
        fitnesses = [(ind, fitness_function(ind, seed=42)) for ind in population]
        fitnesses.sort(key=lambda x: x[1], reverse=True)

        # Atualizar melhor
        if fitnesses[0][1] > best_fitness:
            best_individual, best_fitness = fitnesses[0]

        print(f"Generation {generation+1}: Best Fitness = {fitnesses[0][1]}")

        if best_fitness >= target_fitness:
            break

        # Elitismo
        elites = [ind for ind, _ in fitnesses[:elite_count]]

        # Gerar nova população
        new_population = elites.copy()

        while len(new_population) < population_size:
            parent1, parent2 = random.choices(elites, k=2)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population

    return best_individual, best_fitness