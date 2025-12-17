# main.py
import random
import argparse
import csv
from pathlib import Path

from game import start_game, get_score
from genetic import genetic_algorithm
from nn import create_network_architecture
from dt import train_decision_tree


STATE_SIZE = 1 + 3 * 3
MAX_SCORE = 100


def fitness(rnn, individual, seed):
    rnn.load_weights(individual)
    rnn.reset_state()
    random.seed(seed)

    def ai_player(state):
        value = rnn.forward(state)
        return -1 if value < 0 else 1

    return get_score(player=ai_player)


def train_ai_player(filename, population_size, generations):
    rnn = create_network_architecture(STATE_SIZE)
    individual_size = rnn.compute_num_weights()

    fitness_function = lambda individual, seed=None: fitness(rnn, individual, seed)

    best = genetic_algorithm(
        individual_size,
        population_size,
        fitness_function,
        MAX_SCORE,
        generations
    )

    with open(filename, 'w') as f:
        f.write(','.join(map(str, best[0])))


def load_ai_player(filename):
    file_path = Path(filename)
    if not file_path.exists():
        return None

    with open(filename, 'r') as f:
        weights = list(map(float, f.read().split(',')))

    rnn = create_network_architecture(STATE_SIZE)
    rnn.load_weights(weights)
    rnn.reset_state()

    def ai_player(state):
        value = rnn.forward(state)
        return -1 if value < 0 else 1

    return ai_player


def load_train_dataset(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        headers = next(reader)
        X, y = [], []
        for row in reader:
            X.append(row[1:-1])
            y.append(int(row[-1]))
    return X, y


def train_fruit_classifier(filename):
    X, y = load_train_dataset(filename)
    dt = train_decision_tree(X, y)
    return lambda item: dt.predict(item)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--train', action='store_true')
    parser.add_argument('--population', type=int, default=100)
    parser.add_argument('--generations', type=int, default=100)
    parser.add_argument('--file', default='best_individual.txt')
    parser.add_argument('--headless', action='store_true')
    args = parser.parse_args()

    if args.train:
        train_ai_player(args.file, args.population, args.generations)
        return

    ai_player = load_ai_player(args.file)
    fruit_classifier = train_fruit_classifier('data/train.csv')

    if args.headless:
        score = get_score(ai_player, fruit_classifier)
        print(f'Score: {score}')
    else:
        start_game(ai_player, fruit_classifier)


if __name__ == '__main__':
    main()