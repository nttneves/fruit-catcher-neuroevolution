# Fruit Catcher – Neuroevolution with Recurrent Neural Networks

This project implements an AI agent capable of playing the **Fruit Catcher** game using
**neuroevolution with a recurrent neural network (RNN)**.

Unlike standard feedforward approaches, the agent uses internal memory to cope with
partial observability, learning temporal patterns such as object trajectories without
explicit velocity information.

---

## About the Project

Fruit Catcher is a simple arcade-style game where a basket must catch falling fruits
while avoiding bombs disguised as fruits.  
The challenge lies in the fact that the game state does not explicitly provide temporal
information such as object velocity, making the environment partially observable.

To address this, the AI agent uses a **recurrent neural network evolved with a genetic
algorithm**, allowing it to implicitly learn temporal dynamics through memory.

---

## Game Description

- A basket moves horizontally at the bottom of the screen
- Fruits and bombs fall from the top
- The goal is to:
  - Catch fruits
  - Avoid bombs
- The game ends when:
  - A bomb is caught
  - A fixed number of fruits has been dropped

---

## Usage

### Dependencies

- Python 3.10 or higher  
- numpy  
- pygame  

All dependencies can be installed using:

```bash
pip install numpy pygame
```
---

## AI Architecture

### State Representation

The input state is fixed and contains **10 numerical values**:
- Basket horizontal position
- Position and type (fruit or bomb) of the 3 nearest falling objects

### Neural Network

- Simple **Recurrent Neural Network (RNN)**
- Internal hidden state provides memory across time steps
- Output is a continuous value:
  - Negative value → move left
  - Positive value → move right

### Training Method

- **Genetic Algorithm (Neuroevolution)**
- No gradient descent or backpropagation
- Each individual represents a complete set of network weights
- Fitness is evaluated by running a full game episode

This approach corresponds to **Recurrent Neuroevolution**, treating the network as a
black-box policy.

---

## Fruit Classification

A **Decision Tree classifier** is trained to distinguish:
- Fruits (safe to catch)
- Bombs (must be avoided)

The classifier is trained using categorical features:
- Name
- Color
- Shape

It is used online by the agent during gameplay to label falling objects.

---

## Project Structure
```
.
├── game.py                 # Game engine (provided)
├── main.py                 # Entry point (training and gameplay)
├── nn.py                   # Recurrent Neural Network
├── genetic.py              # Genetic Algorithm
├── dt.py                   # Decision Tree classifier
├── images/                 # Game assets
├── data/                   # Datasets
│   ├── items.csv           # Full dataset
│   ├── train.csv           # Training data for decision tree
│   └── test.csv            # Test data for decision tree
└── best_individual.txt     # Best evolved network weights
```
---

## How to Run

### Train the AI agent

```bash
python main.py --train --population 100 --generations 100
```

## Play with the trained AI
```bash
python main.py
```

## Run without graphics (evaluation mode)
```bash
python main.py --headless
```

## Key Concepts
	•	Neuroevolution
	•	Recurrent Neural Networks
	•	Partial observability
	•	Genetic Algorithms
	•	Decision Trees
	•	Agent-based control

## Notes
	•	The RNN internal state is reset at the beginning of each episode
	•	A fixed random seed is used per generation to ensure fair fitness comparison
	•	The project is fully self-contained and does not rely on external ML frameworks

## Authors

- Nuno Neves

- Beatriz Nunes

## License

This project was developed as an academic work.


